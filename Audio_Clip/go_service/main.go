package main

import (
	"bytes"
	"fmt"
	"os"
	"time"

	"github.com/gordonklaus/portaudio"
	"github.com/youpy/go-wav"
)

const (
	sampleRate   = 16000
	seconds      = 5 // Change to desired chunk duration
	channels     = 1
	chunkSamples = sampleRate * seconds
)

type MLResponse struct {
	Label string `json:"label"` // "cry" or "noise"
}

func main() {
	// Ensure output directory exists
	outDir := "cry_segments"
	if _, err := os.Stat(outDir); os.IsNotExist(err) {
		if err := os.Mkdir(outDir, 0755); err != nil {
			panic(fmt.Sprintf("Failed to create output directory: %v", err))
		}
	}
	portaudio.Initialize()
	defer portaudio.Terminate()

	// List all input devices
	devices, err := portaudio.Devices()
	if err != nil {
		panic(err)
	}
	fmt.Println("Available input devices:")
	for i, dev := range devices {
		if dev.MaxInputChannels > 0 {
			fmt.Printf("[%d] %s\n", i, dev.Name)
		}
	}

	var deviceIndex int
	fmt.Print("Enter input device index: ")
	_, err = fmt.Scanf("%d", &deviceIndex)
	if err != nil || deviceIndex < 0 || deviceIndex >= len(devices) || devices[deviceIndex].MaxInputChannels == 0 {
		fmt.Println("Invalid device index.")
		return
	}

	selectedDevice := devices[deviceIndex]
	in := make([]int16, chunkSamples)
	params := portaudio.StreamParameters{
		Input: portaudio.StreamDeviceParameters{
			Device:   selectedDevice,
			Channels: channels,
			Latency:  selectedDevice.DefaultLowInputLatency,
		},
		SampleRate:      float64(sampleRate),
		FramesPerBuffer: len(in),
	}
	stream, err := portaudio.OpenStream(params, in)
	if err != nil {
		panic(err)
	}
	defer stream.Close()

	if err := stream.Start(); err != nil {
		panic(fmt.Sprintf("Failed to start stream: %v", err))
	}
	defer stream.Stop()

	fmt.Println("Recording... Press Ctrl+C to stop.")
	chunk := make([]int16, 0, chunkSamples)
	for {
		err := stream.Read()
		if err != nil {
			fmt.Println("Audio read error:", err)
			continue
		}
		chunk = append(chunk, in...)
		if len(chunk) < chunkSamples {
			continue
		}

		// Encode to WAV in memory (mono)
		wavBuf := new(bytes.Buffer)
		writer := wav.NewWriter(wavBuf, uint32(len(chunk)), uint16(channels), uint32(sampleRate), 16)
		samples := make([]wav.Sample, len(chunk))
		for i, sample := range chunk {
			samples[i] = wav.Sample{Values: [2]int{int(sample), 0}}
		}
		if err := writer.WriteSamples(samples); err != nil {
			fmt.Println("WAV write error:", err)
			chunk = chunk[:0]
			continue
		}

		// Always save the chunk as a WAV file
		filename := fmt.Sprintf("%s/cry_%s.wav", outDir, time.Now().Format("20060102_150405"))
		f, err := os.Create(filename)
		if err != nil {
			fmt.Println("File save error:", err)
			chunk = chunk[:0]
			continue
		}
		wavBuf.WriteTo(f)
		f.Close()
		fmt.Println("Saved:", filename)
		chunk = chunk[:0] // Reset for next chunk
	}
}
