# Laporan Praktikum Kriptografi
Minggu ke-: XI 
Topik: Secret Sharing
Nama: Setyo Adi Nugroho  
NIM: 230202785
Kelas: 5 IKKA 

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menjelaskan konsep Shamir Secret Sharing (SSS).
Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
Menganalisis keamanan skema distribusi rahasia.(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code
- Git dan akun GitHub 

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1: Perbedaan utama antara Shamir's Secret Sharing (SSS) dan sekadar membagikan salinan kunci secara langsung terletak pada keseimbangan antara keamanan (security) dan ketersediaan (availability). Jika anda hanya membagikan salinan kunci yang sama kepada 5 orang, risikonya sangat tinggi: jika satu orang saja berkhianat, rahasia anda terbongkar. Sebaliknya, jika anda hanya menyimpan satu kunci, dan kunci itu hilang, rahasia anda hilang selamanya.
- Pertanyaan 2: Dalam skema Shamir's Secret Sharing (SSS), threshold (k) adalah jumlah minimum bagian rahasia (shares) yang diperlukan untuk merekonstruksi kembali kunci asli.Peran k sangat krusial karena ia menentukan titik keseimbangan antara keamanan (mencegah akses tidak sah) dan ketersediaan (memastikan kunci bisa dipulihkan jika ada gangguan).
- Pertanyaan 3: Masalah Tanpa SSS:Jika kunci dipegang CEO saja: Jika CEO mengalami kecelakaan atau meninggal dunia secara mendadak (seperti kasus nyata QuadrigaCX), seluruh dana nasabah akan terkunci selamanya dan tidak bisa diambil.Jika kunci disalin ke 3 Direktur: Jika salah satu direktur berkhianat atau komputernya diretas, ia bisa mencuri seluruh dana sendirian tanpa persetujuan yang lain.Solusi Menggunakan SSS (Skenario k=3, n=5):Bursa tersebut menggunakan Shamir's Secret Sharing untuk memecah kunci utama menjadi 5 bagian (shares) yang dibagikan kepada:CEOKomisaris UtamaDirektur OperasionalKepala Keamanan (CISO)Brankas fisik di lokasi rahasia (sebagai cadangan)Dengan ambang batas k=3, manfaat yang didapat adalah:Keamanan dari Pencurian: Jika seorang peretas berhasil meretas laptop Kepala Keamanan, peretas tersebut tidak bisa mencuri dana karena ia hanya punya 1 bagian. Ia butuh minimal 2 bagian lagi dari pejabat lain.Keamanan dari Pengkhianatan: CEO tidak bisa melarikan dana sendirian. Ia harus meyakinkan setidaknya 2 orang lain untuk setuju melakukan transaksi.Ketahanan terhadap Bencana: Jika CEO dan Komisaris Utama sedang berada dalam satu pesawat yang sama dan terjadi kecelakaan, dana nasabah tetap aman dan bisa diakses karena 3 bagian lainnya (Direktur, CISO, dan Brankas) masih ada untuk merekonstruksi kunci.
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
