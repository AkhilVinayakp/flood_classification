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

labels = [0, 0.19]

#creating an empty dataframe to store new data
a = np.zeros(shape=(902,28))
nd = pd.DataFrame(a, columns = [
        'gx_mean','gx_median','gx_variance',
        'gy_mean','gy_median','gy_variance',
        'gz_mean','gz_median','gz_variance',
        'ax_mean','ax_median','ax_variance',
        'ay_mean','ay_median','ay_variance',
        'az_mean','az_median','az_variance',
        'wx_mean','wx_median','wx_variance',
        'wy_mean','wy_median','wy_variance',
        'wz_mean','wz_median','wz_variance',
        'label'
        ])

k = 0 # keeping the row index of the new dataFrame

# creating time domain data 
for l in labels:
    dl = data[data["label"]== l].iloc[:,:-1]
    row_max = dl.shape[0]-1
    # assigning the highest multiple of 50 less than row_max
    fn_row = row_max - row_max % 50
    i, j = 0, 50
    while(True):
        if j > fn_row:
            break
        for col in dl.columns:
            nd[col+"_mean"][k] = dl[col].iloc[i:j].mean()
            nd[col+"_median"][k] = dl[col].iloc[i:j].median()
            nd[col+"_variance"][k] = dl[col].iloc[i:j].var()
            nd['label'][k] = l

        i = i + 25
        j = j + 25
        k = k + 1
        print(i,j)
          

nd.to_csv("windowed.csv")


'''            
nd[col+"_mean"] = dl[col].iloc[i:j].mean()
nd[col+"_median"] = dl[col].iloc[i:j].median()
nd[col+"_variance"] = dl[col].iloc[i:j].var()
print(dl[col].iloc[i:j].mean())
'''
    
