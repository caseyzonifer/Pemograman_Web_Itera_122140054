Penjelasan Sistem Manajemen Perpustakaan
Saya telah membuat sistem manajemen perpustakaan sederhana menggunakan konsep OOP Python sesuai dengan persyaratan yang diberikan. Berikut penjelasan dari implementasi yang telah saya buat:
Komponen Utama
1. Abstract Class LibraryItem

Berfungsi sebagai dasar untuk semua jenis item perpustakaan
Mendefinisikan method abstract yang harus diimplementasikan subclass:

display_info(): Menampilkan informasi detail item
get_loan_period(): Menentukan periode peminjaman



2. Subclass dari LibraryItem

Book: Merepresentasikan buku dengan atribut author, ISBN, dan pages
Magazine: Merepresentasikan majalah dengan atribut issue_number dan publisher
DVD: Merepresentasikan DVD dengan atribut director, duration, dan genre

3. Class Library untuk Pengelolaan Koleksi

Menyimpan dan mengelola semua item perpustakaan
Menyediakan operasi pengelolaan seperti tambah, hapus, pencarian, dll.

Implementasi Konsep OOP
1. Abstract Class dan Inheritance (30%)

LibraryItem adalah abstract class dengan method abstract
Tiga subclass (Book, Magazine, DVD) mewarisi dan mengimplementasikan method abstract
Pewarisan memungkinkan penggunaan polymorphism melalui struktur yang konsisten

2. Encapsulation (25%)

Penggunaan atribut protected (_attribute) dan private (__attribute)
Implementasi property getter untuk mengakses atribut dengan aman
Semua data sensitif seperti ISBN, tanggal peminjaman, dll. dilindungi

3. Polymorphism (20%)

Method display_info() dan get_loan_period() diimplementasikan berbeda di tiap subclass
Perpustakaan dapat mengelola berbagai jenis item dengan interface yang konsisten
Demonstrasi polymorphism di bagian akhir program

4. Fungsionalitas Program (15%)

Menambahkan item ke perpustakaan (add_item())
Menampilkan daftar item yang tersedia (display_all_items())
Mencari item berdasarkan judul (find_items_by_title()) atau ID (find_item_by_id())
Peminjaman dan pengembalian item dengan pengelolaan status ketersediaan

5. Dokumentasi Kode (10%)

Docstring pada setiap class dan method
Penjelasan parameter, return value, dan fungsi utama
Komentar pada bagian penting untuk memperjelas alur program