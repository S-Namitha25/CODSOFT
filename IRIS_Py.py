import pandas as pd
file_path = 'IRIS.csv'  
df = pd.read_csv(file_path)
print("First few rows of the dataset:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nSummary statistics:")
print(df.describe())
print("\nDistribution of species:")
print(df['species'].value_counts())
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(df, hue='species')
plt.show()
