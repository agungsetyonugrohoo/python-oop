"""
Pendahuluan Inheritance

Inheritance (dalam bahasa indonesia diartikan sebagai pewarisan) adalah sesuatu yang diwariskan.

Dalam python inheritance ini berlaku untuk class ke class contohnya class 1 diwariskan ke class 2. Class 1 disebut sebagai super class dan class 2 disebut sub class. Tujuan dari inheritance ini adalah untuk menghindari pengulangan. Contoh skema inheritance

Ada class Tombol, tombol disini memiliki banyak jenis seperti tombol transparant, tombol solid dan tombol touch. Masing-masing jenis tombol ini memiliki karakteristik dasar yang sama seperti Tombol pada umumnya yang membedakan adalah dari segi bentuknya yaitu transparant, solid dan touch. Oleh karena itu, class Tombol diwariskan kepada masing-masing jenis tombol akibat memiliki karaketeristik yang sama dengan class Tombol

Cara mengaplikasikan inheritance pada python dengan cara :
class namasubclass(namasuperclass) :
maka dengan otomatis class namasubclass akan mewarisi dari class namasuperclass
"""

class Hero :
    # ini adalah super class
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    # ini adalah subclass
    pass

class Hero_strength(Hero) :
    # ini adalah subclass
    pass

lina = Hero('lina', 100)
techies = Hero_intelligent('techies', 50) # karena class Hero_intelligent sudah terinheritance dengan class Hero sehingga class Hero_intelligent memiliki karakteristik dasar yang sama seperti Hero jadinya punya init juga yang sama dengan class Hero
axe = Hero_strength('axe', 200)

print(lina.name)
# print(help(techies)) # untuk memberikan overview terkait data variable techies
print(techies.__dict__) # bukti bahwa variable techies merupakan object dari Hero_intelligent yang terinheritance dari class Hero
print(techies.name)
# print(help(axe))
print(axe.name)