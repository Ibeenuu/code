import pandas as pd


df = pd.read_csv('data_kantin.csv')

print(df.duplicated().sum())
df = df.drop_duplicates()

df['harga'] = df['harga'].astype(int)
print(df.dtypes)
