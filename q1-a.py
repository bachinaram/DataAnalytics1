import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
df = pd.read_csv('/content/sample_data/football_data.csv')
df["Height"].fillna("0'0", inplace = True) 


a=[]
for i in df['Height']:
  H_feet = i.split("'")[0]
  H_inch = i.split("'")[1].split("\"")[0]
  H_inches = int(H_feet) * 12 + int(H_inch)
  a.append(H_inches)
sns.set(font_scale=1.4)
df1 = pd.DataFrame(a, columns =['Height'])
df1['Height'].hist(bins=100)
plt.xlabel("Height in inches", labelpad=14)
plt.ylabel("Players", labelpad=14)
plt.title("Count of players based on height", y=1.015, fontsize=22);
