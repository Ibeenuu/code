praktikum 1 - 3
<img width="1472" height="917" alt="Screenshot 2026-09-21 220507" src="https://github.com/user-attachments/assets/e10666d8-ff20-4d6b-869f-eb648da08ca1" />

praktikum 4-6
<img width="1482" height="697" alt="Screenshot 2026-09-21 220519" src="https://github.com/user-attachments/assets/eccc2ebe-7fb9-43b7-8a2b-47cf506eda94" />

tugas kelompok
<img width="1917" height="985" alt="Screenshot 2026-09-21 225824" src="https://github.com/user-attachments/assets/e37af278-465b-42bb-95ea-69daecc7eea3" />

<img width="1917" height="1078" alt="Screenshot 2026-09-21 225836" src="https://github.com/user-attachments/assets/65e3f069-f859-40f2-acf2-f70ca9b6250e" />

<img width="1917" height="348" alt="Screenshot 2026-09-21 225844" src="https://github.com/user-attachments/assets/e71b6ffd-44a3-4046-be5a-2e80411b8f66" />

Pertanyaan:
1. Produk paling banyak terjual?
2. Kategori omzet tertinggi?
3. Kasir dan metode pembayaran terbesar?

Cleaning:
- hapus 4 duplikat
- rapikan tanggal, Rp, pcs
- isi missing (harga dari harga produk, jumlah median, kasir modus)
- koreksi outlier Roti Bakar 500

Hasil:
- 69 baris → 65 baris bersih
- omzet Rp 3.418.000
- produk terlaris: Nasi Goreng
- kategori teratas: Makanan
- metode teratas: QRIS



## Praktikum 1-6

File: `Latihan1.py` sampai `Latihan6.py`

### Praktikum 1 — Operasi dasar pada data harga
Program menghitung ringkasan harga.
- Rata-rata harga: 7125
- Harga tertinggi: 12000
- Harga setelah diskon 10%: 4500, 6300, 10800, 4050

Analisis: Pandas/NumPy bisa menghitung banyak harga sekaligus. Diskon 10% dikalikan ke seluruh data, tidak perlu dihitung satu-satu.

### Praktikum 2 — Membuat tabel dan melihat data kosong
Output menampilkan 5 baris awal:
- Nasi Goreng, Mie Ayam, Es Teh
- Ada nilai kosong: `terjual` pada Es Teh, dan `menu` pada baris terakhir

Analisis: Data tidak selalu lengkap. NaN harus dicek dulu sebelum dijumlahkan, karena bisa membuat hasil omzet salah.

### Praktikum 3 — Loading dan inspeksi dataset
Dataset memiliki 110 baris dan 5 kolom.
- `tanggal`, `menu`, `kategori` bertipe teks
- `harga` bertipe int64
- `terjual` bertipe float64
- `menu` hanya 107 yang terisi (3 kosong)
- `terjual` hanya 104 yang terisi (6 kosong)
- Rata-rata harga 6336, rata-rata terjual 22,9
- Harga paling murah 2000, paling mahal 12000

Analisis: `info()`, `describe()`, dan `shape` dipakai untuk mengenal struktur data sebelum cleaning.

### Praktikum 4 — Cek missing value
Jumlah data kosong per kolom:
- tanggal 0
- menu 3
- kategori 0
- harga 0
- terjual 6

Analisis: Masalah utama ada di `menu` dan `terjual`. Kolom ini yang harus dibersihkan lebih dulu.

### Praktikum 5 — Cek tipe data
Dataset punya 5 kolom:
- tanggal: str
- menu: str
- kategori: str
- harga: int64
- terjual: float64

Analisis: `terjual` terbaca float karena ada nilai kosong. Kalau sudah bersih, tipe ini bisa diubah ke integer.

### Praktikum 6 — Agregasi total pendapatan per menu
Hasil `groupby` menu:
- Nasi Goreng 4.188.000
- Mie Ayam 2.570.000
- Es Teh 2.144.000
- Es Jeruk 1.560.000
- Roti Bakar 1.368.000
- Kerupuk 1.042.000
- Teh Hangat 459.000

Analisis: Nasi Goreng menyumbang pendapatan terbesar. Teh Hangat paling kecil. Groupby dipakai untuk menjawab menu mana yang paling menguntungkan.
