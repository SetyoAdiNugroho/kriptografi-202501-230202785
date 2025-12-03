# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: Cipher Modern  
Nama: Setyo Adi Nugroho  
NIM: 230202785
Kelas: 5 IKKA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Mengimplementasikan algoritma DES untuk blok data sederhana.
Menerapkan algoritma AES dengan panjang kunci 128 bit.
Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.
---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
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

```python
# from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)
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

- Pertanyaan 1: Perbedaan yang paling mendasar antara DES, AES, dan RSA adalah pada jenis kriptografi yang mereka gunakan yaitu mekanisme kunci dan tingkat keamanan yang dihasilkan. Pada DES dan AES adalah algoritma kriptografi simetris (menggunakan satu kunci rahasia untuk enkripsi dan dekripsi), sementara RSA adalah algoritma kriptografi asimetris atau kunci publik (menggunakan sepasang kunci, publik dan privat). 
- Pertanyaan 2: AES jauh lebih banyak digunakandibandingkan dengan DES dikarenakan beebrapa faktor yaitu keamanan superior, panjang kunci yang lebih besar, dan efisiensi yang lebih baik. DES memiliki kelemahan keamanan fatal yang disebabkan oleh panjang kuncinya yang pendek. Sedangkan pada AES menawarkan keamanan yang tak tertandingi dengan kunci yang jauh lebih panjang, sekaligus memberikan kecepatan pemrosesan yang superior, menjadikannya pilihan ideal untuk tuntutan data dan keamanan di era digital. Oleh karena itu DES dianggap usang karenakan tidak lagi aman terhadap serangan komputasi modern.
- Pertanyaan 3: RSA dikategorikan sebagai algoritma kriptografi asimetris atau kunci publik karena dia menggunakan dua kunci yang berbeda dan saling terkait secara matematis untuk proses enkripsi dan dekripsi yaitu Kunci Publik dan Kunci Privat.
Berbeda dengan kriptografi simetris (seperti AES) yang menggunakan satu kunci yang sama, dalam RSA kunci untuk enkripsi dapat diumumkan secara bebas, sementara kunci untuk dekripsi harus dijaga kerahasiaannya.
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
