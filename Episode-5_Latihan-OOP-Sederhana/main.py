"""
Membuat Game Sederhana Saling Perang

Kriteria :
- Ada hero dengan memiliki attribute nama, health, attack power, defence power
- Hero memiliki method untuk dapat menyerang hero lain dan hero yang diserang memiliki method untuk bertahan ketika diserang

Note :
- "self" dalam class didefinisikan sebagai object variable
- di python itu, sebenernya semuanya adalah object baik dari argumen fungsi seperti String sebenarnya merupakan object dari String, int dari health merupakan object dari integer
- python dibuat dari bahasa C yang terdiri dari object-object class contohnya class number, class string 
"""

class Hero :
    def __init__(self, name, health, attackPower, armorNumber) :
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
    
    def serang(self, lawan) :
        # fungsi dari variable lawan adalah menampung object dari karakter hero lain yang akan diserang
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attackPower) # untuk memberikan informasi bahwa object hero lain sedang diserang hero lain

    def diserang(self, lawan, attackPower_lawan) :
        print(self.name + " diserang " + lawan.name) # untuk memberikan informasi bahwa hero ini sedang diserang hero lain yaitu lawan
        attack_diterima = attackPower_lawan/self.armorNumber 
        print('serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima # akibat diserang terjadi pengurangan health sebesar attackpower lawan / armor dari hero yang diserang
        print('darah ' + self.name + ' tersisa ' + str(self.health)) # untuk menampilkan darah yang tersisa

sniper = Hero('sniper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 20, 10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)