# https://www.kaggle.com/uwrfkaggler/ravdess-emotional-speech-audio

import pandas as pd
from os import listdir
from os.path import isfile, join
import csv

mypath = "./ravdess-emotional-speech-audio/"
# Get a list of files in ravdess-emotional-speech-audio folder
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# The array that will be converted to a dataframe
for_df = []
for_emotion = []
# Going though each files and spliting them at the "-" 
# to make a file that will be used for surpervised learning
for each in onlyfiles:
    split_each = each.split('.wav')[0]
    split_each = split_each.split('-')
    for i in range(len(split_each)):
        split_each[i] = int(split_each[i])
    if split_each[len(split_each) - 1] % 2 == 0:
        split_each.append(2)
    else:
        split_each.append(1)
    split_each.insert(0, each)
    for_df.append(split_each)
    for_emotion.append([each,split_each[3]])

# convert array to dataframe
for_csv = pd.DataFrame(for_df, columns = ['file_name' , 'Modality', 'Voice_channel', 'Emotion', 'Intensity', 'Statement', 'Repetition', 'Actor', 'Gender']) 

# write dataframe to csv
for_csv.to_csv("./ravdess_audio_file_attributes.csv", sep=',',index=False)


emotions = pd.DataFrame(for_emotion, columns = ['file_name', 'Emotion'])
# 'neutral' , 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised'

x = pd.get_dummies(emotions['Emotion'])
emotions  = pd.concat([emotions, x], axis=1, join='inner')
emotions = emotions.drop(columns = ['Emotion'])
emotions.to_csv("./emotion.csv", sep=',',index=False)
