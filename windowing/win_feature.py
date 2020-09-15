#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:19:11 2020
status : ok
@author: po
"""

import numpy as np
import pandas as pd
import os
import scipy.fftpack as fftpack

# setting the root directory as the corrent working directory
os.chdir("/home/po/projects/flood_classification/")
data = pd.read_csv(os.path.join("data","filt_data.csv"))
'''
50 consecutive
readings when data is recorded at 10Hz, with an overlap
of 25 readings between consecutive examples

window_size = 50
overlap = 25

since overlap is set to 25 per window then total number of windows for 
a class c will be c/25

'''
def call_ftt(frame):
    fft = fftpack.fft(np.array(frame))
    amplitudes = np.abs(fft)
    coe = amplitudes[0:5]
    return np.sum(coe)


def energy(frame):
    fft = fftpack.fft(np.array(frame))
    amplitudes = np.abs(fft)
    coe = amplitudes[1:26]
    power = coe ** 2
    return np.sum(power)/25


labels = [0,0.19,4.5,2.5]

#creating an empty dataframe to store new data
a = np.zeros(shape=(902,46))
nd = pd.DataFrame(a, columns = [
        'gx_mean','gx_median','gx_variance','gx_fft','gx_spec_energy',
        'gy_mean','gy_median','gy_variance','gy_fft','gy_spec_energy',
        'gz_mean','gz_median','gz_variance','gz_fft','gz_spec_energy',
        'ax_mean','ax_median','ax_variance','ax_fft','ax_spec_energy',
        'ay_mean','ay_median','ay_variance','ay_fft','ay_spec_energy',
        'az_mean','az_median','az_variance','az_fft','az_spec_energy',
        'wx_mean','wx_median','wx_variance','wx_fft','wx_spec_energy',
        'wy_mean','wy_median','wy_variance','wy_fft','wy_spec_energy',
        'wz_mean','wz_median','wz_variance','wz_fft','wz_spec_energy',
        'label'
        ])

k = 0 # keeping the row index of the new dataFrame

# defining the functions to calculate the sum of coefficients of fft
# done above



# creating time domain data 
for l in labels:
    dl = data[data["label"]== l].iloc[:,:-1]
    row_max = dl.shape[0]
    # assigning the highest multiple of 50 less than row_max
    fn_row = row_max - row_max % 50
    i, j = 0, 50
    while(True):
        print(i,j,k)
#         print(k)
        
        for col in dl.columns:
            nd[col+"_mean"][k] = dl[col].iloc[i:j].mean()
            #print(nd[col+"_mean"][k] )
            nd[col+"_median"][k] = dl[col].iloc[i:j].median()
            nd[col+"_variance"][k] = dl[col].iloc[i:j].var()
            nd[col+"_fft"][k] = call_ftt(dl[col].iloc[i:j].values)
            nd[col+"_spec_energy"][k] = energy(dl[col].iloc[i:j].values)
#             print(np.array(dl[col].iloc[i:j]))
            nd['label'][k] = l
            
        
        i = i + 25
        j = j + 25
        k = k + 1
        if i >= fn_row:
            break
        
nd.to_csv(os.path.join("data","win_data.csv"),index=False)