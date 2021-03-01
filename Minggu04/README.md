# workshop-python
<h2>Minggu 04</h2>
<b>Nama : Yusuf Nur Rahman Wahid</b></br>
<b>NIM : 185410039</b>

# Modul Pada Python
Jika Anda berhenti dari interpreter Python dan memasukkannya lagi, definisi yang Anda buat (fungsi dan variabel) akan hilang. Karena itu, jika Anda ingin menulis program yang agak lebih panjang, Anda lebih baik menggunakan editor teks untuk menyiapkan input bagi penerjemah dan menjalankannya dengan file itu sebagai input. Ini dikenal sebagai membuat script. Saat program Anda menjadi lebih panjang, Anda mungkin ingin membaginya menjadi beberapa file untuk pengelolaan yang lebih mudah. Anda mungkin juga ingin menggunakan fungsi praktis yang Anda tulis di beberapa program tanpa menyalin definisi ke setiap program.

Modul adalah file yang berisi definisi dan pernyataan Python. Nama berkas adalah nama modul dengan akhiran .py diakhirnya. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai variabel global __name__. Misalnya, gunakan editor teks favorit Anda untuk membuat bernama bernama fibo.py di direktori saat ini dengan konten berikut

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar1.jpg"/>

# 1. Lebih lanjut tentang Modul
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya first kali nama modul ditemui dalam pernyataan impor. 1 (Mereka juga dijalankan jika file dieksekusi sebagai skrip.) Modul dapat mengimpor modul lain. Biasanya, tetapi tidak diperlukan untuk menempatkan semua pernyataan import di awal modul (atau skrip, dalam hal ini). Nama-nama modul yang diimpor ditempatkan di tabel simbol global modul impor.

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar2.jpg"/>

Ini mengimpor semua nama kecuali yang dimulai dengan garis bawah (_). dalam kebanyakan kasus, programmer Python tidak menggunakan fasilitas ini karena ia memperkenalkan sekumpulan nama yang tidak diketahui ke dalam interpreter, mungkin menyembunyikan beberapa hal yang sudah Anda definisikan_

# a. Mengoperasikan modul sebagai skrip
Ketika Anda mengoperasikan modul Python dengan

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar3.jpg"/>

kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan __name__ diatur ke "__main__". Itu berarti bahwa dengan menambahkan kode ini di akhir modul Anda

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar4.jpg"/>

# b. Jalur Pencarian Modul
Ketika sebuah modul bernama spam diimpor, interpreter pertama-tama mencari modul bawaan dengan nama itu. Jika tidak ditemukan, ia kemudian mencari berkas bernama spam.py dalam daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi ini:
-	Direktori yang berisi skrip masukan (atau direktori saat ini ketika tidak ada file ditentukan).
-	PYTHONPATH (daftar nama direktori, dengan sintaksis yang sama dengan variabel shell PATH).
-	Bawaan yang bergantung pada instalasi.

# c. Berkas Python "Compiled"
Untuk mempercepat memuat modul, Python menyimpan cache versi terkompilasi dari setiap modul di direktori __pycache__ dengan nama module. version.pyc, di mana versi menyandikan format berkas terkompilasi; umumnya berisi nomor versi Python. Misalnya, dalam rilis CPython 3.3 versi yang dikompilasi dari spam.py akan di-cache sebagai __pycache__/spam.cpython-33.pyc. Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang beragam dan versi Python yang berbeda untuk hidup berdampingan.

Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, itu tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (dikompilasi saja), modul yang dikompilasi harus ada di direktori sumber, dan tidak boleh ada modul sumber.

# 2. Modul Standar
Python dilengkapi dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah, Referensi Pustaka Python ("Library Reference" selanjutnya). Beberapa modul dibangun ke dalam interpreter; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti pemanggilan sistem. Himpunan modul tersebut adalah opsi konfigurasi yang juga tergantung pada platform yang mendasarinya. Sebagai contoh, modul winreg hanya disediakan pada sistem Windows. Satu modul tertentu patut mendapat perhatian: sys, yang dibangun ke dalam setiap interpreter Python. Variabel sys.ps1 dan sys.ps2 menentukan string yang digunakan sebagai prompt primer dan sekunder.

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar5.jpg"/>

Kedua variabel ini hanya ditentukan jika interpreter dalam mode interaktif.

# 3. Fungsi dir()
Fungsi bawaan dir() digunakan untuk mencari tahu nama-nama yang ditentukan oleh modul. Ia mengembalikan list string yang diurutkan:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar6.jpg"/>

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar7.jpg"/>

dir() tidak mencantumkan nama fungsi dan variabel bawaan. Jika Anda ingin daftar itu, mereka didefinisikan dalam modul standar builtins:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar8.jpg"/>

# 4. Paket
Paket adalah cara penataan namespace modul Python dengan menggunakan "dotted module names". Sebagai contoh, nama modul A.B menetapkan submodule bernama B dalam sebuah paket bernama A. Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari harus khawatir tentang nama variabel global masing-masing, penggunaan nama modul bertitik menyelamatkan penulis paket multi-modul seperti NumPy atau Pillow dari harus khawatir tentang nama modul masing-masing .

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar9.jpg"/>

Saat mengimpor paket, Python mencari melalui direktori pada sys.path mencari subdirektori paket.

# a. Mengimpor * Dari Paket
Satu-satunya solusi adalah bagi pembuat paket untuk memberikan indeks paket secara eksplisit. Pernyataan import menggunakan konvensi berikut: jika suatu paket punya kode __init __.py yang mendefinisikan daftar bernama __all__, itu diambil sebagai daftar nama modul yang harus diimpor ketika from package import * ditemukan. Terserah pembuat paket untuk tetap memperbarui daftar ini ketika versi baru dari paket dirilis. Pembuat paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat penggunaan untuk mengimpor * dari paket mereka. Sebagai contoh, berkas sound/effects/__init__.py dapat berisi kode berikut:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar10.jpg"/>

# b. Referensi Intra-paket
Ketika paket disusun menjadi subpaket (seperti pada paket sound pada contoh), Anda dapat menggunakan impor absolut untuk merujuk pada submodul paket saudara kandung. Misalnya, jika modul sound.filters.vocoder perlu menggunakan modul echo dalam paket sound.effects, ia dapat menggunakan from sound.effects import echo.

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu04/gambar/gambar11.jpg"/>

# c. Paket di Beberapa Direktori
Paket mendukung satu atribut khusus lagi, __path__. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan file paket: __init__.py sebelum kode dalam file tersebut dieksekusi. Variabel ini dapat dimodifikasi; hal itu memengaruhi pencarian modul dan subpackage di masa depan yang terkandung dalam paket.
