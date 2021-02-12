# workshop-python
<h2>Minggu 01</h2>
<b>Nama : Yusuf Nur Rahman Wahid</b></br>
<b>NIM : 185410039</b>

# Instalasi python

# 1. Dwonload python
Download installer python di situs https://www.python.org/download. 
Di sini kita menggunakan python versi 3.9.1. Bila Anda bingung yang mana linknya, silahkan klik saja link yang ada
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu01/Screenshot_1.png"/>

# 2. Instal python 
Tunggu hingga proses download selesai. Setelah selesai, 
buka folder tempat python terdownload kemudian instal.

# 3. Jalankan python
<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu01/Screenshot_2.png"/>

# Menggunakan Interpreter Python
Interpreter beroperasi mirip seperti shell Unix: ketika dipanggil dengan masukan bawaan yang terhubung ke perangkat tty, 
ia membaca dan mengeksekusi perintah secara interaktif; ketika dipanggil dengan argumen nama berkas 
atau dengan berkas sebagai masukan bawaan, ia membaca dan mengeksekusi script dari berkas itu.
ketika sudah melakukan instalasi python pada windows kita dapat langsung menggunakan shell nya.

# Melewatkan Argumen
Ketika diketahui oleh interpreter, nama skrip dan argumen tambahan sesudahnya diubah menjadi daftar string 
dan diberikan nilai ke variabel argv dalam modul sys. Anda dapat mengakses daftar ini dengan menjalankan import sys. 
Panjang daftar setidaknya satu; ketika tidak ada skrip dan tidak ada argumen yang diberikan, sys.argv[0] adalah string kosong. 
Ketika nama skrip diberikan sebagai '-' (artinya standar masukan), sys.argv[0] diatur ke '-'. Ketika command -c digunakan, 
sys.argv[0] diatur ke``'-c'. Ketika *module* :option:`-m` digunakan, ``sys.argv[0] diatur ke nama lengkap modul yang digunakan. 
Opsi ditemukan setelah command -c atau module -m tidak dikonsumsi oleh pemrosesan opsi interpreter Python tetapi ditinggalkan di sys.
argv untuk perintah atau modul yang akan ditangani.

# Mode Interaktif
Ketika perintah dibaca dari tty, interpreter dikatakan dalam interactive mode. Dalam mode ini interpreter meminta perintah 
berikutnya dengan primary prompt, biasanya tiga tanda lebih besar dari (>>>); untuk garis lanjutan, 
interpreter meminta dengan secondary prompt, secara bawaan tiga titik (...). Interpreter mencetak 
pesan selamat datang yang menyatakan nomor versinya dan pemberitahuan hak cipta sebelum mencetak prompt pertama:
