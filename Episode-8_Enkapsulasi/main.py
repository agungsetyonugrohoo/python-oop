"""
Enkapsulasi dalam Python

Aturan enkapsulasi :
- Buat semua variable private
- Untuk mengambil data yang kita butuhkan dari enkapsulasi dibutuhkan getter (mengambil variable) dan setter (mensetting variable)

Enkapsulasi berfungsi untuk mengurangi bug pada program dan membantu dalam memaintain object. Selain itu dengan adanya metode enkapsulasi ini mampu melindungi terjadinya perubahan pada variable-variable critical dari luar (input user) contohnya nama hero, attack power hero, health hero yang dimana seharusnya sudah di set dari awal game bukan berdasarkan input user atau dapat diubah berdasarkan input dari user
"""

# Enkapsulasi dalam Python

class Hero :

    def __init__(self, name, health, attackPower) :
        # membuat seluruh attribute menjadi private
        self.__name = name
        self.__health = health
        self.__attPower = attackPower
        
    # getter
    def getName(self) :
        return self.__name
    
    def getHealth(self) :
        return self.__health
    
    # setter
    def diserang(self, serangPower) :
        self.__health -= serangPower
    
    def setAttPower(self, nilaiBaru) :
        self.__attPower = nilaiBaru


# awal dari game
earthshaker = Hero("earthshaker", 50, 5)
print(earthshaker.__dict__)

# game berjalan
# earthshaker.name = "windrunner" # karena dengan menggunakan metode enkapsulasi dan jenis variable data yang digunakan adalah private maka perintah ini tidak akan mengubah nilai dari nama earthshaker melainkan menghasilkan variable baru dengan perintah tersebut

# menampilkan nama dari hero dengan method getter
# print(earthshaker.__name) # akan error karena variable private dan ternkapsulasi
print(earthshaker.getName())

# menggunakan method setter untuk mengubah nilai dari variable private yang terenkapsulasi
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())

