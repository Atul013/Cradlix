import joblib
import librosa
import numpy as np

# Define constants for feature extraction
n_fft = 2048
hop_length = 512
win_length = 2048
n_mels = 128
n_bands = 6
fmin = 20.0

def extract_features(file_path):
    try:
        # Load audio file and extract features
        y, sr = librosa.load(file_path, sr=16000)
        
        # Extract MFCC features (40 features)
        mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40, 
                                           n_fft=n_fft, hop_length=hop_length,
                                           win_length=win_length).T, axis=0)
        
        # Extract Mel spectrogram features (128 features)
        mel = np.mean(librosa.feature.melspectrogram(y=y, sr=sr, n_fft=n_fft,
                                                    hop_length=hop_length,
                                                    win_length=win_length,
                                                    window='hann',
                                                    n_mels=n_mels).T, axis=0)
        
        # Extract STFT and related features
        stft = np.abs(librosa.stft(y))
        
        # Chroma features (12 features)
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr, n_chroma=12).T, axis=0)
        
        # Spectral contrast features (7 features, 6 bands + 1 valley)
        contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sr,
                                                           n_fft=n_fft,
                                                           hop_length=hop_length,
                                                           win_length=win_length,
                                                           n_bands=n_bands,
                                                           fmin=fmin).T, axis=0)
        
        # Tonnetz features (6 features)
        tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr).T, axis=0)
        
        # Add spectral rolloff (1 feature)
        rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr).T, axis=0)
        
        # Concatenate all features (40 + 128 + 12 + 7 + 6 + 1 = 194 features)
        features = np.concatenate((mfcc, mel, chroma, contrast, tonnetz, rolloff))
        return features
    
    except Exception as e:
        print(f"Error: Exception occurred in feature extraction - {str(e)}")
        return None

def predict_cry(file_path):
    try:
        # Load the saved model and LabelEncoder
        model_path = 'e:/Projects/Cradlix/ver 2.0/baby-cry-classification/model.joblib'
        label_path = 'e:/Projects/Cradlix/ver 2.0/baby-cry-classification/label.joblib'
        loaded_model = joblib.load(model_path)
        loaded_le = joblib.load(label_path)
        
        # Extract features from the audio file
        features = extract_features(file_path)
        
        if features is not None:
            # Reshape features to match the input shape expected by the model
            features = features.reshape(1, -1)
            
            # Make prediction
            prediction = loaded_model.predict(features)
            
            # Convert prediction back to original label
            predicted_label = loaded_le.inverse_transform(prediction)
            
            return predicted_label[0]
        else:
            return "Error: Could not extract features from the audio file"
            
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    while True:
        # Get the audio file path from user
        file_path = input("\nEnter the path to the audio file (or 'q' to quit): ").strip('"').strip("'")
        
        if file_path.lower() == 'q':
            break
            
        # Make prediction
        result = predict_cry(file_path)
        print(f"\nPredicted cry type: {result}")

if __name__ == "__main__":
    print("Baby Cry Classifier")
    print("------------------")
    print("This program classifies baby cries into different categories.")
    print("Make sure your audio file is in WAV format.")
    main()
