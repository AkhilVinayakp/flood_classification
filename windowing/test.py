# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os

# setting the root directory as the corrent working directory
os.chdir("/home/po/projects/flood_classification/")
'''
data = pd.read_csv("windowed.csv")
b = data[['gx_mean','gx_median','label']]
'''
data = pd.read_csv(os.path.join("data","filt_data.csv"))
