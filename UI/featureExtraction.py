import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import librosa
from sklearn.preprocessing import StandardScaler
import io
from scipy.io import wavfile
import warnings
warnings.filterwarnings("ignore")  # Ignore all warnings
from joblib import load

def extract_features(audio_data, sr):
     
    features = {}
    # Existing Librosa Features
    features["chroma_stft"] = librosa.feature.chroma_stft(y=audio_data, sr=sr)
    features["chroma_cqt"] = librosa.feature.chroma_cqt(y=audio_data, sr=sr)
    features["chroma_cens"] = librosa.feature.chroma_cens(y=audio_data, sr=sr)
    features["melspectrogram"] = librosa.feature.melspectrogram(y=audio_data, sr=sr)
    features["mfccs"] = librosa.feature.mfcc(y=audio_data, sr=sr)
    features["rms"] = librosa.feature.rms(y=audio_data)
    features["spectral_centroid"] = librosa.feature.spectral_centroid(y=audio_data, sr=sr)
    features["spectral_bandwidth"] = librosa.feature.spectral_bandwidth(y=audio_data, sr=sr)
    features["spectral_contrast"] = librosa.feature.spectral_contrast(y=audio_data, sr=sr)
    features["spectral_flatness"] = librosa.feature.spectral_flatness(y=audio_data)
    features["spectral_rolloff"] = librosa.feature.spectral_rolloff(y=audio_data, sr=sr)
    features["poly_features"] = librosa.feature.poly_features(y=audio_data, sr=sr)
    features["zero_crossing_rate"] = librosa.feature.zero_crossing_rate(y=audio_data)
    # Additional Librosa Features
    features["harmonic_centroid"] = librosa.feature.spectral_centroid(y=librosa.effects.harmonic(audio_data), sr=sr)
    features["harmonic_tonnetz"] = librosa.effects.harmonic(librosa.feature.tonnetz(y=audio_data, sr=sr))
    features["harmonic_rms"] = librosa.feature.rms(y=librosa.effects.harmonic(audio_data))
    features["harmonic_spectral_flatness"] = librosa.feature.spectral_flatness(y=librosa.effects.harmonic(audio_data))
    features["harmonic_spectral_contrast"] = librosa.feature.spectral_contrast(y=librosa.effects.harmonic(audio_data), sr=sr)
    features["harmonic_spectral_rolloff"] = librosa.feature.spectral_rolloff(y=librosa.effects.harmonic(audio_data), sr=sr)
    features["harmonic_zero_crossing_rate"] = librosa.feature.zero_crossing_rate(y=librosa.effects.harmonic(audio_data))
        
    return features

def calculate_mean(features):
    
    mean=[]
    for feature_name, feature_values in features.items():
        # Calculate mean
        feature_mean = np.mean(feature_values, axis=1)
        Final_feature_mean=np.mean(feature_mean, axis=0)
        mean.append(Final_feature_mean)
    return mean

def compute_features(X):

    audio_data, sr = librosa.load(X)
    features = extract_features(audio_data, sr)
    mean= calculate_mean(features)
    #this will pass to pre processing function
    return mean


class Data_Preprocessing:
    def __init__(self, X):
        self.dataset = pd.read_csv("data.csv")
        self.X = X

    def get_X(self):
        return np.array(self.X)
    
    def scaling_data(self, X):
        
        XX=self.dataset.iloc[:,:-1].values
        y=self.dataset.iloc[:,-1].values
        x_train,x_test,y_train,y_test=train_test_split(XX,y,test_size=0.25,stratify=y,random_state=42)
        ss = StandardScaler()
        self.x_train=ss.fit_transform(x_train)
        self.x_test=ss.transform(x_test)
        X_scaled = ss.transform([X])
        
        return  X_scaled

    def preprocessing(self):
        X = self.get_X()
        features = self.scaling_data(X)
#         print("Scaled features : ",features)
        return features
        