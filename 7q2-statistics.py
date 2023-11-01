import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearson3

df = pd.read_excel('./data/Bhadra Haralahalli.xlsx')
# df = pd.read_excel('./data/Bhadra Discharge data.xlsx')
df.columns = ['Date', 'Discharge']
df['Date'] = df['Date'].astype(str)
df['Date'] = df['Date'].str.replace(' 00:00:00', '')
df['Date'] = df['Date'].str.replace('-', '/')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.fillna(0, inplace=True)

# rolling window
df['Discharge'] = df['Discharge'].rolling(7).mean()
#drop all rows with 0 discharge
df = df[df['Discharge'] != 0]

df = df.groupby(pd.Grouper(key='Date', freq='Y')).min()
df = df.dropna()

params = pearson3.fit(df['Discharge'])
dist = pearson3(*params)

# find value which has non exceedance probability of 0.5, 0.9
q = dist.ppf(0.5)
print("7Q2 is: ", q)
q = dist.ppf(0.9)
print("7Q10 is: ", q)


