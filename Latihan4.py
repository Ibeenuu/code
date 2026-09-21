import pandas as pd


df = pd.read_csv('data_kantin.csv')

print(df.isnull().sum())

df['terjual'] = df['terjual'].fillna(0)
df = df.dropna(subset=['menu'])