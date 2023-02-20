"""
Staticmethod dan Classmethod

'Bagaimana caranya membuat enkapsulasi untuk class hero?'

staticmethod vs class method :
- keduanya dapat digunakan untuk mengakses nilai dari variable class dan object
- untuk staticmethod tidak diperlukan argumen dalam penggunaannya
- untuk classmethod memerlukan argumen dalam penggunaannya
"""

class Hero :
    # private class variable
    __jumlah = 0

    def __init__(self, name) :
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object
    def getJumlah(self) :
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk object karena tidak ada self tetapi berlaku untuk class
    def getJumlah1() :
        return Hero.__jumlah
    
    # method static (decorator), akan menempel pada object dan class
    @staticmethod # ini merupakan decorator yang berfungsi untuk menandakan bahwa method dibawah ini adalah static
    def getJumlah2() :
        return Hero.__jumlah
    
    # method class, hanya akan menempel pada class akan tetapi bisa jg untuk object karena ada konsep polimorfisme yaitu pada argumen yang digunakan sehingga argumen bisa berupa object atau jenis variable lain, dan ini akan memudahkan dalam proses inheritance dimana tidak bergantung pada nama classnya sehingga ketika diinheritance fungsi di bawah ini akan otomatis menempel sehingga lebih elegan
    @classmethod
    def getJumlah3(cls) :
        return cls.__jumlah

sniper = Hero('sniper')
# print(Hero.__jumlah) # akan error karena tidak bisa mengakses variable private dari class hero
# print(Hero.getJumlah()) # akan error karena perlu argument self sehingga hanya berlaku untuk object
# print(sniper.getJumlah()) # berlaku untuk object
# print(Hero.getJumlah1()) # berlaku untuk class

# mengambil nilai getJumlah akan tetapi berlaku untuk keduanya (object dan class) dengan menggunakan staticmethod
print(Hero.getJumlah2()) # (class) dengan static method
print(sniper.getJumlah2()) # (object) dengan static method
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2()) # (object) dengan static method
drowranger = Hero('drowranger')

# mengambil nilai yang hanya dispesifikan untuk class saja
print(Hero.getJumlah3())
print(sniper.getJumlah3()) # tidak akan error dikarenakan adanya metode polimorfisme yang menyebabkan argumen cls bisa menjadi object atau variable lainnya
