import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\LENOVO\Desktop\PYTHON C-2\data_set CA-2.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.fillna(0))

