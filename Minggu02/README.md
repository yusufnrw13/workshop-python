# workshop-python
<h2>Minggu 02</h2>
<b>Nama : Yusuf Nur Rahman Wahid</b></br>
<b>NIM : 185410039</b>

# Pengendali Aliran Program

# Banyak Alat Pengatur Aliran Control Flow
Selain pernyataan while baru saja diperkenalkan, Python menggunakan pernyataan kontrol 
aliran yang biasa dikenal dari bahasa lain, dengan beberapa twist.
# a. Pernyataan If
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar1.jpg"/>

Mungkin ada nol atau lebih bagian elif, dan bagian else adalah opsional. Kata kunci 'elif' adalah kependekan dari 'else if', 
dan berguna untuk menghindari indentasi yang berlebihan. Sebuah if ... elif ... elif ... adalah urutan pengganti untuk pernyataan 
switch atau case yang ditemukan dalam bahasa lain.

# b. Pernyataan For
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar2.jpg"/>
Kode yang memodifikasi koleksi collection sambil mengulangi koleksi yang sama bisa sulit untuk diperbaiki. 
Sebagai gantinya, biasanya lebih mudah untuk mengulang salinan koleksi atau membuat koleksi baru:
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar3.jpg"/>

# c. Fungsi Range
Ini menghasilkan urutan pregressions aritmatika:
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar4.jpg"/>
Titik akhir yang diberikan tidak pernah menjadi bagian dari urutan yang dihasilkan; range(10) menghasilkan 10 nilai, 
indeks sah legal untuk item dengan urutan panjang 10. 
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar5.jpg"/>
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar6.jpg"/>
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar7.jpg"/>

Dimungkinkan untuk membiarkan rentang mulai dari nomor lain, atau untuk menentukan kenaikan 
yang berbeda (bahkan negatif; kadang-kadang ini disebut 'step').

Untuk beralih pada indeks urutan, Anda dapat menggabungkan range() dan len() sebagai berikut:
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar8.jpg"/>

# d. Pernyataan break dan continue, dan else Klausa pada Perulangan Loops.
Pernyataan perulangan loop mungkin memiliki klausa else; itu dieksekusi ketika loop berakhir melalui selesainya exhaustion iterable 
(dengan for) atau ketika kondisi menjadi salah (dengan while), tetapi tidak ketika loop diakhiri oleh pernyataan break. 
Ini dicontohkan oleh perulangan berikut, yang mencari bilangan prima:
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar9.jpg"/>

Ketika digunakan dengan sebuah perulangan, klausa else memiliki lebih banyak kesamaan dengan klausa else dari pernyataan try 
dibandingkan dengan pernyataan if: sebuah klausa else pernyataan try berjalan ketika tidak ada pengecualian terjadi, 
dan klausa else perulangan berjalan ketika tidak ada break terjadi. Untuk lebih lanjut tentang pernyataan try dan pengecualian, 
lihat Menangani Pengecualian.
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar10.jpg"/>

# e. Pernyataan Pass
Pernyataan pass tidak melakukan apa-apa. Ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan. 
Sebagai contoh:
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar11.jpg"/>

# f. Mendefinisikan Fungsi
Kita dapat membuat fungsi yang menulis seri Fibonacci ke batas acak arbitrary:
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar12.jpg"/>
Kata kunci def memperkenalkan fungsi definition. Itu harus diikuti oleh nama fungsi dan daftar parameter formal yang di dalam tanda kurung. 
Pernyataan yang membentuk tubuh fungsi mulai dari baris berikutnya, dan harus diberi indentasi.

Sangat mudah untuk menulis fungsi yang mengembalikan daftar list nomor seri Fibonacci, alih-alih mencetaknya:
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar13.jpg"/>

# g. Lebih lanjut tentang Mendefinisikan Fungsi
-	Nilai Argumen Bawaan
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar14.jpg"/>

-	Argumen Kata Kunci Keyword Arguments
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar15.jpg"/>

-	Parameter spesial
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar16.jpg"/>

-	Daftar Argumen Berubah-ubah Arbitrary
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar17.jpg"/>

-	Pembukaan Paket Unpacking Daftar Argumen
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar18.jpg"/>

-	Ekspresi Lambda
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar19.jpg"/>

-	String Dokumentasi
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu02/gambar/gambar20.jpg"/>


