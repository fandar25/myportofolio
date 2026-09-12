Nama : Muhammad Gathfaan Nur Aziz Suhendar

NPM  : 2506609214

Kelas: PBP F

### Tugas 2

1. memasukkan URL, permintaan tersebut masuk kedalam urls.py yang ada di portofolio dan langsung meneruskan kedalam urls.py yang berada di aplikasi main karena include. lalu urls.py yang berada di aplikasi mencocokan dengan url yang ada, apakah /experience/ atau /education/ sehingga diarahkan ke dalam fungsi views yang tepat. views menjalankan fungsinya dengan mengambil data dari model, pada model saya yang dilakukan dalam mengambil data adalah Experience.objects.all(), lalu mengembalikan template experence.html menggunakan fungsi render. template tersebut berisikan data-data hasil dari pengambilan dari model dan value dari context. setelah itu, template tersebut tertampilkan dan user dapat melihatnya.
2. tidak ditulis dalam template memudahkan developer atau saya sendiri dalam melakukan debugging, reduce redundansi, dan juga membuat halaman website menjadi lebih rapih dan tidak hard coded. hard coded berpotensi untuk bekerja dalam pace yang manual dan memerlukan waktu yang sangat banyak, sedangkan jika menggunakan model, bisa diterapkan logika-logika pemrograman seperti loop atau if else sehingga lebih dinamis dan fleksibel untuk dimanipulasi dan dikelola 
3. fungsi makemigrations adalah untuk mempersiapkan berkas migrasi hasil perubahan namun belum diimplementasikan kedalam basis data. migrate mengaplikasikan perubahan model tersebut kedalam basis data. contoh perubahan model yang perlu menjalankan kedua perintah tersebut adalah mengubah atribut, seperti dalam model experience terdapat atribut id, started_at, dan seterusnya. jika menghapus atau menambah atribut, maka perlu menjalankan kedua perintah tersebut. 