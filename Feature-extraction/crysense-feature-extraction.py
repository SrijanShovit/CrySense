import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse

def compute_mfcc(file, num_cepstral_coeff = 13,energy = False):
    signal, rate= librosa.load(file)
    mfccs = librosa.feature.mfcc(y=signal, sr=rate, n_mfcc=num_cepstral_coeff)
    if energy:
        mfccs[0,:]= np.log(np.sum(np.square(signal)))
    return mfccs

def compute_chroma_features(file):
    signal,rate = librosa.load(file)
    chroma = librosa.feature.chroma_stft(y=signal,sr=rate)

    return chroma

def compute_spectral_contrast(audio_file):
 
    signal, rate = librosa.load(audio_file)
    spectral_contrast = librosa.feature.spectral_contrast(y=signal, sr=rate)

    return spectral_contrast

def plot_features(feature,title):
    plt.figure(figsize=(10, 4))

    librosa.display.specshow(feature, x_axis='time')
    
    plt.colorbar()
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is parser to take arguments filepath and feature_name")

    parser.add_argument('--file_path' , type=str, help="audio file of type .wav path")
    parser.add_argument('--feature_name', type=str, help="feature name among mfcc spectral_contrast chrome_features ")

    args =parser.parse_args()

    file = args.file
    feature =args.feature_name


    function_name = f"compute_{feature}"

# Check if the function exists
if hasattr(locals(), function_name) and callable(locals()[function_name]):
    # Call the function dynamically
    dynamic_function = getattr(locals(), function_name)
    feature_values = dynamic_function(file)


