# Kaggle competition - PUBG

# Import libraries
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Select current path
PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(PATH, 'data')

# Read file
df = pd.read_csv(INPUT_PATH + '/train_V2.csv')

# Split features with labels
train = df.loc[:, df.columns != 'winPlacePerc']
labels = df['winPlacePerc']
col_names = list(df.columns.values)

# EDA
data = train.copy()
data = data[data['kills']==0]
plt.figure(figsize=(15,10))
plt.title("Damage Dealt by 0 killers",fontsize=15)
sns.distplot(data['damageDealt'])
plt.show()
