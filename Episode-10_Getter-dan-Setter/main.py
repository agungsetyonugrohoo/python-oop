"""
Getter dan Setter pada Python

Operator decorator
- @staticmethod
- @classmethod
- @property : mengubah sebuah method menjadi sebuah variable
"""

class Hero :
    def __init__(self, name, health, armor) :
        # self.__name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.__name, self.__health) # variable self info ini dapat diubah-ubah dari user input sehingga tidak tetap padahal seharusnya tetap
        # self.__info = "name {} : \n\thealth: {}".format(self.__name, self.__health)
        self.name = name
        # self.info = "name {} : \n\thealth: {}".format(self.name, self.__health) # bariable nama pada variable ini tidak akan berubah meskipun diubah dari luar karena hanya berubah pada saat init dijalankan
    
    def getHealth(self) :
        return self.__health
    
    # solusi untuk permasalahan info yang dapat diubah nilainya dari luar dengan menggunakan decorator
    @property # membuat method di bawah ini sebagai suatu variable sehingga penggunaannya layaknya sebuah variable
    def info(self) :
        return "name {} : \n\thealth: {}".format(self.name, self.__health)
    
    @property
    def armor(self) :
        pass # akan berisi none dikarenakan belum ada nilainya (pass)

    @armor.getter # untuk membaca nilai variable armor
    def armor(self) :
        return self.__armor
    
    @armor.setter # unutk mengubah nilai variable armor
    def armor(self, input) :
        self.__armor = input

    @armor.deleter
    def armor(self) :
        print('armor di delet')
        self.__armor = None


sniper = Hero('sniper', 100, 10)
# print(sniper.getHealth())
# print(sniper.info)
# sniper.info = "info" # contoh mengubah nilai dari variable info
# print(sniper.info) # hasilnya akan mengubah nilai yang seharusnya sudah ditetapkan sebelumnya
# print(sniper.info) # menggunakan variable object
# print(sniper.__dict__)

# apabila menggunakan public variable dalam mengakses info dan kemudian mengubah isi namanya maka nilai variable info tidak akan berubah berikut ini contohnya
# print(sniper.info) # belum ada perubahan
# sniper.name = "dadang" # terjadi perubahan pada variable nama
# print(sniper.info) # variable nama tidak akan berubah karena nilai nama pada self.info hanya berubah pada saat awal saja atau saat pakai init sehingga tidak menjadi update, namun apabila menggunakan property bisa mengatasi permasalahan ini sehingga bisa update

print("merubah info")
print(sniper.info)
sniper.name = "dadang"
print(sniper.info)

print('getter dan setter untuk __armor')
print(sniper.armor)
print(sniper.__dict__)
# sniper.armor = 10 # akan error karena object sniper tidak memiliki attribute armor karena variable armor dalam object bersifat private sehingga enkapsulasi berhasil
# biasanya kalau method dalam megubah nilai dari suatu variable menggunakan sintaks sniper.armor(50) akan tetapi kalau menggunakan decorator pengubahan dapat dilakukan layaknya variable seperti dibawah ini
sniper.armor = 50 # method setter tpi yang memiliki kapabilitas seperti variable akibat adanya decorator armor.setter
print(sniper.armor) # akan mengubah nilai variable private armor
print(sniper.__dict__)

# mendelete variable armor dengan deleter
print("delete armor")
del sniper.armor # untuk mendelete variable armor dengan membuat nilainya menjadi None
print(sniper.__dict__)



