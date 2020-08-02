# importing libraries
import pandas as pd
import numpy as nm
import os
# importing sklearn



# preprocessing functions TODO>> seperate file

def check_nan(data_frm):
    li = []
    for i in data_frm.columns:
        if any(list(data_frm[i].isnull())):
            li.append(i)
    return li

r_data = pd.read_csv(os.path.join("data","raw_data.csv"))
#print(r_data)

# data only available upto 22597 row . required features available from 3 to 11 
f_data = r_data.iloc[:22598,3:12]

# changing the column names of each 9 fileds
f_data.columns = ['gx','gy','gz','ax','ay','az','wx','wy','wz']

# extracting the y label ( output) of each observation into a separate series
y_data = r_data.iloc[:22598,-1]

# creating dataframe of f_data and y_data USE future data collecting & write to a file
f_data['label'] = y_data

f_data.to_csv(os.path.join('data','filt_data.csv'),index=False)


# checking for nan cells in any columns
nan_culumns= check_nan(f_data)

    

