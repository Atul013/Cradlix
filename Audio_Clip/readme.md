# Cradlix Audio Baby Cry Detection

This project captures real-time audio from a microphone, chunks it into segments (default: 5 seconds), and saves each segment as a WAV file if a baby cry is detected by a Python ML microservice.

## How It Works

- The Go service (`go_service/main.go`) records audio from your selected input device.
- Audio is buffered into chunks (default: 5 seconds, configurable).
- Each chunk is sent to a Python ML microservice for baby cry detection.
- If a baby cry is detected, the chunk is saved as a timestamped WAV file in the `cry_segments` folder.
- Only valid baby cry segments are saved; other audio is ignored.

## Setup Instructions

### Prerequisites
- Go (1.18+ recommended)
- Python 3.8+
- PortAudio library (for Go audio capture)
- Microphone or audio input device

### 1. Install Go Dependencies
Open a terminal in `go_service` and run:
```
go mod tidy
```

### 2. Install PortAudio
- Download PortAudio for Windows: [PortAudio Downloads](http://www.portaudio.com/download.html)
- Place the DLL in your PATH or in the project directory.

### 3. Install Python Dependencies
Open a terminal in `python_ml_service` and run:
```
pip install flask soundfile
```

### 4. Start the Python ML Microservice
In `python_ml_service`, run:
```
python app.py
```
This will start the ML service on `localhost:5000`.

### 5. Run the Go Service
In `go_service`, run:
```
go run main.go
```
- Select your input device from the list.
- The service will start recording and processing audio.

### 6. Check Output
- Detected baby cry segments will be saved as WAV files in the `cry_segments` folder.
- If you want to change the chunk duration, edit the `seconds` constant in `main.go`.

## Troubleshooting
- If you get PortAudio errors, ensure the DLL is installed and accessible.
- If no files are saved, check that the Python ML service is running and reachable.
- If files are corrupt, ensure your audio device is working and the sample rate matches your hardware.

## Customization
- You can adjust the ML service logic in `python_ml_service/app.py`.
- Change chunk duration or sample rate in `go_service/main.go`.

## License
MIT
