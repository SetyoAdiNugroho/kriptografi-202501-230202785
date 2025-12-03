# Laporan Praktikum Kriptografi
Minggu ke-: 4 
Topik: Entropy Unicity  
Nama: Setyo Adi Nugroho  
NIM: 230202785  
Kelas: 5IKKA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menyelesaikan perhitungan sederhana terkait entropi kunci.
Menggunakan teorema Euler pada contoh perhitungan modular & invers.
Menghitung unicity distance untuk ciphertext tertentu.
Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
(- Python 3.x  
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
# import math
from typing import Iterable, Tuple

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_SIZE = len(ALPHABET)  # 26

# ---------------- Core crypto-metrics ----------------

def entropy_bits_from_keyspace(keyspace_size: int) -> float:
    if keyspace_size <= 0:
        raise ValueError("keyspace_size harus > 0")
    return math.log2(keyspace_size)
```

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

- Pertanyaan 1: Nilai entropi dalam konteks kekuatan kunci (kriptografi) adalah ukuran dari ketidakpastian atau keacakan suatu kunci. Semakin tinggi nilai entropinya, semakin kuat kunci tersebut dan semakin sulit bagi penyerang untuk menebak atau memecahkannya melalui serangan brute force (coba-coba).
- Pertanyaan 2: Jarak unicity (Unicity Distance) penting karena ia menentukan jumlah minimum ciphertext (teks tersandi) yang diperlukan oleh seorang kriptanalis yang memiliki daya komputasi tak terbatas (computationally unbounded) untuk secara unik dan pasti menentukan kunci enkripsi yang benar.
- Pertanyaan 3: Beberapa alasan utama ancaman brute force
    1. Kunci Lemah (Entropi Rendah) 
    Sebagian besar serangan brute force menargetkan kata sandi pengguna yang lemah.
    Kata sandi yang mudah ditebak memiliki entropi rendah (keacakan rendah), yang secara drastis mengurangi ruang kunci yang harus dicoba penyerang, membuatnya mudah ditembus dalam waktu singkat.
    
    2. Kekuatan Komputasi Tinggi 
    Penyerang menggunakan GPU (Graphics Processing Unit) dan ASIC (Application-Specific Integrated Circuit) yang dapat melakukan miliaran percobaan hashing per detik secara paralel.
    Penyewaan sumber daya komputasi cloud juga memungkinkan serangan besar-besaran dan cepat.
    
    3. Otomatisasi Serangan Cerdas 
    Serangan modern menggunakan Serangan Hybrid (menggabungkan kamus dengan brute force) dan Serangan Credential Stuffing (menggunakan daftar kredensial curian).
    Metode ini memanfaatkan data yang telah bocor dan pola kata sandi umum, mempercepat proses penemuan kunci yang benar tanpa perlu mencoba semua kombinasi secara acak. 

---

## 8. Kesimpulan
Kekuatan suatu sistem kriptografi modern bergantung pada interaksi tiga faktor utama: Entropi Kunci, Jarak Unicity, dan Ketahanan Implementasi terhadap serangan praktis seperti Brute Force.
1. Entropi sebagai Sumber Kekuatan UtamaEntropi adalah ukuran keacakan sejati suatu kunci, diukur dalam bit. Semakin tinggi entropinya ($N$ bit), semakin besar ruang kunci ($2^N$ upaya) yang harus dicoba penyerang.Kunci kuat harus memiliki entropi yang sama dengan panjang fisiknya (misalnya, kunci 256-bit harus memiliki 256 bit entropi efektif).
2. Jarak Unicity sebagai Batasan TeoretisJarak Unicity ($U$) adalah batas teoretis yang menentukan jumlah minimum ciphertext yang diperlukan penyerang untuk secara unik mengidentifikasi kunci enkripsi yang benar.$U$ bergantung pada entropi kunci dan redundansi bahasa plaintext. Idealnya, cipher harus memiliki $U$ yang sangat besar.
3.  Brute Force: Ancaman Praktis TerbesarMeskipun algoritma modern (seperti AES) sangat kuat secara teoretis, serangan Brute Force masih menjadi ancaman serius karena menargetkan implementasi yang lemah, bukan algoritma itu sendiri.Ancaman ini didorong oleh:Penggunaan kunci/kata sandi lemah (entropi rendah).Peningkatan kekuatan komputasi (GPU/ASIC) yang mempercepat laju percobaan.Penggunaan metode serangan cerdas (Hybrid dan Credential Stuffing).

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
