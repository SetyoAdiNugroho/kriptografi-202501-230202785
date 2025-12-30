# Laporan Praktikum Kriptografi
Minggu ke-: XII  
Topik:  Transport Layer Security
Nama: Setyo Adi Nugroho 
NIM: 230202785  
Kelas: 5 IKKA 

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
Menjelaskan enkripsi dalam transaksi e-commerce.
Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.
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

- Pertanyaan 1: Perbedaan mendasar antara HTTP (Hypertext Transfer Protocol) dan HTTPS (Hypertext Transfer Protocol Secure) terletak pada aspek keamanan. Secara sederhana, HTTPS adalah versi HTTP yang lebih aman.  Dari segi keamanan dan enkripsi pada HTTP data dikirimkan dalam bentuk teks biasa (plain text). Artinya, jika seseorang berhasil mencegat data tersebut (seperti kata sandi atau nomor kartu kredit), mereka bisa membacanya dengan mudah. Sedangkan pada HTTPS menggunakan protokol enkripsi yang disebut TLS (Transport Layer Security) atau dulunya SSL (Secure Sockets Layer). Data diacak sedemikian rupa sehingga tidak bisa dibaca oleh pihak ketiga saat sedang dikirim.
- Pertanyaan 2: Sertifikat digital dalam komunikasi TLS (Transport Layer Security) sangat penting karena berfungsi sebagai kartu identitas resmi di dunia digital. Tanpa sertifikat ini, enkripsi saja tidak cukup untuk menjamin keamanan. Tanpa sertifikat digital, komunikasi internet mungkin tetap terenkripsi, tetapi Anda tidak akan pernah tahu kepada siapa Anda mengirimkan informasi sensitif tersebut.
- Pertanyaan 3: Kriptografi adalah pedang bermata dua dalam dunia digital. Di satu sisi, ia adalah perisai terkuat untuk melindungi hak asasi manusia dan privasi, namun di sisi lain, ia menciptakan "ruang gelap" yang menyulitkan penegakan hukum. Sebab kriptografi modern, terutama Enkripsi End-to-End (E2EE), memastikan bahwa pesan hanya bisa dibaca oleh pengirim dan penerima. Akantetapi pemerintah dan lembaga penegak hukum (seperti FBI atau Kepolisian) sering mengeluhkan fenomena "Going Dark". Karena data terenkripsi total, mereka tidak bisa menyadap komunikasi penjahat, teroris, atau jaringan perdagangan manusia meskipun sudah memiliki surat izin penggeledahan resmi.
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
