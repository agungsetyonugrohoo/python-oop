"""
Super untuk Inheritance dalam Python

Super merupakan suatu teknik dalam mengambil method dari Super Class dan dapat mengubahnya sesuka kita dan tidak perlu menggunakan argumen self di dalam penggunaannya.

Kelebihan Super() dibandingkan dengan className.method() adalah apabila nama super class berubah tidak akan fleksibel atau mengikuti nama perubahan dari class karena yang digunakan adalah super() beda lain halnya dengan className.method() yang mengharuskan perubahan nama className sesuai dari class yang diinheritancekannya
"""

class Hero :
    def __init__(self, name, health) :
        self.name = name
        self.health = health

    def showInfo(self) :
        print("{} dengan health: {}".format(self.name, self.health))

class Hero_intelligent(Hero) :
    # membuat nilai default health untuk hero sebesar 100
    def __init__(self, name):
        # menggunakan class Hero untuk membuat health hero intelligent sebesar 100 sehingga menghindari perulangan
        # Hero.__init__(self, name, 100)
        # dengan menggunakan Super yang berarti mengambil Super Class atau method dari Super Class, berbeda dengan teknik di atas dengan super tidak perlu lagi menggunakan argumen self
        super().__init__(name, 100) # artinya mengambil __init__ yang ada di super class yaitu class Hero karena class Hero_intelligent merupakan inheritance dari class Hero
        super().showInfo() # mengambil method showInfo dari super class
        # method lain untuk memanggil showInfo selain super()
        Hero.showInfo(self) # kekurangan apabila nama super class berubah maka nama class name yang digunakan dalam perintah ini juga akan berubah. Hal inilah mengapa super lebih diuntungkan karena lebih fleksibel yang dimana apabila nama super class berubah maka akan mengikuti perubahannya

class Hero_strength(Hero) :
    # membuat nilai default health untuk hero sebesar 200
    def __init__(self, name):
        # menggunakan class Hero untuk membuat health hero strength sebesar 200 sehingga menghindari perulangan
        # Hero.__init__(self, name, 200)
        super().__init__(name, 200) # artinya mengambil __init__ yang ada di super class yaitu class Hero karena class Hero_intelligent merupakan inheritance dari class Hero
        super().showInfo() # mengambil method showInfo dari super class


lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

# print(lina.name, " ", lina.health)
# print(axe.name, " ", axe.health)