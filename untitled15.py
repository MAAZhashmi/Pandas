# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nOay5y_3nMLXB4L2bWkwU3CFs3bpNVsn
"""

# Commented out IPython magic to ensure Python compatibility.

import pandas as pd
import numpy as np
import os
import sys
import seaborn as sns; sns.set(color_codes=True)
from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
# %matplotlib inline

from google.colab import files
uploaded = files.upload()

df = pd.read_csv("cricket report.csv")

df.head(10)



df.notnull()

df.isnull().sum().sum()

df.shape

df.columns

df.describe



df.nunique()

df.info()

print(df.isna().sum(axis = 0))

df1 = df.groupby(['Player'],as_index=False)['4s','6s','SR','Runs']
df1

plt.plot(df['Player'],df['Runs'])
plt.title("Player Vs Runs")
plt.xlabel("Player")
plt.ylabel("Runs")
plt.show()



plt.plot(df['Player'],df['6s'])
plt.title("Player Vs 6s ")
plt.xlabel("Player")
plt.ylabel(" 6s")
plt.show()

plt.plot(df['Player'],df['SR'])
plt.title("Player Vs SR")
plt.xlabel("Player")
plt.ylabel("SR")
plt.show()

plt.plot(df['Player'],df['6s'])
plt.title("Player Vs 6s")
plt.xlabel("player")
plt.ylabel("6s")
plt.show()

df1.corr()

import seaborn as sns; sns.set(color_codes=True)

import seaborn as sns

sns.heatmap(df1.corr(), vmin=-1, vmax=1,
annot=True,cmap="rocket_r")
plt.show()