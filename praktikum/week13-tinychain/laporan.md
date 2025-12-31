# Laporan Praktikum Kriptografi
Minggu ke-: XIII  
Topik:   
Nama: Setyo Adi Nugroho  
NIM: 230202785 
Kelas: 5 IKKA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menjelaskan peran hash function dalam blockchain.
Melakukan simulasi sederhana Proof of Work (PoW).
Menganalisis keamanan cryptocurrency berbasis kriptografi.

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
 
- Pertanyaan 1: Fungsi hash adalah "tulang punggung" yang menjaga integritas dan keamanan seluruh sistem blockchain. Tanpa fungsi hash, blockchain hanyalah sebuah basis data biasa yang mudah dimanipulasi. Sebab dalam blockchain setiap blok berisi hash dari blok sebelumnya, hal ini menciptakan rantai yang saling mengunci. Selain itu fungsi hash bersifat satu arah sangat mudah untuk menghasilkan hash dari data, tetapi secara matematis hampir mustahil untuk mendapatkan data asli hanya dari melihat nilai hash-nya. Ini melindungi privasi dan informasi sensitif dalam jaringan.
- Pertanyaan 2: Proof of Work (PoW) adalah mekanisme yang memastikan bahwa untuk mencatat transaksi ke dalam blockchain, seseorang harus mengeluarkan sumber daya nyata (daya komputasi dan listrik). Pengeluaran sumber daya inilah yang membuat manipulasi data, termasuk Double Spending (pengeluaran ganda), menjadi sangat sulit dan mahal.
- Pertanyaan 3: Meskipun Proof of Work (PoW) sangat tangguh dalam menjaga keamanan, efisiensi energi adalah tumit Achille-nya. Masalah utamanya bukan sekadar pada penggunaan listrik yang besar, tetapi pada cara energi tersebut digunakan. Dalam PoW, ribuan atau bahkan jutaan komputer di seluruh dunia (para penambang) berlomba menyelesaikan teka-teki matematika yang sama. Sistem PoW memiliki mekanisme otomatis untuk menjaga waktu pembuatan blok agar tetap stabil olehkarena itu jika penambang menggunakan komputer yang lebih canggih, sistem akan otomatis menaikkan tingkat kesulitan teka-tekinya. Dampaknya, meskipun teknologi perangkat keras semakin efisien, jaringan justru memaksa penggunaan daya yang lebih besar untuk menjaga tingkat keamanan yang sama.

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
