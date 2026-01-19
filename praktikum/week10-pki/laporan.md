# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik:  Public Key Infrastructure 
Nama: Setyo Adi Nugroho 
NIM: 230202785
Kelas: 5 IKKA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Membuat sertifikat digital sederhana.
Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

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

```
from cryptography import x509 # type: ignore
from cryptography.x509.oid import NameOID # type: ignore
from cryptography.hazmat.primitives import hashes, serialization # type: ignore
from cryptography.hazmat.primitives.asymmetric import rsa # type: ignore
from cryptography.hazmat.backends import default_backend # type: ignore
from datetime import datetime, timedelta, timezone

# Generate key pair
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
```

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

- Pertanyaan 1: Certificate Authority (CA) bertindak seperti "Kantor Imigrasi" digital yaitu berfungsi untuk memverifikasi identitas sebuah entitas (seperti situs web, perangkat, atau individu) dan menerbitkan sertifikat digital untuk membuktikan identitas tersebut. Tanpa CA, kita tidak akan pernah tahu apakah situs web yang kita buka benar-benar asli atau hanya halaman palsu yang mencoba mencuri data kita.
- Pertanyaan 2: Self-signed certificate tidak cukup untuk sistem produksi karena tidak ada pihak ketiga yang memvalidasi bahwa "Anda adalah Anda" dan siapa pun, termasuk penyerang, bisa membuat sertifikat palsu atas nama domain anda. Kemudian karena browser tidak bisa memverifikasi keaslian sertifikat, penyerang bisa mencegat koneksi dan menyisipkan sertifikat self-signed milik mereka sendiri.
- Pertanyaan 3: Public Key Infrastructure (PKI) mencegah serangan Man-in-the-Middle (MITM) bukan hanya melalui enkripsi, tetapi yang paling krusial adalah melalui otentikasi. Tanpa PKI, anda mungkin berkomunikasi secara terenkripsi, tetapi anda tidak tahu dengan siapa Anda berbicara. PKI memastikan bahwa kunci publik yang anda gunakan benar-benar milik server tujuan, bukan milik penyerang. 
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
