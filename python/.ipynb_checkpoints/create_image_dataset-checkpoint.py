# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:40:02 2020

@author: miapr
"""
from PIL import Image
from numpy import array
import matplotlib.pyplot as plt
import librosa
import librosa.display
import os
import numpy as np 

def create_image_set(dataset):
    res_set = []
    for each in dataset:
        fig = plt.figure(figsize=(6, 4))
        filename = "..\\ravdess-emotional-speech-audio\\" + each
        y, sr = librosa.load(filename)
        begin = librosa.time_to_samples(1)
        mid = librosa.time_to_samples(2.5)
        y = y[begin:mid]
        spect = librosa.feature.melspectrogram(y=y, sr=sr)
        spect = librosa.power_to_db(spect, ref=np.max)
        librosa.display.specshow(spect, y_axis='mel', x_axis='time', cmap='gray_r')
        image_name = "..\\images\\temp\\" + each.split(".")[0]
        fig.savefig(image_name)
        plt.close()
        im_1 = Image.open(image_name + ".png")
        ar = array(im_1)
        res_set.append(ar)
        os.remove(image_name + ".png") 
        
    return np.asarray(res_set)
    
if __name__ == '__main__':
    print('hello')