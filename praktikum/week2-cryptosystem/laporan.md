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

**Pesan Terenkripsi *(Ciphertext / Teks Sandi)***
Ini adalah hasil dari proses enkripsi, yaitu pesan asli yang telah diubah menjadi bentuk yang tidak dapat dibaca atau dimengerti tanpa kunci yang benar. Ini adalah data yang ditransmisikan melalui saluran yang tidak aman.
Contoh: "Xm92nFh8Aop2Bq3Rz7yG" (tergantung pada algoritma yang digunakan).

**Prosedur Enkripsi dan Dekripsi**
Ini adalah dua proses fungsional yang menggunakan algoritma dan kunci:
Enkripsi: Proses mengubah plaintext menjadi ciphertext.
Dekripsi: Proses mengubah ciphertext kembali menjadi plaintext (hanya dapat dilakukan oleh penerima yang sah dengan kunci yang benar).

---

## 2. Beberapa kelebihan dan kelemahan sistem simetris dibandingkan asimetris

**Enkripsi Kunci Simetris**
Enkripsi kunci simetris, juga dikenal sebagai enkripsi rahasia bersama, adalah metode yang menggunakan kunci yang sama untuk enkripsi dan dekripsi. Metode ini sederhana, cepat, dan efisien, sehingga cocok untuk enkripsi data massal. Contoh algoritma enkripsi kunci simetris adalah AES, DES, dan Blowfish.

Kelebihan:
Cepat: Enkripsi kunci simetris lebih cepat daripada enkripsi asimetris karena menggunakan kunci yang sama untuk enkripsi dan dekripsi.
Efisien: Enkripsi kunci simetris efisien dalam hal komputasi dan penyimpanan, membuatnya cocok untuk mengenkripsi data dalam jumlah besar.
Kontra:
Manajemen kunci: Kelemahan terbesar enkripsi kunci simetris adalah pengirim dan penerima harus memiliki akses ke kunci yang sama, sehingga manajemen kunci menjadi tantangan. Jika kunci hilang atau dibobol, semua data terenkripsi berisiko.
Distribusi kunci: Mendistribusikan kunci kepada semua pihak yang membutuhkannya dapat menjadi tantangan, terutama dalam organisasi besar.

**Enkripsi Kunci Asimetris**
Enkripsi kunci asimetris, juga dikenal sebagai kriptografi kunci publik, menggunakan dua kunci berbeda untuk enkripsi dan dekripsi. Kunci publik digunakan untuk enkripsi, sedangkan kunci privat digunakan untuk dekripsi. Contoh algoritma enkripsi kunci asimetris adalah RSA, Kriptografi Kurva Eliptik (ECC), dan DSA.

Kelebihan:
Manajemen kunci: Enkripsi kunci asimetris lebih aman daripada enkripsi kunci simetris karena setiap pengguna memiliki sepasang kunci, yaitu kunci publik dan kunci privat. Kunci publik dapat dibagikan secara bebas, sementara kunci privat dirahasiakan.
Distribusi kunci: Kunci publik dapat didistribusikan dengan mudah, membuatnya lebih mudah untuk mengenkripsi dan mendekripsi pesan.
Kontra:
Lambat: Enkripsi kunci asimetris lebih lambat daripada enkripsi kunci simetris karena melibatkan operasi komputasi intensif.
Tidak efisien: Enkripsi kunci asimetris kurang efisien daripada enkripsi kunci simetris, membuatnya tidak cocok untuk mengenkripsi data dalam jumlah besar.

---

## 3. Penyebab distribusi kunci menjadi masalah utama dalam kriptografi simetris
Distribusi kunci menjadi masalah utama dalam kriptografi simetris karena memerlukan cara yang aman untuk membagikan kunci rahasia yang sama kepada pengirim dan penerima sebelum komunikasi dimulai. Jika kunci tersebut dicegat oleh pihak ketiga selama proses distribusi, seluruh komunikasi yang dienkripsi akan disusupi. 

Berikut adalah beberapa alasan utama mengapa distribusi kunci menjadi masalah dalam kriptografi simetris:

**Keamanan kunci saat transit**
Kunci rahasia harus didistribusikan melalui saluran yang aman dan terpisah dari data yang dienkripsi. 
- Jika kunci dikirim melalui saluran yang tidak aman, seperti jaringan internet biasa, pihak jahat dapat mencegatnya dan mendekripsi semua pesan.
- Masalah ini menghadirkan dilema mendasar: untuk membangun komunikasi yang aman, Anda sudah membutuhkan saluran yang aman, padahal tujuan kriptografi itu sendiri adalah menciptakan saluran yang aman. 

**Masalah skalabilitas**
Dalam jaringan besar, mengelola kunci unik untuk setiap pasangan pengguna yang ingin berkomunikasi menjadi tidak praktis dan rumit. 
Contoh: 
- Jika ada 100 orang yang perlu berkomunikasi secara aman, mereka membutuhkan \(100(100-1)/2=4.950\) kunci unik yang berbeda. Jumlah ini meningkat drastis seiring bertambahnya jumlah pengguna.
- Sistem manajemen kunci yang kompleks akan diperlukan untuk mengelola ribuan kunci tersebut, yang menimbulkan tantangan logistik yang besar. 

**Kurangnya otentikasi** 
Kriptografi simetris tidak memiliki mekanisme bawaan untuk memverifikasi identitas pengirim pesan. 
- Jika seorang penyerang berhasil mendapatkan kunci, mereka dapat memodifikasi dan mengenkripsi ulang pesan, lalu mengirimkannya seolah-olah berasal dari pengirim asli. Penerima tidak akan memiliki cara untuk mengetahui bahwa pesan tersebut telah diubah. 

**Risiko man-in-the-middle** 
Serangan ini terjadi ketika pihak ketiga menempatkan dirinya di antara dua pihak yang berkomunikasi untuk mencegat kunci. 
- Misalnya, Alice ingin berkomunikasi dengan Bob. Penyerang, Eve, mencegat kunci yang dikirim Alice. Eve kemudian mengirimkan kuncinya sendiri kepada Bob, menyamar sebagai Alice. Eve kini dapat mencegat, mendekripsi, dan memodifikasi semua komunikasi di antara mereka. 

**Solusi untuk masalah distribusi kunci** 
Masalah ini sebagian besar diselesaikan dengan menggunakan kriptografi kunci asimetris (kunci publik) untuk distribusi kunci. 
- Pertukaran kunci Diffie-Hellman: Metode ini memungkinkan dua pihak untuk membuat kunci rahasia bersama melalui saluran yang tidak aman tanpa perlu benar-benar mengirimkan kunci tersebut.
- Kriptografi hibrida: Dalam skema modern, kriptografi asimetris digunakan untuk menukar kunci simetris secara aman, yang kemudian digunakan untuk mengenkripsi data dalam jumlah besar. Ini menggabungkan kecepatan enkripsi simetris dengan keamanan distribusi kunci asimetris. 
