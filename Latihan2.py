import pandas as pd
data_kantin = {
'menu': ['Nasi Goreng', 'Mie Ayam', 'Es Teh', 'Es Teh', None],
'harga': [12000, 4000, 10000, 4000, 8000],
'terjual': [23, 40, None, 35, 18]
}
df = pd.DataFrame(data_kantin)
print(df)