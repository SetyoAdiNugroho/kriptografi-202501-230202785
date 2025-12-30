# Laporan Praktikum Kriptografi
Minggu ke-: IX  
Topik: Digital Signature  
Nama: Setyo Adi Nugroho  
NIM: 230202785  
Kelas: 5 IKKA

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
Memverifikasi keaslian tanda tangan digital.
Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

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
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

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

- Pertanyaan 1: Perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA terletak pada tujuan penggunaan, pada enkripsi RSA kerahasiaan memastikan hanya penerima yang bisa membaca pesan sedangkan pada tanda tangan digital RSA otentikasi dan integritas memastikan pengirim adalah orang yang asli dan pesan tidak diubah. Perbedaan lain terletak pada urutan kunci yang digunakan dalam prosesnya, pada digital RSA kunci untuk mengunci menggunakan kunci publik penerima dan untuk membuka menggunakan kunci privat penerima, sedangkan pada tanda tangan digital RSA kunci untuk mengunci menggunakan kunci privat pengirim dan untuk membuka kunci menggunakan kunci publik pengirim. Meskipun keduanya menggunakan algoritma matematika yang sama, fungsinya sangat berbeda: satu untuk menjaga rahasia, yang lain untuk membuktikan keaslian.
- Pertanyaan 2: Tanda tangan digital mampu menjamin integritas dan otentikasi karena menggabungkan dua teknologi kriptografi yang kuat yaitu fungsi hash dan kriptografi kunci publik.
- Pertanyaan 3: Certificate Authority (CA) adalah entitas pihak ketiga tepercaya yang berperan sebagai "Notaris Digital" dimana CA berperan untuk memverifikasi identitas memastikan bahwa pemegang kunci privat adalah pihak yang sah. Kemudian CA menerbitkan Sertifikat Digital yang berisi kunci publik pengirim beserta informasi identitasnya, setelahnya CA menandatangani sertifikat tersebut dengan kunci privat milik CA sendiri. Ini membuktikan bahwa CA menjamin keaslian kunci publik tersebut.
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
