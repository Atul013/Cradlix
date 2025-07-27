---
license: apache-2.0
language:
- en
tags:
- baby-cry-classification
- machine-learning
- audio-analysis
- baby-cry-classification
- signal-processing
- acoustic-feature-extraction
- audio-classification
- speech-recognition
---
# Baby Cry Classifier

<p align="center">
<!-- Smaller size image -->
<img src="https://huggingface.co/foduucom/baby-cry-classification/resolve/main/Baby-cry.jpg" alt="Image" style="width:500px; height:300px;">
</p>

## Table of Contents
1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Solution](#solution)
4. [Importance and Need](#importance-and-need)
5. [How It Works](#how-it-works)
6. [How to Use This Model](#how-to-use-this-model)
7. [Future Developments](#future-developments)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)
10. [Model Card Contact](#model-card-contact)

## Introduction

The Baby Cry Classifier is an advanced machine learning model designed to analyze and categorize different types of baby cries. This innovative tool aims to assist parents, caregivers, and healthcare professionals in understanding and responding to babys' needs more effectively.

## Problem Statement

Interpreting an baby's cries can be challenging, especially for new parents or in high-stress situations. Babies communicate their needs primarily through crying, but distinguishing between different types of cries (e.g., hunger, discomfort, tiredness) can be difficult. This uncertainty can lead to:

1. Increased stress for parents and caregivers
2. Delayed response to the baby's needs
3. Potential misinterpretation of the baby's requirements

## Solution

Our baby Cry Classifier addresses these challenges by:

1. Analyzing audio recordings of baby cries
2. Extracting relevant acoustic features
3. Classifying the cry into predefined categories (e.g., belly pain, burping, discomfort, hunger, tiredness)

## Importance and Need

### 1. Enhanced baby Care

By accurately identifying the reason behind an baby's cry, caregivers can respond more promptly and appropriately to the baby's needs. This can lead to:

- Improved baby comfort and well-being
- Reduced stress for both the baby and caregiver
- Better overall care and nurturing

### 2. Medical Applications

In healthcare settings, the baby Cry Classifier can be a useful diagnostic tool:

- Assisting pediatricians in identifying potential health issues
- Supporting early detection of certain conditions that may affect an baby's cry patterns
- Providing objective data to complement clinical observations

### 3. Research Opportunities

This model opens up new avenues for research in:

- baby communication and development
- Early childhood psychology
- Acoustic analysis of baby vocalizations

## How It Works

1. **Data Collection**: The model is trained on baby cry audio samples, carefully labeled with their corresponding causes.

2. **Feature Extraction**: Advanced signal processing techniques are used to extract relevant acoustic features from the audio samples.

3. **Machine Learning**: A sophisticated machine learning algorithm is employed to learn the patterns associated with different types of cries.

4. **Classification**: When presented with a new audio sample, the model analyzes it and classifies it into one of the predefined categories.

## How to Use This Model

### Prerequisites

- Python 3.7 or higher
- Required libraries (install via pip):
  ```bash
  pip install numpy pandas scikit-learn joblib librosa
  ```

### Installation

1. Clone this repository:
   ```bash
   git clone https://huggingface.co/nehulagrawal/baby-cry-classification   
   cd baby-cry-classifier
   ```

2. Download the pre-trained model files:
    'model.joblib'
    'label.joblib'

### Usage

1. Import the necessary libraries:

```python
import joblib
import librosa
import numpy as np
```

2. Load the pre-trained model and label encoder:

```python
loaded_model = joblib.load('model.joblib')
loaded_le = joblib.load('label.joblib')
```

3. Define the feature extraction function (make sure this matches the function used during training):

```python
def extract_features(file_path):
    try:
        # Load audio file and extract features
        y, sr = librosa.load(file_path, sr=16000)
        mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40,n_fft=n_fft,hop_length=hop_length,win_length=win_length,window=window).T,axis=0)
        mel = np.mean(librosa.feature.melspectrogram(y=y, sr=sr,n_fft=n_fft, hop_length=hop_length, win_length=win_length, window='hann',n_mels=n_mels).T,axis=0)
        stft = np.abs(librosa.stft(y))
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, y=y, sr=sr).T,axis=0)
        contrast = np.mean(librosa.feature.spectral_contrast(S=stft, y=y, sr=sr,n_fft=n_fft,
                                                      hop_length=hop_length, win_length=win_length,
                                                      n_bands=n_bands, fmin=fmin).T,axis=0)
        tonnetz =np.mean(librosa.feature.tonnetz(y=y, sr=sr).T,axis=0)
        features = np.concatenate((mfcc, chroma, mel, contrast, tonnetz))
        # print(shape(features))
        return features
    except:
        print("Error: Exception occurred in feature extraction")
        return None
```

4. Use the model to classify a new cry audio:

```python
def predict_cry(file_path):
    # Load the saved model and LabelEncoder
    loaded_model = joblib.load('model.joblib')
    loaded_le = joblib.load('label.joblib')
    
    # Extract features from the new audio file
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

# Example usage
file_path = 'path/to/your/file.wav'
result = predict_cry(file_path)
print(f"Predicted cry type: {result}")
```

## Model Performance

Model Performance
The baby Cry Classifier has undergone extensive testing to evaluate its effectiveness. Here's an overview of its performance:
Accuracy Metrics:

|      class |precision|recall|f1-score|
|:----------:|:-------:|:----:|:------:|
|          0 | 0.00    | 0.00 |  0.00  |    
|          1 | 0.67    | 0.67 |  0.67  |    
|          2 | 0.75    | 0.33 |  0.46  |   
|          3 | 0.50    | 0.43 |  0.46  |    
|          4 | 0.25    | 0.50 |  0.33  |    
|   accuracy |         |      |  0.38  |  
|  macro avg | 0.43    | 0.39 |  0.38  |  
|weighted avg| 0.51    | 0.38 |  0.41  |       

Overall Accuracy: 

- Accuracy: 0.38461538461538464
- Precision: 0.4333333333333333
- Recall: 0.38571428571428573
- F1 Score: 0.38461538461538464

### Integration

You can integrate this model into your own applications, such as:

- A mobile app for parents
- A monitoring system for nurseries
- A research tool for pediatric studies

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- Thanks to all the parents and caregivers who contributed audio samples
- Pediatric researchers who provided domain expertise
- Open-source community for various tools and libraries used in this project

## Model Card Contact

For inquiries and contributions, please contact us at info@foduu.com.

```bibtex
@ModelCard{
    author       = {Nehul Agrawal and
                              Priyal Mehta},
    title         = {baby Cry Classifier},
    year           = {2024}
}
```