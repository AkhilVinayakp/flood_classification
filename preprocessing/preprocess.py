import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir("/home/po/projects/flood_classification/")
data = pd.read_csv(os.path.join("data","win_data.csv"))
fft = data[["gx_fft","label"]]
plt.plot(fft['gx_fft'], fft['label'])