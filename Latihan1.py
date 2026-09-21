import numpy as np

harga = np.array ([5000, 7000, 12000, 4500])
print ('Rata-rata harga:', harga.mean())
print ('Harga tertinggi:', harga.max())
print ('Harga setelah diskon 10%:', harga * 0.9)