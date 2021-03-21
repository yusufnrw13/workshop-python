# workshop-python
<h2>Minggu 07</h2>
<b>Nama : Yusuf Nur Rahman Wahid</b></br>
<b>NIM : 185410039</b>

# OOP PYTHON

# 1. Classes

Classes atau kelas-kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Membuat sebuah class baru menghasilkan objek dengan type baru, memungkinkan dibuat instance baru dari tipe itu. Setiap instance dari class dapat memiliki atribut yang melekat padanya untuk mempertahankan kondisinya. Instance dari sebuah class juga dapat memiliki metode (ditentukan oleh class) untuk memodifikasi kondisinya.
# a. Sepatah Kata Tentang Nama dan Objek

Objek memiliki individualitas, dan banyak nama (dalam berbagai lingkup) dapat terikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama pada Python, dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tuple).

# b. Lingkup Python dan Namespaces

Sebuah namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama namespace saat ini diimplementasikan sebagai kamus dictionary Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan itu mungkin berubah di masa depan. Contoh ruang nama namespace adalah: himpunan nama bawaan (berisi fungsi seperti abs(), dan nama pengecualian bawaan); nama-nama global dalam sebuah modul; dan nama-nama lokal dalam pemanggilan fungsi. Dalam arti himpunan atribut suatu objek juga membentuk namespace. Hal penting yang perlu diketahui tentang ruang nama namespace adalah sama sekali tidak ada hubungan antara nama dalam ruang nama namespace yang berbeda; misalnya, dua modul yang berbeda dapat mendefinisikan fungsi maximize tanpa kebingungan --- pengguna modul harus memberikan awalan dengan nama modul.


# 1. Contoh Lingkup Scopes dan Ruang Nama Namespaces

Ini adalah contoh yang menunjukkan cara mereferensikan lingkup scopes dan ruang nama namespaces yang berbeda, dan bagaimana global dan nonlocal memengaruhi pengikatan variabel:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar1.jpg"/>

# c. Pandangan Pertama tentang Kelas
Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru

# 1.	Sintaks Definisi Kelas
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar2.jpg"/>

Definisi kelas, seperti definisi fungsi (pernyataan def) harus dieksekusi sebelum mereka memiliki efek. (Anda dapat menempatkan definisi kelas di cabang dari pernyataan if, atau di dalam suatu fungsi.)

# 2. Objek Kelas Class Objects
Objek kelas mendukung dua jenis operasi: referensi atribut dan instansiasi.
Attribute references menggunakan sintaks standar yang digunakan untuk semua referensi atribut dalam Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di namespace kelas saat objek kelas dibuat. Jadi, jika definisi kelas tampak seperti ini:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar3.jpg"/>

# 3. Objek Instance
data attributes sesuai dengan "variabel instan" di Smalltalk, dan "data members" di C++. Atribut data tidak perlu dinyatakan; seperti variabel lokal, mereka muncul ketika mereka pertama kali ditugaskan. Misalnya, jika x adalah turunan dari MyClass yang dibuat di atas, bagian kode berikut akan mencetak nilai 16, tanpa meninggalkan jejak:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar4.jpg"/>

# 4. Metode Objek
Biasanya, metode dipanggil tepat setelah itu terikat:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar5.jpg"/>

Dalam contoh MyClass, ini akan mengembalikan string 'hello world'. Namun, tidak perlu memanggil metode segera: x.f adalah metode objek, dan dapat disimpan dan dipanggil di lain waktu. Sebagai contoh:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar6.jpg"/>

# 5. Variabel Kelas dan Instance
Secara umum, variabel instance adalah untuk data unik untuk setiap instance dan variabel kelas adalah untuk atribut dan metode yang dibagikan oleh semua instance kelas:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar7.jpg"/>

# d. Keterangan acak
Jika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar8.jpg"/>

# e. Pewarisan
Tentu saja, fitur bahasa tidak akan layak untuk nama "class" tanpa mendukung pewarisan. Sintaks untuk definisi kelas turunan terlihat seperti ini:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar9.jpg"/>

# 1. Pewarisan Berganda
Python mendukung bentuk pewarisan berganda juga. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar10.jpg"/>

# 1. Variabel Privat
Variabel instance "Private" yang tidak dapat diakses kecuali dari dalam suatu objek tidak ada dalam Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama diawali dengan garis bawah (mis. _spam) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode atau anggota data). Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.
Name mangling sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass. Sebagai contoh:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar11.jpg"/>

# g. Barang Sisa Odds and Ends
Kadang-kadang berguna untuk memiliki tipe data yang mirip dengan "record" Pascal atau "struct" C, menyatukan beberapa item data bernama. Definisi kelas kosong akan menghasilkan hal tersebut dengan baik:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar12.jpg"/>

# h. Iterators
Sekarang Anda mungkin telah memperhatikan bahwa sebagian besar objek penampung container dapat dibuat perulangan menggunakan pernyataan for:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar13.jpg"/>

# i. Pembangkit Generator
Generator adalah alat sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakan pernyataan hasil kapan pun mereka ingin mengembalikan data. Setiap kali next () dipanggil, generator melanjutkan di mana ia tinggalkan (ia mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi). Sebuah contoh menunjukkan bahwa generator dapat dibuat dengan sangat mudah:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar14.jpg"/>

# j. Ekspresi Pembangkit Generator
Beberapa pembangkit generators sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar list comprehensions tetapi dengan tanda kurung bukan dengan tanda kurung siku. Ungkapan-ungkapan ini dirancang untuk situasi di mana generator digunakan segera oleh fungsi penutup. Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator penuh dan cenderung lebih ramah memori daripada pemahaman daftar list comprehensions setara.
Contoh:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu07/gambar/gambar15.jpg"/>

