from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class LibraryItem(ABC):
    """
    Abstract Base Class untuk semua item perpustakaan.
    Menyediakan struktur dasar yang harus diimplementasikan oleh semua jenis item perpustakaan.
    """
    def __init__(self, id, title, year_published):
        """
        Constructor untuk class LibraryItem
        
        Args:
            id (str): ID unik untuk item perpustakaan
            title (str): Judul item
            year_published (int): Tahun penerbitan
        """
        self._id = id                     # Protected attribute
        self._title = title               # Protected attribute
        self._year_published = year_published  # Protected attribute
        self._is_available = True         # Protected attribute
        self.__check_out_date = None     # Private attribute
        self.__due_date = None           # Private attribute
    
    @property
    def id(self):
        """Property getter untuk id"""
        return self._id
    
    @property
    def title(self):
        """Property getter untuk title"""
        return self._title
    
    @property
    def is_available(self):
        """Property getter untuk status ketersediaan"""
        return self._is_available
    
    @abstractmethod
    def display_info(self):
        """
        Abstract method yang harus diimplementasikan oleh semua subclass.
        Method ini akan menampilkan informasi detail tentang item perpustakaan.
        """
        pass
    
    @abstractmethod
    def get_loan_period(self):
        """
        Abstract method yang menentukan periode peminjaman untuk jenis item.
        Harus diimplementasikan oleh subclass.
        
        Returns:
            int: Jumlah hari untuk periode peminjaman
        """
        pass
    
    def check_out(self):
        """
        Method untuk meminjam item perpustakaan
        
        Returns:
            tuple: (bool, str) - Status operasi dan pesan
        """
        if self._is_available:
            self._is_available = False
            self.__check_out_date = datetime.now()
            self.__due_date = self.__check_out_date + timedelta(days=self.get_loan_period())
            return True, f"{self._title} telah dipinjam. Harap dikembalikan sebelum {self.__due_date.strftime('%d-%m-%Y')}"
        else:
            return False, f"{self._title} sedang tidak tersedia"
    
    def check_in(self):
        """
        Method untuk mengembalikan item perpustakaan
        
        Returns:
            tuple: (bool, str) - Status operasi dan pesan
        """
        if not self._is_available:
            self._is_available = True
            self.__check_out_date = None
            self.__due_date = None
            return True, f"{self._title} telah dikembalikan"
        else:
            return False, f"{self._title} tidak sedang dipinjam"
    
    def get_due_date(self):
        """
        Method untuk mendapatkan tanggal jatuh tempo
        
        Returns:
            datetime or None: Tanggal jatuh tempo jika dipinjam, None jika tidak
        """
        return self.__due_date


class Book(LibraryItem):
    """
    Class untuk merepresentasikan buku di perpustakaan.
    Mewarisi dari LibraryItem.
    """
    def __init__(self, id, title, year_published, author, isbn, pages):
        """
        Constructor untuk class Book
        
        Args:
            id (str): ID unik untuk buku
            title (str): Judul buku
            year_published (int): Tahun penerbitan
            author (str): Penulis buku
            isbn (str): Nomor ISBN buku
            pages (int): Jumlah halaman buku
        """
        super().__init__(id, title, year_published)
        self._author = author        # Protected attribute
        self.__isbn = isbn          # Private attribute
        self._pages = pages         # Protected attribute
    
    @property
    def author(self):
        """Property getter untuk author"""
        return self._author
    
    @property
    def isbn(self):
        """Property getter untuk isbn"""
        return self.__isbn
    
    @property
    def pages(self):
        """Property getter untuk pages"""
        return self._pages
    
    def display_info(self):
        """
        Implementasi method abstract display_info untuk menampilkan info buku
        
        Returns:
            str: Informasi lengkap tentang buku
        """
        status = "Tersedia" if self._is_available else "Tidak Tersedia"
        return f"Buku: {self._title} ({self._year_published})\n" \
               f"ID: {self._id}, ISBN: {self.__isbn}\n" \
               f"Penulis: {self._author}\n" \
               f"Halaman: {self._pages}\n" \
               f"Status: {status}"
    
    def get_loan_period(self):
        """
        Implementasi method abstract get_loan_period
        
        Returns:
            int: Periode peminjaman untuk buku (14 hari)
        """
        return 14


class Magazine(LibraryItem):
    """
    Class untuk merepresentasikan majalah di perpustakaan.
    Mewarisi dari LibraryItem.
    """
    def __init__(self, id, title, year_published, issue_number, publisher):
        """
        Constructor untuk class Magazine
        
        Args:
            id (str): ID unik untuk majalah
            title (str): Judul majalah
            year_published (int): Tahun penerbitan
            issue_number (str): Nomor terbitan majalah
            publisher (str): Penerbit majalah
        """
        super().__init__(id, title, year_published)
        self._issue_number = issue_number  # Protected attribute
        self._publisher = publisher        # Protected attribute
    
    @property
    def issue_number(self):
        """Property getter untuk issue_number"""
        return self._issue_number
    
    @property
    def publisher(self):
        """Property getter untuk publisher"""
        return self._publisher
    
    def display_info(self):
        """
        Implementasi method abstract display_info untuk menampilkan info majalah
        
        Returns:
            str: Informasi lengkap tentang majalah
        """
        status = "Tersedia" if self._is_available else "Tidak Tersedia"
        return f"Majalah: {self._title} ({self._year_published})\n" \
               f"ID: {self._id}, Edisi: {self._issue_number}\n" \
               f"Penerbit: {self._publisher}\n" \
               f"Status: {status}"
    
    def get_loan_period(self):
        """
        Implementasi method abstract get_loan_period
        
        Returns:
            int: Periode peminjaman untuk majalah (7 hari)
        """
        return 7


class DVD(LibraryItem):
    """
    Class untuk merepresentasikan DVD di perpustakaan.
    Mewarisi dari LibraryItem.
    """
    def __init__(self, id, title, year_published, director, duration, genre):
        """
        Constructor untuk class DVD
        
        Args:
            id (str): ID unik untuk DVD
            title (str): Judul DVD
            year_published (int): Tahun penerbitan
            director (str): Sutradara film
            duration (int): Durasi film dalam menit
            genre (str): Genre film
        """
        super().__init__(id, title, year_published)
        self._director = director    # Protected attribute
        self._duration = duration    # Protected attribute
        self._genre = genre          # Protected attribute
    
    @property
    def director(self):
        """Property getter untuk director"""
        return self._director
    
    @property
    def duration(self):
        """Property getter untuk duration"""
        return self._duration
    
    @property
    def genre(self):
        """Property getter untuk genre"""
        return self._genre
    
    def display_info(self):
        """
        Implementasi method abstract display_info untuk menampilkan info DVD
        
        Returns:
            str: Informasi lengkap tentang DVD
        """
        status = "Tersedia" if self._is_available else "Tidak Tersedia"
        return f"DVD: {self._title} ({self._year_published})\n" \
               f"ID: {self._id}, Sutradara: {self._director}\n" \
               f"Durasi: {self._duration} menit, Genre: {self._genre}\n" \
               f"Status: {status}"
    
    def get_loan_period(self):
        """
        Implementasi method abstract get_loan_period
        
        Returns:
            int: Periode peminjaman untuk DVD (3 hari)
        """
        return 3


class Library:
    """
    Class untuk merepresentasikan perpustakaan.
    Mengelola koleksi item perpustakaan dan operasi-operasinya.
    """
    def __init__(self, name):
        """
        Constructor untuk class Library
        
        Args:
            name (str): Nama perpustakaan
        """
        self.name = name
        self.__items = {}  # Private attribute - Dictionary untuk menyimpan semua item
        self._num_books = 0       # Protected attribute
        self._num_magazines = 0   # Protected attribute
        self._num_dvds = 0        # Protected attribute
    
    @property
    def num_items(self):
        """
        Property untuk mendapatkan jumlah total item
        
        Returns:
            int: Jumlah total item di perpustakaan
        """
        return len(self.__items)
    
    @property
    def collection_stats(self):
        """
        Property untuk mendapatkan statistik koleksi
        
        Returns:
            dict: Statistik koleksi perpustakaan
        """
        return {
            "total_items": self.num_items,
            "books": self._num_books,
            "magazines": self._num_magazines,
            "dvds": self._num_dvds,
            "available_items": sum(1 for item in self.__items.values() if item.is_available)
        }
    
    def add_item(self, item):
        """
        Method untuk menambahkan item ke perpustakaan
        
        Args:
            item (LibraryItem): Item perpustakaan untuk ditambahkan
            
        Returns:
            tuple: (bool, str) - Status operasi dan pesan
        """
        if not isinstance(item, LibraryItem):
            return False, "Item harus merupakan instance dari LibraryItem"
        
        if item.id in self.__items:
            return False, f"Item dengan ID {item.id} sudah ada di perpustakaan"
        
        self.__items[item.id] = item
        
        # Update statistik koleksi
        if isinstance(item, Book):
            self._num_books += 1
        elif isinstance(item, Magazine):
            self._num_magazines += 1
        elif isinstance(item, DVD):
            self._num_dvds += 1
            
        return True, f"{item.title} telah ditambahkan ke perpustakaan"
    
    def remove_item(self, item_id):
        """
        Method untuk menghapus item dari perpustakaan
        
        Args:
            item_id (str): ID item untuk dihapus
            
        Returns:
            tuple: (bool, str) - Status operasi dan pesan
        """
        if item_id not in self.__items:
            return False, f"Item dengan ID {item_id} tidak ditemukan"
        
        item = self.__items[item_id]
        
        # Update statistik koleksi
        if isinstance(item, Book):
            self._num_books -= 1
        elif isinstance(item, Magazine):
            self._num_magazines -= 1
        elif isinstance(item, DVD):
            self._num_dvds -= 1
            
        del self.__items[item_id]
        return True, f"{item.title} telah dihapus dari perpustakaan"
    
    def get_all_items(self):
        """
        Method untuk mendapatkan semua item di perpustakaan
        
        Returns:
            list: Semua item perpustakaan
        """
        return list(self.__items.values())
    
    def find_item_by_id(self, item_id):
        """
        Method untuk mencari item berdasarkan ID
        
        Args:
            item_id (str): ID item yang dicari
            
        Returns:
            LibraryItem or None: Item jika ditemukan, None jika tidak
        """
        return self.__items.get(item_id)
    
    def find_items_by_title(self, title_keyword):
        """
        Method untuk mencari item berdasarkan kata kunci judul
        
        Args:
            title_keyword (str): Kata kunci judul untuk pencarian
            
        Returns:
            list: Item yang judulnya mengandung kata kunci
        """
        title_keyword = title_keyword.lower()
        return [item for item in self.__items.values() 
                if title_keyword in item.title.lower()]
    
    def check_out_item(self, item_id):
        """
        Method untuk meminjam item
        
        Args:
            item_id (str): ID item yang akan dipinjam
            
        Returns:
            tuple: (bool, str) - Status operasi dan pesan
        """
        item = self.find_item_by_id(item_id)
        if not item:
            return False, f"Item dengan ID {item_id} tidak ditemukan"
        
        return item.check_out()
    
    def check_in_item(self, item_id):
        """
        Method untuk mengembalikan item
        
        Args:
            item_id (str): ID item yang akan dikembalikan
            
        Returns:
            tuple: (bool, str) - Status operasi dan pesan
        """
        item = self.find_item_by_id(item_id)
        if not item:
            return False, f"Item dengan ID {item_id} tidak ditemukan"
        
        return item.check_in()
    
    def display_all_items(self):
        """
        Method untuk menampilkan semua item
        
        Returns:
            str: Informasi tentang semua item
        """
        if not self.__items:
            return "Perpustakaan tidak memiliki item"
        
        result = f"=== Daftar Item di {self.name} ===\n"
        for item in self.__items.values():
            result += f"\n{item.display_info()}\n"
            result += "-" * 40 + "\n"
        
        return result


# Demonstrasi penggunaan sistem
if __name__ == "__main__":
    # Membuat perpustakaan
    perpus = Library("Perpustakaan Kota")
    
    # Membuat beberapa item
    buku1 = Book("B001", "Harry Potter and the Philosopher's Stone", 1997, 
                "J.K. Rowling", "9780747532699", 223)
    
    buku2 = Book("B002", "Python Programming", 2021, 
                "John Smith", "9781234567890", 415)
    
    majalah1 = Magazine("M001", "National Geographic", 2023, 
                      "Vol. 243 No. 6", "National Geographic Society")
    
    majalah2 = Magazine("M002", "Time", 2023, 
                      "Vol. 201 No. 5", "Time USA, LLC")
    
    dvd1 = DVD("D001", "Interstellar", 2014, 
              "Christopher Nolan", 169, "Sci-Fi")
    
    # Menambahkan item ke perpustakaan
    print(perpus.add_item(buku1)[1])
    print(perpus.add_item(buku2)[1])
    print(perpus.add_item(majalah1)[1])
    print(perpus.add_item(majalah2)[1])
    print(perpus.add_item(dvd1)[1])
    print()
    
    # Menampilkan statistik koleksi
    stats = perpus.collection_stats
    print(f"=== Statistik Koleksi {perpus.name} ===")
    print(f"Total item: {stats['total_items']}")
    print(f"Buku: {stats['books']}")
    print(f"Majalah: {stats['magazines']}")
    print(f"DVD: {stats['dvds']}")
    print(f"Item tersedia: {stats['available_items']}")
    print()
    
    # Menampilkan semua item
    print(perpus.display_all_items())
    
    # Mencari item berdasarkan ID
    item = perpus.find_item_by_id("B001")
    if item:
        print(f"Item dengan ID B001 ditemukan: {item.title}")
    
    # Mencari item berdasarkan judul
    items = perpus.find_items_by_title("Harry")
    if items:
        print(f"Item dengan judul mengandung 'Harry': {items[0].title}")
    print()
    
    # Meminjam dan mengembalikan item
    print(perpus.check_out_item("B001")[1])
    print(perpus.check_out_item("M001")[1])
    print()
    
    # Mencoba meminjam item yang sudah dipinjam
    print(perpus.check_out_item("B001")[1])
    print()
    
    # Mengembalikan item
    print(perpus.check_in_item("B001")[1])
    print()
    
    # Demonstrasi polymorphism
    print("=== Demonstrasi Polymorphism ===")
    items = [buku1, majalah1, dvd1]
    for item in items:
        print(f"{item.title} - Periode peminjaman: {item.get_loan_period()} hari")