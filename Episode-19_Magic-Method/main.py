"""
Magic Method

Magic method adalah keywords method yang sudah ada keywordsnya yang ada di python yang bisa kita gunakan kembali. Salah satu contoh magic method standar yang selalu digunakan adalah __init__. Magic method init ini merupakan salah satu method dalam class yang akan dieksekusi pertama kali ketika digunakan pada suatu object. Tanda atau ciri-ciri dari magic method adalah terdapat double underscore pada penamaan methodnya contohnya __init__, __repr__, __str__ dsb. Magic method ini banyak sekali jenisnya dan bisa kita cari melalui dokumentasinya. Fungsi magic method ini adalah untuk melakukan operasi
"""

class Mangga:
    
    # magic method
    def __init__(self, nama, jumlah):
        # magic method ini akan dieksekusi pertama kali ketika class Mangga digunakan pada suatu object dalam menyimpan attribute dari object
        self.nama = nama
        self.jumlah = jumlah
    
    def __repr__(self):
        # magic method repr ini berfungsi sebagai informasi dari object ketika object tersebut di print (print(object))sehingga tidak menghasilkan informasi <__main__.class object at ...> akan tetapi informasi yang ditampilkan adalah dari keluaran fungsi / method repr ini sehingga lebih informatif dan biasanya berformat string. repr bisanya digunakan pada saat debugging
        # return "ini adalah repr"
        # selain itu dengan fungsi repr ini kita juga bisa menggunakan nilai property yang sudah disimpan pada init
        return "Debug - Mangga: {} dengan jumlah: {}".format(self.nama, self.jumlah)
    
    def __str__(self) -> str:
        # magic method str memiliki kelakukan sama dengan repr, bedanya dengan repr adalah biasanya str ini digunakan ketika programmnya sudah jadi atau sudah siap produksi
        return "Mangga: {} dengan jumlah: {}".format(self.nama, self.jumlah)
    
    def __add__(self, objek):
        # magic method add biasanya berfungsi untuk aritmatika, fungsinya untuk menjumlahkan antara dua buah object
        return self.jumlah + objek.jumlah
    
    @property # apabila ini tidak ada maka yang ditampilkan dict adalah bound method ...
    def __dict__(self):
        # magic method ini berfungsi untuk mengoverride dari fungsi dict sebelumnya yaitu menampilkan attribute menjadi informasi lain
        return "object ini mempunyai nama dan jumlah"


belanja1 = Mangga("arumanis", 10)
belanja2 = Mangga("mana lagi", 30)
print(belanja1)
print(belanja2)
# print(belanja1.nama)

# dikarenakan fungsi repr tidak bisa dijalankan ketika ada fungsi str, maka untuk masih dapat menjalankan fungsi repr dapat dilakukan caranya sebagai berikut
print(repr(belanja1)) # dengan perintah ini maka akan mengakses perintah repr

# magic method add dalam melakukan proses aritmatika in action
print(belanja1 + belanja2) # apabila tidak ada fungsi / magic method add akan error dikarenakan unsupported operand karena operator plus (+) tidak dikenali, dengan adanya fungsi add maka ini bisa dilaukan dengan menghasilkan penjumlahan dari jumlah belanja1 dan belanja2. Selain add masih banyak lagi yang bisa digunakan dalam melakukan operasi aritmatika

# salah satu contoh magic method lagi yang biasanya digunakan yang berfungsi untuk menampilkan attribute object
print(belanja1.__dict__)