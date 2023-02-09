"""
Method

Method adalah template perilaku yang melekat dari suatu object. Method terbagi menjadi dua yaitu :
1. Method interactive dengan client => perilaku menghubungkan antara object dengan client (user)
2. Method interaksi antar object => perilaku yang menghubungkan antara object dengan object

Jenis-jenis method :

"""

class Hero :
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor) :
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # void function, method tanpa return, tanpa argumen
    def siapa(self) :
        print("namaku adalah " + self.name)

    # method dengan argumen, tanpa return
    def healthUp(self, up) :
        self.health += up

    # method dengan return
    def getHealth(self) :
        return self.health


hero1 = Hero("sniper", 100, 10, 5)
hero2 = Hero("mario bros", 90, 5, 10)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa() # menampilkan nama dari object hero 1 yaitu sniper
hero1.healthUp(10) # menambahkan health dari object hero 1
hero1.getHealth() # menampilkan dan mengembalikan nilai health dari object hero 1

print(hero1.health)
print(hero1.getHealth)