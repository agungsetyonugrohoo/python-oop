class Hero : # template
    # class variable merupakan variabel yang menempel pada class sehingga tidak akan menjadi milik object walaupun disematkan dalam fungsi template object
    jumlah = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor) :
        # instance variable / attribute object : variable template untuk dapat dimiliki dari suatu object
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat Hero dengan nama " + inputName)

hero1 = Hero("sniper", 100, 10, 4)
print(Hero.jumlah) # mengakses class variable
hero2 = Hero("mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup", 1000, 100, 0)
print(Hero.jumlah)

# print(Hero.__dict__) # karena berfungsi sebagai template maka tidak memiliki nilai attribute

'''
Variabel static adalah variabel yang ada di dalam class itu sendiri. Di dalam python, variabel static disebut sebagai class variable. Fungsi dari variable static adalah sebagai variabel dalam class sehingga bisa digunakan dalam melakukan operasi apapun contohnya dalam kasus ini adalah menghitung jumlah object yang sudah di instanciate
'''
