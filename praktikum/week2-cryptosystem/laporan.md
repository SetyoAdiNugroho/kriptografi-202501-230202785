# Laporan Praktikum Kriptografi
Minggu ke-: 2
Topik: [CRYPTOSYSTEM]  
Nama: [Setyo Adi Nugroho]  
NIM: [230202785]  
Kelas: [5IKKA]  

---

## 1. Komponen utama dalam sebuah kriptosistem (sistem kriptografi)

lima elemen fundamental yang bekerja sama untuk mengamankan data:

**Komponen Utama Kriptosistem**

**Pesan Asli *(Plaintext / Teks Terbuka)***
Ini adalah pesan atau data yang dapat dibaca dan dimengerti maknanya. Ini adalah input dari proses enkripsi.
Contoh: "Rahasia besar perusahaan."

**Algoritma Kriptografi *(Cipher)***
Ini adalah serangkaian instruksi atau prosedur matematika yang digunakan untuk mengubah pesan asli menjadi pesan terenkripsi (ciphertext), dan sebaliknya.
Contoh: Algoritma AES, RSA, atau fungsi hashing SHA-256.

**Kunci *(Key)***
Ini adalah informasi rahasia (bisa berupa angka, kata, atau serangkaian karakter biner) yang digunakan oleh algoritma untuk melakukan enkripsi dan dekripsi. Kekuatan keamanan kriptosistem hampir selalu bergantung pada kerahasiaan dan panjang kunci.
Jenis:
Kunci Simetris: Satu kunci untuk enkripsi dan dekripsi.
Kunci Asimetris: Pasangan kunci (publik dan privat) yang berbeda.

**Pesan Terenkripsi *(Ciphertext / Teks Sandi) ***
Ini adalah hasil dari proses enkripsi, yaitu pesan asli yang telah diubah menjadi bentuk yang tidak dapat dibaca atau dimengerti tanpa kunci yang benar. Ini adalah data yang ditransmisikan melalui saluran yang tidak aman.
Contoh: "Xm92nFh8Aop2Bq3Rz7yG" (tergantung pada algoritma yang digunakan).

**Prosedur Enkripsi dan Dekripsi**
Ini adalah dua proses fungsional yang menggunakan algoritma dan kunci:
Enkripsi: Proses mengubah plaintext menjadi ciphertext.
Dekripsi: Proses mengubah ciphertext kembali menjadi plaintext (hanya dapat dilakukan oleh penerima yang sah dengan kunci yang benar).

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

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
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
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
