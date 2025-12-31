# Laporan Praktikum Kriptografi
Minggu ke-: XV  
Topik: Tiny Coin erc20  
Nama: Setyo Adi Nugroho  
NIM: 230202785  
Kelas: 5 IKKA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Mengembangkan proyek sederhana berbasis algoritma kriptografi.
Mendokumentasikan proses implementasi proyek ke dalam repository Git.
Menyusun laporan teknis hasil proyek akhir.

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
 
- Pertanyaan 1: Fungsi-fungsi utama ERC20 dalam ekosistem blockchain:
1. Standardisasi dan Interoperabilitas
Sebelum ada ERC20, setiap pengembang membuat token dengan aturan mereka sendiri. Hal ini menyulitkan bursa (exchange) atau dompet digital (wallet) karena mereka harus menulis kode baru setiap kali ingin mendukung token baru.
Fungsinya: Dengan standar ini, dompet digital dan bursa kripto dapat dengan mudah mengintegrasikan token baru secara otomatis karena mereka semua "berbicara dalam bahasa yang sama."
2. Memfasilitasi Pembuatan Token (Smart Contracts)
ERC20 menyediakan kerangka kerja yang sudah jadi. Pengembang tidak perlu membangun blockchain dari nol jika ingin meluncurkan aset digital.
Fungsinya: Memungkinkan siapa saja untuk membuat token di atas jaringan Ethereum dengan mendefinisikan aturan dasar seperti total pasokan, cara transfer, dan cara memantau saldo.
3. Tulang Punggung DeFi (Decentralized Finance)
Sebagian besar ekosistem keuangan terdesentralisasi (DeFi) bergantung pada ERC20.
Fungsinya: Token ERC20 digunakan untuk staking, memberikan pinjaman (lending), atau menjadi penyedia likuiditas di bursa desentralisasi seperti Uniswap. Tanpa standar ini, protokol DeFi tidak akan bisa saling terhubung secara modular.
4. Alat Penggalangan Dana (ICO)
ERC20 menjadi sangat populer karena memicu ledakan Initial Coin Offering (ICO) pada tahun 2017.
Fungsinya: Memudahkan proyek baru untuk mengumpulkan modal dengan menjual token ERC20 kepada investor sebagai imbalan atas pendanaan proyek mereka. 
- Pertanyaan 2: Terdapat dua cara utama bagaimana transfer terjadi, tergantung pada siapa yang memulai transaksi:
1. Transfer Langsung (transfer)
Mekanisme ini digunakan ketika Anda mengirim token langsung dari dompet Anda ke alamat lain.
Proses: Anda memanggil fungsi transfer(recipient, amount).
Cara Kerja di Balik Layar:
Kontrak memeriksa apakah saldo Anda (msg.sender) cukup.
Jika cukup, kontrak mengurangi saldo Anda.
Kontrak menambah jumlah yang sama ke saldo penerima.
Kontrak memicu (emit) event Transfer agar riwayatnya tercatat secara publik.
2. Mekanisme Delegasi (approve + transferFrom)
Ini adalah mekanisme paling penting untuk ekosistem dApps dan DeFi (seperti Uniswap). Mekanisme ini memungkinkan kontrak pintar lain memindahkan token Anda atas izin Anda.
Langkah-langkahnya:
Approve (Izin): Anda memanggil fungsi approve(spender, amount). Anda memberikan izin kepada alamat tertentu (misalnya kontrak DEX) untuk mengambil token Anda hingga batas tertentu.
Allowance (Jatah): Kontrak menyimpan catatan bahwa "Alamat A mengizinkan Kontrak B untuk mengambil maksimal X token."
TransferFrom (Eksekusi): Saat Anda melakukan swap atau staking, Kontrak B akan memanggil transferFrom(owner, recipient, amount).
Kontrak akan memeriksa apakah jumlahnya tidak melebihi jatah (allowance) yang Anda berikan.
Jika oke, saldo Anda dikurangi, saldo penerima ditambah, dan jatah (allowance) dikurangi secara otomatis. 
- Pertanyaan 3: Risiko utama serta langkah mitigasi yang umum dilakukan oleh pengembang:
1. Reentrancy Attack
Ini adalah salah satu celah keamanan paling terkenal (penyebab peretasan The DAO). Risiko ini terjadi ketika kontrak memanggil fungsi ke kontrak eksternal sebelum ia sempat memperbarui saldonya sendiri.
Risiko: Penyerang bisa menarik dana berulang kali dalam satu transaksi sebelum kontrak sempat mencatat bahwa saldo penyerang sudah kosong.
Mitigasi: * Gunakan pola Checks-Effects-Interactions: Selalu perbarui saldo internal sebelum mengirim dana keluar.
Gunakan Reentrancy Guard (seperti modifier nonReentrant dari OpenZeppelin).
2. Overflow dan Underflow
Terjadi ketika hasil operasi matematika melebihi kapasitas penyimpanan variabel (misalnya, angka yang terlalu besar kembali ke nol).
Risiko: Seorang pengguna bisa memanipulasi saldo mereka menjadi sangat besar secara tidak sah.
Mitigasi: * Gunakan bahasa Solidity versi 0.8.0 ke atas yang sudah memiliki pemeriksaan otomatis untuk overflow/underflow.
Gunakan pustaka SafeMath jika menggunakan versi Solidity yang lebih lama.
3. Kelemahan Logika dan Akses Kontrol
Risiko ini muncul jika fungsi sensitif (seperti penarikan dana) tidak dilindungi dengan benar.
Risiko: Pihak yang tidak berwenang bisa memanggil fungsi withdraw() atau mengubah parameter penting kontrak.
Mitigasi: * Implementasikan modul Ownable atau AccessControl (Role-Based Access Control).
Gunakan modifier seperti onlyOwner untuk fungsi-fungsi kritis.
4. Front-running
Karena transaksi di blockchain masuk ke mempool (antrean publik) sebelum dikonfirmasi, orang lain dapat melihat transaksi Anda sebelum diproses.
Risiko: Penyerang bisa membayar biaya gas yang lebih tinggi untuk "menyalip" transaksi Anda dan mengambil keuntungan (misalnya dalam perdagangan di DEX).
Mitigasi: * Gunakan batas toleransi harga (slippage tolerance).
Gunakan skema Commit-Reveal atau solusi off-chain seperti Flashbots.
Strategi Mitigasi Secara Umum (Best Practices)
Untuk meminimalkan risiko di atas, pengembang profesional biasanya mengikuti alur kerja berikut:
Audit Pihak Ketiga: Selalu gunakan jasa auditor keamanan independen (seperti CertiK, OpenZeppelin, atau Trail of Bits) sebelum peluncuran besar.
Bug Bounty: Membuka program bagi pengembang luar untuk menemukan celah dengan imbalan hadiah uang.
Formal Verification: Menggunakan pembuktian matematis untuk memastikan kode berperilaku sesuai spesifikasi.
Timelock & Multisig: Jangan biarkan satu orang memiliki kontrol penuh. Gunakan dompet Multi-signature (misalnya Gnosis Safe) dan Timelock agar ada jeda waktu sebelum perubahan besar diterapkan.

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
