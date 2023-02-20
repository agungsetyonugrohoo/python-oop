"""
Variable dalam class disebut dengan Class Variable dan bersifat publik

Variable dalam object (self) disebut bersifat publik

Dalam python, ada juga yang disebut sebagai private variable. Kenapa harus ada private variable?
Private variable adalah suatu variable yang tidak dapat diubah sebebasnya layaknya publik variable. Fungsinya untuk enkapsulasi yaitu untuk variable yang menempel pada suatu object tidak terlalu banyak.

Dikarenakan python tidak ada identifier variable (int, double) sehingga diperlukan konversi secara background

Variable protected bersifat publik variable dan hanya perbedaannya adalah penamaannya yang menggunakan kata protected sebagai konvensi. Akan tetapi, karena jadi konvensi maka aksesnya hanya di dalam class saja. Jadi bisa di akses tapi jangan diubah.
"""

class Hero :
    __privateJumlah = 0

    # class variable
    jumlah = 0

    def __init__(self, name, health) :
        self.name = name
        self.health = health

        # variable instance private
        # pembuatan variable private menggunakan awalan underscore "_" sebanyak dua buah
        self.__private = "private"

        # variable instance protected
        # pembuatan variable protected menggunakan awalan underscore "_" sebanyak satu buah
        self._protected = "protected"


lina = Hero("lina", 100)
print(lina.__dict__) # arti dalam perintah ini adalah bahwasannya name dan health pada object lina bersifat publik sehingga bisa diakses dimanapun

print(lina.health) # contoh pemanggilan dari publik variable dari object

# variable publik dapat kita ubah isinya juga
# lina.name = 10
# print(lina.__dict__)

# akses variable private dari object
# print(lina.__private) # menghasilkan error yang dimana tidak adanya attribute __private pada object padahal variable tersebut ada namun tidak bisa diakses dari luar

lina.private = "testing" # dengan perintah ini, akan terbuat variable baru bernama private yang berisi "private" tanpa menggantikan atau menghapus variable __private

lina.__private = "testing" # membuat assignment baru dari variable private diluar dari class, seperti menambahkan suatu variable dalam class

print(lina.__dict__)
print(lina.private)
print(lina.__private) # tidak akan bisa diakses walaupun sebelumnya sudah diassign dikarenakan dalam mengassignkan variable yang sama dengan __private malah membuat variable baru

# mencoba mengubah nilai dari variable protected
lina._protected = "testing"
print(lina.__dict__)
print(lina._protected)

# mencoba akses private variable class
print(Hero.__dict__)
print(Hero.__privateJumlah) # walaupun dibentuk sebagai class variable, private variable tetap tidak bisa di akses dari luar
