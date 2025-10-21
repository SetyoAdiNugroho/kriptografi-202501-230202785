# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Modular-Math  
Nama: Setyo Adi Nugroho 
NIM: 230202785  
Kelas: 5IKKA 

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Modular Math adalah sistem aritmetika untuk bilangan bulat di mana bilangan "berputar" atau berulang setelah mencapai nilai tertentu yang disebut modulus. Cara kerjanya mirip dengan jam, di mana setelah pukul 12, waktu kembali ke pukul 1. Konsep ini berfokus pada sisa pembagian dan memiliki aplikasi luas dalam bidang seperti kriptografi dan ilmu komputer. 

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
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Aritmetika modular (Modular Math) adalah fondasi matematis yang krusial dalam kriptografi modern. Perannya sangat penting untuk memastikan keamanan, kerahasiaan, dan integritas data.
  beberapa peran utama aritmetika modular dalam kriptografi modern:
  1. Mendukung algoritma kunci publik
  2. Memfasilitasi fungsi hash
  3. Menciptakan kurva eliptik
  4. Memungkinkan kriptografi kunci simetris
  5. Mengatur operasi dalam cakupan yang terbatas
  6. Menjadi dasar untuk tanda tangan digital
- Pertanyaan 2: Invers modular sangat penting dalam algoritma kunci publik seperti RSA karena menjadi jembatan matematis yang memungkinkan proses dekripsi. Tanpa invers modular, enkripsi akan bersifat satu arah dan pesan yang sudah dienkripsi tidak akan bisa dikembalikan ke bentuk aslinya.
- Pertanyaan 3: Tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar adalah :
  1. Kompleksitas komputasi eksponensial
     Waktu pemrosesan: Algoritma yang paling efektif untuk memecahkan logaritma diskrit berjalan dalam waktu eksponensial terhadap panjang modulus dalam bit.
     Ukuran modulus: Dalam kriptografi, ukuran modulus dipilih sedemikian rupa sehingga masalah logaritma diskrit menjadi tidak dapat dipecahkan dalam rentang waktu yang wajar.
  2. Kurangnya algoritma efisien
     Algoritma yang ada: Beberapa algoritma yang dikenal untuk memecahkan masalah logaritma diskrit adalah algoritma "Baby-step, giant-step" dan algoritma "Pollard's Rho". Meskipun lebih cepat daripada metode pencarian brute-force, algoritma ini tetap intensif secara komputasi dan tidak dapat digunakan untuk modulus besar.
     Saringan medan bilangan (Number Field Sieve/NFS): NFS adalah algoritma paling efisien yang ada saat ini untuk menyelesaikan logaritma diskrit dalam bidang hingga (\(Z_{p}^{*}\)). Namun, NFS juga sangat intensif secara komputasi dan memerlukan sumber daya yang besar untuk modulus besar.
  3. Tidak adanya pola yang jelas
     Perilaku logaritma: Tidak seperti logaritma dalam matematika biasa yang berperilaku terus-menerus dan teratur, logaritma diskrit berperilaku tidak menentu dan tidak dapat diprediksi. Karena tidak ada pola yang jelas, tidak ada metode pintas yang dapat digunakan untuk menyelesaikannya secara efisien.
     Fungsi satu arah: Fenomena ini menjadikannya "fungsi satu arah", yang mudah untuk dihitung ke satu arah (eksponensiasi modular), tetapi hampir tidak mungkin untuk dibalik ke arah lain (logaritma diskrit) tanpa kunci yang tepat.
  4. Kerentanan terhadap komputasi kuantum
     Komputer kuantum: Meskipun algoritma klasik tidak dapat menyelesaikan masalah logaritma diskrit dalam waktu polinomial, komputer kuantum berpotensi mengubah lanskap keamanan. Algoritma Shor, misalnya, dapat menyelesaikan masalah ini secara efisien pada komputer kuantum.
     Ancaman masa depan: Kemunculan komputer kuantum yang kuat menjadi ancaman besar bagi kriptografi berbasis logaritma diskrit. Hal ini mendorong penelitian kriptografi pasca-kuantum untuk menemukan metode enkripsi baru yang tahan terhadap serangan kuantum.
  5. Keterbatasan kelompok yang dipilih dengan buruk
     Pemilihan grup yang hati-hati: Keamanan sistem kriptografi yang menggunakan logaritma diskrit bergantung pada pemilihan grup yang cermat.
     Pengecualian khusus: Beberapa grup memiliki struktur matematika yang memungkinkan logaritma diskrit dihitung dengan mudah. Dalam kasus seperti ini, masalahnya tidak lagi sulit, dan kriptografi yang dibangun di atasnya akan rentan. 
    
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

```
