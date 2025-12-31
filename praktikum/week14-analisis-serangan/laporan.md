# Laporan Praktikum Kriptografi
Minggu ke-: XIV  
Topik: Analisis Serangan 
Nama: Setyo Adi Nugroho  
NIM: 230202785  
Kelas: 5 IKKA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Mengidentifikasi jenis serangan pada sistem informasi nyata.
Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

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
  
- Pertanyaan 1: Banyak sistem lama (legacy systems) masih rentan terhadap serangan brute force atau dictionary attack karena dibangun pada era di mana standar keamanan dan kekuatan komputasi sangat jauh berbeda dengan kondisi saat ini. Sebab itu kerentanan ini terjadi karena adanya kesenjangan antara desain sistem masa lalu dengan kekuatan komputasi modern (seperti penggunaan GPU untuk memecahkan sandi).
- Pertanyaan 2: Perbedaan kelemahan algoritma dan implementasi adalah :
1. Kelemahan Algoritma (Theoretical/Mathematical Flaw)
Kelemahan ini bersifat mendasar. Artinya, tidak peduli seberapa rapi Anda menulis kodenya, algoritma tersebut memang sudah tidak aman karena logika matematikanya telah dipatahkan.
Penyebab: Kemajuan ilmu matematika atau peningkatan kekuatan komputasi yang membuat algoritma tersebut bisa ditebak atau dicari polanya.
Karakteristik: Sekali sebuah algoritma dinyatakan "broken", semua sistem yang menggunakannya dianggap tidak aman.
2. Kelemahan Implementasi (Practical/Human Error)
Di sini, algoritmanya mungkin sangat kuat (seperti AES-256), namun cara pengembang memasangnya ke dalam sistem ceroboh atau salah.
Penyebab: Kelalaian manusia, kurangnya pemahaman tentang protokol keamanan, atau keterbatasan infrastruktur.
Karakteristik: Algoritmanya sendiri masih dianggap standar industri, namun pintu masuknya terbuka karena kesalahan teknis.
- Pertanyaan 3: Beberapa strategi berkelanjutan untuk memastikan keamanan kriptografi tetap relevan:
1. Mengadopsi "Crypto-Agility"
Agilitas Kriptografi adalah kemampuan sistem untuk beralih dari satu algoritma kriptografi ke algoritma lain tanpa harus membongkar seluruh infrastruktur aplikasi.
Abstraksi Kode: Jangan menulis fungsi kriptografi secara keras (hardcoded) di dalam aplikasi. Gunakan penyedia layanan atau library pihak ketiga yang dapat diperbarui secara terpusat.
Pemisahan Kunci dan Logika: Pastikan mekanisme manajemen kunci (seperti HSM - Hardware Security Module) terpisah dari logika bisnis, sehingga saat algoritma perlu diganti, Anda hanya perlu memperbarui modul tersebut.
2. Migrasi ke Post-Quantum Cryptography (PQC)
Komputer kuantum di masa depan diprediksi mampu memecahkan algoritma asimetris populer seperti RSA dan ECC. Organisasi harus mulai merencanakan transisi ke algoritma yang tahan terhadap serangan kuantum.
Standarisasi NIST: Pantau dan mulailah menguji algoritma yang telah distandarisasi oleh NIST (seperti Kyber untuk enkripsi dan Dilithium untuk tanda tangan digital).
Hybrid Approach: Gunakan metode hibrida di mana data dienkripsi dengan algoritma klasik (AES/RSA) sekaligus algoritma PQC. Jika salah satu jebol, lapisan lainnya tetap melindungi data.
3. Manajemen Kunci yang Ketat (Lifecycle Management)
Algoritma sekuat apa pun akan gagal jika kuncinya dicuri atau disalahgunakan.
Rotasi Kunci Otomatis: Terapkan kebijakan rotasi kunci secara berkala untuk membatasi jumlah data yang terekspos jika sebuah kunci terkompromi.
Principle of Least Privilege: Hanya berikan akses ke kunci kriptografi pada layanan atau pengguna yang benar-benar membutuhkannya.
Audit dan Monitoring: Pantau setiap akses ke kunci enkripsi secara real-time untuk mendeteksi perilaku anomali.
4. Zero Trust Architecture
Jangan berasumsi bahwa enkripsi di tingkat penyimpanan (At-Rest) sudah cukup. Gunakan pendekatan keamanan berlapis:
Encryption in Transit: Pastikan semua data yang berpindah menggunakan protokol terbaru (seperti TLS 1.3).
Encryption in Use: Pertimbangkan teknologi seperti Confidential Computing atau Homomorphic Encryption yang memungkinkan data diolah tanpa harus didekripsi terlebih dahulu.
5. Audit dan Pengujian Berkala
Keamanan kriptografi bukan proyek "sekali jadi", melainkan proses terus-menerus.
Vulnerability Assessment: Lakukan pemindaian secara rutin untuk mendeteksi penggunaan algoritma usang (misalnya, mencari sisa-sisa penggunaan SHA-1 atau MD5 dalam sistem).
Compliance Check: Pastikan implementasi kriptografi mematuhi standar internasional seperti FIPS 140-3 atau regulasi lokal yang berlaku.
Poin Penting: Ancaman terbesar di masa depan bukan hanya "pembobolan paksa", tetapi serangan "Harvest Now, Decrypt Later"—di mana penyerang mencuri data terenkripsi sekarang dan menyimpannya untuk didekripsi setelah mereka memiliki komputer kuantum yang cukup kuat.
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
