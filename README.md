import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\LENOVO\Desktop\PYTHON C-2\data_set CA-2.csv")

print(df.head())

print(df.info())

print(df.isnull().sum())

df.fillna(0, inplace=True)

print(df.describe())

# Total Yield by Crops
plt.figure(figsize=(10, 6))
sns.barplot(x='Crops', y='yeilds', data=df, estimator=sum)
plt.title('Total Yield by Crop')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Average Price by Crops 
avg_price = df.groupby('Crops')['price'].mean()
plt.figure(figsize=(8, 8))
plt.pie(avg_price, labels=avg_price.index, autopct='%1.1f%%', startangle=140)
plt.title('Average Price Distribution by Crop')
plt.tight_layout()
plt.show()

# Top 10 Crops 
top_crops = df.groupby('Crops')['yeilds'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_crops.plot(kind='bar')
plt.title('Top 10 Crops by Total Yield')
plt.ylabel('Yield')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation Heatmap 
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Scatter: Price vs Yield  by Soil type
plt.figure(figsize=(8, 6))
sns.scatterplot(x='yeilds', y='price', hue='Soil type', data=df)
plt.title('Price vs Yield by Soil Type')
plt.tight_layout()
plt.show()
