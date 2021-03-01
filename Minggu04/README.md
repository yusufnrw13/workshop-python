# workshop-python
<h2>Minggu 03</h2>
<b>Nama : Yusuf Nur Rahman Wahid</b></br>
<b>NIM : 185410039</b>

# Struktur Data Python

# 1. Lebih Lanjut tentang Daftar Lists
Tipe data daftar list memiliki beberapa metode lagi. Berikut ini semua metode dari objek daftar list:
-	list.append(x)
Tambahkan item ke akhir daftar list. Setara dengan a[len(a):] = [x].
-	list.extend(iterable)
Perpanjang daftar list dengan menambahkan semua item dari iterable. Setara dengan a[len(a):] = iterable.
-	list.insert(i, x)
Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum memasukkan, jadi a.insert(0, x) memasukkan di bagian depan daftar list, dan a.insert(len(a), x) sama dengan a.append(x).
-	list.remove(x)
Hapus item pertama dari daftar list yang nilainya sama dengan x. Ini memunculkan ValueError jika tidak ada item seperti itu.
-	list.pop([i])
Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam daftar. 
-	list.clear()
Hapus semua item dari daftar list. Setara dengan del a[:].
-	list.index(x[, start[, end]])
Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Menimbulkan ValueError jika tidak ada item seperti itu.
-	list.count(x)
Kembalikan berapa kali x muncul dalam daftar.
-	list.sort(*, key=None, reverse=False)
Urutkan item daftar di tempat (argumen dapat digunakan untuk mengurutkan ubahsuaian customization, lihat sorted() untuk penjelasannya).
-	list.reverse()
Balikkan elemen daftar list di tempatnya.
-	list.copy()
Kembalikan salinan daftar list yang dangkal. Setara dengan a[:].
Contoh yang menggunakan sebagian besar metode daftar list:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar1.jpg"/>

# 1.1. Menggunakan Daftar Lists sebagai Tumpukan Stacks
Metode daftar membuatnya sangat mudah untuk menggunakan daftar lust sebagai tumpukan stack, di mana elemen terakhir yang 
ditambahkan adalah elemen pertama yang diambil ("last-in, first-out"). Untuk menambahkan item ke atas tumpukan, gunakan append(). 
Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit. Sebagai contoh:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar2.jpg"/>


# 1.2. Menggunakan Daftar Lists sebagai Antrian Queues
Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen 
pertama yang diambil ("first-in, first-out"); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan 
dan muncul dari akhir daftar cepat, melakukan memasukkan atau muncul dari awal daftar lambat 
(karena semua elemen lain harus digeser satu).

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar3.jpg"/>


# 1.3. Daftar List Comprehensions
Pemahaman daftar list comprehensions menyediakan cara singkat untuk membuat daftar. Aplikasi umum adalah membuat daftar 
baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan pada setiap anggota dari urutan lain atau iterable, 
atau untuk membuat urutan elemen-elemen yang memenuhi kondisi tertentu.

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar4.jpg"/>

# 1.4. Pemahaman Daftar List Comprehensions Bersarang
Ekspresi awal dalam pemahaman daftar list comprehension dapat berupa ekspresi acak arbitrary, termasuk pemahaman daftar list comprehension lainnya.

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar5.jpg"/>

# 2. Pernyataan del
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya, bukan nilainya: pernyataan del. Ini berbeda dari metode pop() yang mengembalikan nilai.
Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar list atau menghapus seluruh daftar list 
(yang kami lakukan sebelumnya dengan menetapkan daftar kosong pada slice).

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar6.jpg"/>

# 3. Tuples and Urutan Sequences
Kita melihat bahwa daftar list dan string memiliki banyak properti yang sama, seperti operasi pengindeksan dan pemotongan. 
Mereka adalah dua contoh tipe data sequence (lihat Sequence Types --- list, tuple, range). Karena Python adalah bahasa yang berkembang, 
tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lain: tuple.

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar7.jpg"/>

# 4. Himpunan Set
Python juga menyertakan tipe data untuk sets. Himpunan atau Set adalah koleksi yang tidak terurut tanpa elemen duplikat. 
Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Atur objek juga mendukung operasi matematika 
seperti penyatuan union, persimpangan intersection, perbedaan difference, dan perbedaan simetris.

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar8.jpg"/>

# 5. Kamus Dictionaries
Tipe data lain yang berguna yang dibangun ke dalam Python adalah dictionary (lihat Mapping Types --- dict). 
Kamus dictionary kadang-kadang ditemukan dalam bahasa lain sebagai "assosiative memories" atau "assosiative array".
Ini adalah contoh kecil menggunakan kamus dictionary:

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar9.jpg"/>

# 6. Teknik Perulangan
Saat mengulang kamus dictionaries, kunci key dan nilai value terkait dapat diambil pada saat yang sama menggunakan metode items().

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar10.jpg"/>

# 7. Lebih lanjut tentang Kondisi
Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa pun, bukan hanya perbandingan.
Operator perbandingan in dan not in memeriksa apakah suatu nilai terjadi (tidak terjadi) secara berurutan. 
Operator is dan is not membandingkan apakah dua objek benar-benar objek yang sama; ini hanya penting untuk objek yang
dapat diubah seperti daftar list. Semua operator pembanding memiliki prioritas yang sama, yang lebih rendah daripada semua operator numerik.

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar11.jpg"/>

# 8. Membandingkan Urutan Sequences dan Jenis Lainnya
Objek urutan sequence biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan pengurutan 
lexicographical: pertama dua item pertama dibandingkan, dan jika mereka berbeda ini menentukan hasil perbandingan; jika mereka sama, 
dua item berikutnya dibandingkan, dan seterusnya, sampai urutan mana pun habis. Jika dua item yang akan dibandingkan adalah urutannya 
sendiri dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan hasilnya sama, 
urutannya dianggap sama. Jika satu urutan adalah sub-urutan awal dari yang lain, urutan yang lebih pendek adalah yang lebih kecil (lebih pendek).

<img src="https://github.com/yusufnrw13/workshop-python/blob/master/Minggu03/gambar/gambar12.jpg"/>




