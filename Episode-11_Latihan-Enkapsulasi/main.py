"""
Latihan Enkapsulasi

- membuat game dota dengan adanya hero yang bisa berinteraksi satu sama lain
- memiliki kemampuan sistem level dan experience
- hero memiliki attribute health, attackpower, armor dsb
- attribute pada hero akan berubah sesuai level jadi kalau misal naik level jadinya nambah nilai attributenya yg tadinya attackpowernya 1 di level 1 jadi 2 dilevel 2
- level juga dipengaruhi oleh experience sehingga level akan berubah berdasarkan banyaknya experience
- yang bisa dilihat oleh client user adalah attribute hero dan yang tidak bisa dilihat adalah experience
"""

class Hero :
    # private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor) :
        self.__name = name
        self.__healthStandar = health # health standar merupakan nilai awal dari health hero sebelum naik level
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        
        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self) :
        return "{} level {} : \n\thealth = {}/{}\n\tAttack = {}\n\tArmor = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPower, self.__armor)

    @property
    def gainExp(self) :
        pass

    @gainExp.setter
    def gainExp(self, addExp) :
        self.__exp += addExp
        if(self.__exp >= 100) :
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self, musuh) :
        self.gainExp = 50
    

slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info)

# contoh menambah exp
# slardar.gainExp = 50
# slardar.gainExp = 80
slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
print(slardar.info)
print(slardar.__dict__)
print(slardar.gainExp)

