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
