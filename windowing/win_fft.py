# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os

# setting the root directory as the corrent working directory
os.chdir("/home/po/projects/flood_classification/")
data = pd.read_csv(os.path.join("data","filt_data.csv"))
'''
50 consecutive
readings when data is recorded at 10Hz, with an overlap
of 25 readings between consecutive examples
'''
window_size = 50
overlap = 25
'''
since overlap is set to 25 per window then total number of windows for 
a class c will be c/25

'''
# checking procedure
# selecting data belongs to label 0
data_l = data[data["label"]== 0].iloc[:,:-1]
print(data_l.shape) # 3503,9

# total nuber of windows  
total_windows_l = data_l.shape[0]//25
#OUT :  140 same as in paper

labels = [0,]

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
def cal_fft(df):
    coe = np.fft.rfft(df)
    with open('fft.txt','w') as f:
        f.write(str(coe))




# creating time domain data 
for l in labels:
    dl = data[data["label"]== l].iloc[:,:-1]
    row_max = dl.shape[0]-1
    # assigning the highest multiple of 50 less than row_max
    fn_row = row_max - row_max % 50
    i, j = 0, 50
    while(True):
        print(i,j,k)
        
        for col in dl.columns:
            nd[col+"_mean"][k] = dl[col].iloc[i:j].mean()
            #print(nd[col+"_mean"][k] )
            nd[col+"_median"][k] = dl[col].iloc[i:j].median()
            nd[col+"_variance"][k] = dl[col].iloc[i:j].var()
            cal_fft(dl[col].iloc[i:j].values)
            nd['label'][k] = l
            
        
        i = i + 25
        j = j + 25
        k = k + 1
        if i >= fn_row:
            break
        
          

nd.to_csv("windowed.csv")


'''            
nd[col+"_mean"] = dl[col].iloc[i:j].mean()
nd[col+"_median"] = dl[col].iloc[i:j].median()
nd[col+"_variance"] = dl[col].iloc[i:j].var()
print(dl[col].iloc[i:j].mean())
'''
    
