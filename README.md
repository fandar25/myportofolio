Nama : Muhammad Gathfaan Nur Aziz Suhendar

NPM  : 2506609214

Kelas: PBP F

### Tugas 6

1. Yang dimaksud dari REST adalah gaya arsitektur dengan server mengekspos resource dengan URL dan client mengelola dan memanipulasi melalui representasi resource tersebut yang biasanya dalam bentuk JSON menggunakan operasi HTTP. REST memiliki batasan utama, yaitu client-server, stateless, cacheable, uniform interface, dan layered system. JSON hanya sebuat struktur data, sedangkan REST adalah cara design interaksi. Jika hanya memakai API biasa dengan mengembalikan JSON, URL yang dipakai bergaya RPC, semua request memakai POST, tidak stateless, kode status tidak tepat, dan tidak ada header cache. RESTful merupakan resource, method HTTP, kode status, dan constrain yang konsisten. perbedaan PUT dan PATCH adalah:

PUT
maknanya adalah mengganti seluruh resource dengan representasi baru. Payload harus lengkap. Jika terdapat field yang tidak dikirim akan dianggap hilang atau ditolak validasi. Dapat idempoten

PATCH
maknanya adalah mengubah sebagian field resource. Payloadnya dapat hanya fieldnya saja. jika terdapat field yang tidak terkirim, maka akan dibiarkan seperti semua. tidak menjamin idempoten

2. Serializer berperan sebagai suatu penerjemah diantara objek python/django dengan format yang biasa dikirim seperti JSON. serialisasi serialisasi memiliki tugas mengubah model instance -> tipe data native python -> JSON, deserialisasi JSON/request data _> data Python tervalidasi, dan validasi & penyimpanan. keuntungannya adalah validasi dapat terpusat, mengurangi kode berulang, penanganan tipe yang kompleks pada field model contohnya, dua arah (serialisasi dan deserialisasi), kontrol field yang eksplisit dan secure, format yang konsisten, dapat terintegrasi dengan ekosistem DRF, dan mudah diuji dan dipelihara. 


3. perbedaan autentikasi dan otorisasi

autentikasi
bermakna "siapa kamu?". hasilnya adalah mengisi request.user dan request.auth. autentikasi dapat dilakukan dengan authentication_classes. respon gagalnya adalah 401 unauthorized. 

otorisasi
bermakna "apa yang boleh kamu lakukan?". hasilnya adalah dapat mengisinkan atau menolak request. otorisasi dapat dilakukan dengan permission_classes. respon gagalnya adalah 403 forbidden.

authentikasi sebagai identifikasi pengguna dan otorisasi sebagai batasan akses atau hak dalam melakukan sesuatu. 

permission wajib berada di server karena jika hanya menyembunyikan tombol saja siapapun dapat memanggil endpointnya dengan memakai curl, postman, atau devtools browser. segala hal yang berjalan pada sisi client tidak dapat dipercaya karena yang berjalan di client dapat dimodifikasi oleh pengguna. url juga dapat ditebak. 

4. CSRF tetap diperlukan. session authentication mengandalkan session id yang dapat dikirim otomatis oleh browser pada setiap request, termasuk request dari situs lain. pengguna yang sedang login di situs membuka situs lain yang bisa mengirim POST / PUT / PATCH / DELETE ke API situs yang sedang login. Token CSRF bermaksud sebagai nilai rahasia tambahan yang tidak otomatis dikirim browser sehingga tidak bisa dibaca oleh situs lainnya. 

oleh karena itu, DRF sengaja mengimplementasikannya CSRF di SessionAuthentication untuk metode yang dapat mengubah data. test force authenticate tidak dapat membuktikan perlindungan CSRF karena force_authenticate(user=...) melewati seluruh proses autentikasi sehingga request bisa langsung dianggap milik user tersebut tanpa memeriksa cookie sesi karena SessionAuthentication tidak pernah dieksekusi. 

