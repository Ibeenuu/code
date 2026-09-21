import pandas as pd


df = pd.read_csv('data_kantin.csv')

laris = df[df['terjual'] > 20]
urut = df.sort_values(by='terjual', ascending=False)

df['total_pendapatan'] = df['harga'] * df['terjual']

ringkasan = df.groupby('menu')['total_pendapatan'].sum()
print(ringkasan)