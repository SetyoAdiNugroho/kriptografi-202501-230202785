# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Cipher Klasik  
Nama: Setyo Adi Nugroho  
NIM: 230202785
Kelas: 5 IKKA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
Mengimplementasikan algoritma transposisi sederhana.
Menjelaskan kelemahan algoritma kriptografi klasik.

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

```python
# def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result
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
 
- Pertanyaan 1: Kelemahan utama Caesar Cipher adalah dia hanya menggunakan satu pergeseran tetap untuk setiap huruf di seluruh pesan, yang membuatnya sangat mudah dipecahkan. Hal ini disebabkan karena ruang kunci yang sangat kecil yaitu hanya ada 25 kunci potensial (pergeseran 1 hingga 25) yang dapat digunakan. Ini memungkinkan penyerang untuk menggunakan serangan brute force (mencoba semua kunci) dengan sangat cepat, bahkan secara manual.
  Sedangkan pada Vigenère Cipher meskipun jauh lebih aman daripada Caesar Cipher karena menggunakan kunci kata yang berulang, akan tetapi tetap memiliki kelemahan utama yaitu Vigenère Cipher adalah setelah panjang kunci diketahui, metode enkripsi sandi ini menjadi efektif setara dengan beberapa sandi Caesar yang mudah dipecahkan.
- Pertanyaan 2: Cipher klasik mudah diserang dengan analisis frekuensi sebab dia gagal menyembunyikan pola statistik alami dari bahasa yang digunakan. Hal ini mengakibatkan meskipun huruf dalam pesan asli diganti atau dipindahkan, frekuensi kemunculan setiap huruf dalam pesan terenkripsi akan secara langsung mencerminkan frekuensi huruf dalam pesan asli.
- Pertanyaan 3: Perbandingan utama antara Cipher Substitusi dan Cipher Transposisi terletak pada cara mereka mengubah plaintext (teks asli) menjadi ciphertext (teks sandi). Substitusi berfokus pada apa yang dienkripsi (mengganti huruf), sedangkan pada Transposisi berfokus pada di mana huruf-huruf itu berada (mengubah posisi).
  
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
