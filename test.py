import pandas as pd
import numpy as np
import os
'''
dataset = pd.read_csv(os.path.join("Ieee data","data","data","windowed","windowed_new_data.csv"))

dataset2 = dataset
dataset = dataset.drop([col for col in dataset.columns if  not col.find('MAGNETIC')], axis = 1)
dataset = dataset.drop([col for col in dataset.columns if  not col.find('ORIENTATION')], axis = 1)
dataset = dataset.drop([col for col in dataset.columns if  not col.find('ACCELEROMETER')], axis = 1)
dataset = dataset.drop([col for col in dataset.columns if  not col.find('PRT')], axis = 1)
dataset = dataset.drop([col for col in dataset.columns if  not col.find('std_dev')==-1], axis = 1)#input *std_dev for removing substring with std_dev


dataset = pd.read_csv(os.path.join("data","filt_data.csv"))
cols = dataset.columns
print(cols)
Y = dataset.iloc[:,-1]
x = dataset.values
print(len(x))

classes = [0,]
window = 50
stride = 25
for c in classes:
    class_raw_line = np.asarray([x[j, :-1] for j in range(0,len(x)) if Y[j] == c])
    # taking rows correponding to each class 
    #class_raw_line holds the class rows belogs to the first classification
    windowed_len = int(class_raw_line.shape[0] / stride)
'''
dataset = pd.read_csv(os.path.join("Ieee data","data","data","windowed","windowed_new_data.csv"))
d = dataset[['GRAVITY_X_mean','GRAVITY_X_median','OUT']]