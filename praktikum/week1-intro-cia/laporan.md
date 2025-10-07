# Laporan Praktikum

# Sejarah Kriptografi
Sejarah Kriptografi: Dari Pesan Rahasia Kuno hingga Era Digital
Kriptografi (berasal dari bahasa Yunani kryptos = tersembunyi, dan graphein = tulisan) adalah ilmu dan seni menjaga keamanan pesan. Sejarahnya membentang ribuan tahun, berevolusi dari teknik pena-dan-kertas sederhana menjadi algoritma matematika yang kompleks.

**I. Kriptografi Klasik (Zaman Kuno hingga Abad Pertengahan)**
Era ini didominasi oleh dua jenis sandi utama: Substitusi (mengganti huruf) dan Transposisi (mengubah urutan huruf).

1. Abad Kuno (Yunani dan Romawi)
Scytale (Yunani Kuno, sekitar 400 SM): Contoh awal kriptografi Transposisi. Pesan ditulis pada pita yang melilit sebuah tongkat (scytale) dengan diameter tertentu. Pesan hanya dapat dibaca oleh penerima yang memiliki tongkat dengan diameter yang sama.

Caesar Cipher (Romawi Kuno): Dikenalkan oleh Julius Caesar, ini adalah bentuk sederhana dari sandi Substitusi. Setiap huruf pada teks asli diganti dengan huruf lain yang digeser sejumlah posisi tetap (misalnya 3) ke depan dalam urutan alfabet. Meskipun sederhana, teknik ini efektif untuk komunikasi militer pada masanya.

2. Periode Pencerahan Islam (Abad ke-9)
Penemuan Kriptanalisis: Ilmuwan Arab Abu Yusuf Yaqub Ibnu Ishaq Al-Kindi (Al-Kindi) merupakan tokoh kunci. Ia mengembangkan teknik Analisis Frekuensi, sebuah metode untuk memecahkan sandi substitusi dengan menganalisis frekuensi kemunculan setiap huruf dalam teks tersandi. Penemuan ini secara efektif mengakhiri efektivitas sandi monoalfabetik sederhana.

3. Abad Pertengahan hingga Renaisans
Vigenère Cipher (Abad ke-16): Sandi yang menggunakan kunci berulang dan dikenal sebagai sandi Polialfabetik (menggunakan banyak cipher Caesar yang berbeda). Sandi ini jauh lebih sulit dipecahkan dengan analisis frekuensi dan sempat dijuluki sebagai "sandi yang tidak dapat dipecahkan" selama ratusan tahun.

**II. Kriptografi Mekanik dan Perang Dunia (Awal Abad ke-20)**
Perkembangan teknologi mekanik melahirkan mesin-mesin enkripsi yang lebih rumit, meningkatkan keamanan secara eksponensial.

Mesin Rotor (Awal Abad ke-20): Mesin seperti Enigma (Jerman) dan Turing Bombe (Sekutu) menjadi inti dari komunikasi rahasia militer selama Perang Dunia II.

Enigma (Jerman): Mesin rotor yang dapat menghasilkan sandi yang sangat kompleks dan dianggap tidak dapat dipecahkan.

Pemecahan Enigma: Kriptografer Sekutu di Bletchley Park, Inggris, yang dipimpin oleh Alan Turing, berhasil memecahkan kode Enigma menggunakan logika, matematika, dan cikal bakal komputer modern. Upaya ini disebut-sebut mempercepat akhir Perang Dunia II dan menjadi tonggak penting dalam perkembangan ilmu komputer.

**III. Kriptografi Modern (Era Komputer dan Digital)**
Sejak paruh kedua abad ke-20, kriptografi bergeser dari teknik linguistik ke matematika murni, seiring dengan munculnya komputer digital.

1. Kriptografi Kunci Simetris Standar (1970-an)
DES (Data Encryption Standard, 1977): Dikembangkan oleh IBM dan diadopsi oleh Pemerintah AS. DES menjadi standar enkripsi simetris yang dominan. Kriptografi Simetris menggunakan kunci yang sama untuk enkripsi dan dekripsi.

AES (Advanced Encryption Standard, 2001): Standar enkripsi simetris pengganti DES yang lebih kuat dan digunakan secara luas hingga saat ini (misalnya, untuk mengamankan Wi-Fi atau hard drive).

2. Kriptografi Kunci Publik / Asimetris (1976)
Ini adalah revolusi terbesar dalam sejarah kriptografi sejak Al-Kindi.

Konsep Kunci Publik: Diperkenalkan oleh Whitfield Diffie dan Martin Hellman pada tahun 1976. Konsep ini menggunakan dua kunci yang berbeda: Kunci Publik (untuk enkripsi, dapat disebar ke publik) dan Kunci Privat (untuk dekripsi, harus dirahasiakan). Ini memecahkan masalah distribusi kunci yang merupakan kelemahan utama kriptografi simetris.

Algoritma RSA (Rivest, Shamir, dan Adleman, 1977): Algoritma kunci publik pertama yang dapat digunakan secara praktis dan masih menjadi dasar untuk keamanan internet saat ini (termasuk SSL/TLS).

3. Masa Depan: Kriptografi Kuantum
Saat ini, penelitian berfokus pada Kriptografi Pasca-Kuantum. Hal ini didorong oleh ancaman teoretis bahwa komputer kuantum di masa depan dapat memecahkan algoritma kunci publik yang ada (seperti RSA) dalam hitungan detik. Tujuannya adalah mengembangkan algoritma baru yang aman dari serangan komputer kuantum dan klasik.

---

**Konsep Dasar *Confidentiality, Integrity, Availability (CIA)***
CIA Triad (Tiga Serangkai CIA) adalah model keamanan informasi fundamental yang memandu kebijakan keamanan suatu organisasi. Model ini terdiri dari tiga komponen inti yang sering dianggap sebagai tujuan paling penting dari keamanan informasi.

1. **Confidentiality *(Kerahasiaan)***
Kerahasiaan adalah upaya untuk mencegah pengungkapan informasi kepada pihak yang tidak berwenang. Ini memastikan bahwa data hanya dapat diakses oleh individu, entitas, atau proses yang telah diberi izin.

Tujuan Utama: Melindungi data sensitif dari mata-mata atau pengguna yang tidak berwenang.

Contoh Penerapan: Menggunakan enkripsi untuk mengacak data; menerapkan kontrol akses (misalnya, username dan password); menggunakan otentikasi dua faktor (2FA).

Ancaman terhadap Kerahasiaan: Sniffing jaringan, data leakage, atau akses tidak sah.

2. **Integrity *(Integritas)***
Integritas merujuk pada keakuratan dan kelengkapan data. Ini memastikan bahwa data tidak diubah, dihapus, atau dimanipulasi secara tidak sah selama penyimpanan, pemrosesan, atau transmisi.

Tujuan Utama: Memastikan data dapat dipercaya dan tidak dirusak.

Contoh Penerapan: Menggunakan fungsi hashing untuk membuat sidik jari data (data fingerprint); tanda tangan digital untuk memverifikasi keaslian dokumen; kontrol versi (version control).

Ancaman terhadap Integritas: Virus dan malware, kesalahan saat transmisi, atau perubahan data yang disengaja oleh hacker.

3. **Availability *(Ketersediaan)***
Ketersediaan adalah jaminan bahwa sistem dan data dapat diakses dan digunakan oleh pengguna yang sah ketika mereka membutuhkannya. Hal ini berkaitan dengan fungsionalitas sistem dan kemampuan pengguna untuk mengakses sumber daya.

Tujuan Utama: Memastikan akses yang andal dan tepat waktu terhadap sistem.

Contoh Penerapan: Redundancy (memiliki sistem cadangan); Disaster Recovery Plan (DRP); backup data secara teratur; dan pemeliharaan perangkat keras yang baik.

Ancaman terhadap Ketersediaan: Serangan Distributed Denial of Service (DDoS), pemadaman listrik, kegagalan hardware atau software, dan bencana alam.

Ketiga elemen ini saling terkait. Keamanan yang kuat harus menyeimbangkan ketiganya; mengabaikan salah satunya akan melemahkan dua elemen lainnya.

**Peran Kriptografi dalam Kehidupan Sehari-hari**
Kriptografi adalah praktik dan studi tentang teknik komunikasi yang aman di hadapan pihak ketiga (disebut sebagai adversaries). Kriptografi adalah tulang punggung keamanan digital modern dan merupakan mekanisme utama untuk mencapai Confidentiality dan Integrity (serta otentikasi dan non-repudiasi).

Berikut adalah peran kunci kriptografi dalam aktivitas sehari-hari:

1. **Enkripsi Pesan *(Messaging Encryption)***
Contoh: Enkripsi End-to-End (E2EE) pada WhatsApp, Telegram, atau iMessage.

Mekanisme: Kriptografi memastikan Kerahasiaan. Pesan dienkripsi pada perangkat pengirim dan hanya dapat didekripsi pada perangkat penerima. Bahkan penyedia layanan atau hacker yang mencegat pesan tidak dapat membacanya. Ini biasanya menggunakan kombinasi kriptografi simetris dan asimetris.

2. **Keamanan Transaksi dan Browsing Web *(SSL/TLS)**
Contoh: Simbol gembok 🔒 di browser Anda saat mengunjungi situs web perbankan atau e-commerce.

Mekanisme: Secure Sockets Layer (SSL) dan penerusnya, Transport Layer Security (TLS), menggunakan kriptografi asimetris untuk membangun koneksi yang aman antara browser Anda dan server web.

Ini memastikan Kerahasiaan data (informasi login, nomor kartu kredit) yang dikirim melintasi internet.

Ini juga menjamin Integritas data, memastikan bahwa data tidak diubah selama transmisi.

Sertifikat SSL/TLS juga berfungsi sebagai otentikasi (verifikasi identitas server).

3. **Tanda Tangan Digital *(Digital Signature)***
Contoh: Mengesahkan keaslian software yang diunduh, otorisasi dokumen hukum digital, atau transaksi blockchain.

Mekanisme: Tanda tangan digital menggunakan kriptografi kunci asimetris untuk memverifikasi Integritas dokumen dan otentikasi (identitas pengirim).

Pengirim menggunakan kunci privatnya untuk "menandatangani" hash data.

Penerima menggunakan kunci publik pengirim untuk memverifikasi bahwa hash yang ditandatangani cocok dengan hash dokumen yang diterima, membuktikan bahwa dokumen tersebut tidak diubah dan benar-benar berasal dari pengirim tersebut (Non-Repudiasi).

4. ***Cryptocurrency dan Blockchain***
Contoh: Bitcoin, Ethereum, dan mata uang digital lainnya.

Mekanisme: Blockchain sangat bergantung pada fungsi hashing kriptografi dan tanda tangan digital.

Hashing memastikan Integritas (setiap blok ditautkan secara kriptografis ke blok sebelumnya, mencegah perubahan data).

Tanda tangan digital digunakan untuk otorisasi transaksi.

---

# QUIS
**1. Tokoh yang paling sering disebut sebagai Bapak Kriptografi Modern adalah Claude Shannon.**

Mengapa Claude Shannon?
Claude Shannon, seorang ahli matematika, insinyur listrik, dan kriptografer Amerika, dianggap sebagai pelopor utama karena:

Teori Komunikasi: Ia meletakkan dasar teoritis yang kuat untuk kriptografi dalam makalahnya yang revolusioner tahun 1948, "A Mathematical Theory of Communication" (Teori Matematis Komunikasi). Meskipun makalah ini lebih luas tentang teori informasi, konsep-konsep di dalamnya sangat mendasar bagi keamanan dan perancangan sistem kriptografi.

Analisis Kriptografi: Sebelumnya, ia menerbitkan makalah yang tidak dirahasiakan, "Communication Theory of Secrecy Systems" (Teori Komunikasi Sistem Kerahasiaan) pada tahun 1949, yang secara formal memperkenalkan dan mendefinisikan konsep penting seperti diffusion (penyebaran) dan confusion (kebingungan)—dua properti kunci yang harus dimiliki oleh cipher yang aman untuk menahan serangan analisis frekuensi dan metode lainnya.

Kontribusi Shannon mengubah kriptografi dari seni yang didasarkan pada trik dan aturan menjadi ilmu pengetahuan yang didasarkan pada prinsip-prinsip matematika yang ketat.

**2. Algoritma kunci publik (asimetris) yang populer dan paling banyak digunakan saat ini adalah RSA dan Elliptic Curve Cryptography (ECC), serta algoritma Diffie-Hellman (DH) untuk pertukaran kunci.**

  1. RSA (Rivest–Shamir–Adleman)
RSA adalah algoritma kunci publik yang paling terkenal dan paling banyak diaplikasikan.

Prinsip Keamanan: Keamanannya didasarkan pada kesulitan komputasi dalam memfaktorkan bilangan bulat yang sangat besar menjadi faktor-faktor bilangan primanya.

Aplikasi: Digunakan secara luas untuk enkripsi/dekripsi, Tanda Tangan Digital, dan dalam protokol keamanan web seperti SSL/TLS.

  2. ECC (Elliptic Curve Cryptography)
ECC merupakan pesaing utama RSA dan semakin populer digunakan, terutama pada perangkat bergerak.

Prinsip Keamanan: Didukung oleh kesulitan komputasi dalam memecahkan masalah Logaritma Diskrit Kurva Eliptik (Elliptic Curve Discrete Logarithm Problem/ECDLP).

Keunggulan: ECC menawarkan tingkat keamanan yang setara dengan RSA, tetapi dengan ukuran kunci yang jauh lebih kecil. Misalnya, kunci ECC 256-bit setara dengan kunci RSA 3072-bit, sehingga lebih efisien untuk perangkat dengan daya komputasi dan memori terbatas.

Varian Populer:

ECDSA (Elliptic Curve Digital Signature Algorithm): Digunakan untuk Tanda Tangan Digital.

ECDH (Elliptic Curve Diffie-Hellman): Digunakan untuk pertukaran kunci.

  3. Diffie-Hellman (DH)
Diffie-Hellman adalah algoritma kunci publik pertama yang ditemukan dan sering digunakan untuk satu tujuan utama.

Fungsi Utama: Digunakan secara eksklusif untuk Pertukaran Kunci (Key Exchange). Tujuannya adalah untuk memungkinkan dua pihak yang tidak memiliki informasi rahasia sebelumnya untuk menyepakati (menghasilkan) sebuah kunci simetris bersama secara aman melalui saluran komunikasi yang tidak aman.

Penerapan: Versi modifikasi dan lebih aman, seperti Ephemeral Diffie-Hellman (DHE), sering digunakan dalam protokol web untuk memberikan kerahasiaan ke depan yang sempurna (Perfect Forward Secrecy).

**3. perbedaan utama antara kriptografi klasik dan kriptografi modern dalam format urutan, bukan tabel.**

Kriptografi modern adalah evolusi yang didorong oleh ilmu matematika kompleks dan munculnya komputer digital, jauh lebih aman dan serbaguna dibanding pendahulunya.

  1. Unit Operasi Data
Kriptografi Klasik: Beroperasi pada level karakter (huruf, angka, simbol) sebagai unit dasar. Contohnya, mengganti atau memindahkan huruf per huruf dalam pesan.

Kriptografi Modern: Beroperasi pada level bit biner (rangkaian 0 dan 1). Seluruh data (pesan, kunci, ciphertext) diolah sebagai blok atau aliran bit.

  2. Landasan dan Kekuatan Keamanan
Kriptografi Klasik: Keamanannya didasarkan pada kerahasiaan algoritma (security by obscurity) atau teknik yang relatif sederhana (substitusi dan transposisi). Sistem ini rentan dan mudah dipecahkan menggunakan analisis frekuensi atau serangan brute force sederhana.

Kriptografi Modern: Keamanannya didasarkan pada prinsip matematika yang kompleks dan kerahasiaan kunci (sesuai Prinsip Kerckhoffs). Keamanannya terletak pada kesulitan komputasi untuk memecahkan masalah matematika yang mendasarinya (misalnya, faktorisasi bilangan prima besar atau logaritma diskrit).

  3. Jenis Kunci dan Model Komunikasi
Kriptografi Klasik: Hampir seluruhnya menggunakan model Kunci Simetris (kunci tunggal). Kunci yang sama digunakan untuk enkripsi dan dekripsi, sehingga kunci tersebut harus dibagikan secara rahasia sebelum komunikasi.

Kriptografi Modern: Menggunakan dua model kunci utama:

Kunci Simetris (Modern): Lebih efisien dan kuat daripada versi klasik (contoh: AES).

Kunci Asimetris (Kunci Publik): Memperkenalkan pasangan kunci (publik dan privat) yang berbeda. Model ini merevolusi pertukaran kunci yang aman, autentikasi, dan Tanda Tangan Digital (RSA, ECC).

  4. Tujuan dan Aplikasi
Kriptografi Klasik: Fokus utamanya adalah pada Kerahasiaan (menyembunyikan pesan agar tidak dibaca oleh musuh) dan terbatas penggunaannya, kebanyakan di bidang militer atau diplomatik.

Kriptografi Modern: Mencakup empat tujuan keamanan utama: Kerahasiaan, Integritas (memastikan data tidak diubah), Autentikasi (memverifikasi identitas), dan Non-Repudiasi (tidak dapat menyangkal tindakan). Aplikasinya merambah ke seluruh aspek digital, seperti perbankan online, SSL/TLS, dan mata uang kripto.
