"""
Object Oriented Programming (OOP) pada Python

1. Apa itu Object Oriented Programming (OOP) ?
Dalam pola pikir pembuatan program atau sering disebut Programming Paradigm, terdiri dari dua macam paradigma (cara berpikir) diantaranya :
- Structural -> Procedural Programming : Suatu paradigma pemrograman yang akan dieksekusi berdasarkan urutan (serial) sehingga tidak bisa multi tasking atau paralel dalam eksekusinya. Contoh game dota dimana terdapat 4 karakter (a,b,c,d) yang dimana a sedang attack b, tapi c juga lagi attack d. C baru bisa attack d apabila a sudah attack b padahal di gamenya bisa dilakukan secara berbarengan (paralel). Hal inilah yang disebut serial dalam procedural programming. Kekurangan structural adalah tidak bisa dieksekusi secara paralel dan biasanya menggunakan variabel sebagai memberikan keterangan attribute
- Object-Oriented Programming : Suatu paradigma pemrograman yang semua intruksi menjadi object-object kecil. Dikarenakan berupa object dan bisa memiliki kesamaan maka dapat dikelompokkan (grouping) menjadi satu kesatuan yang bisa disebut sebagai template atau class. Contohnya class hero pada game dota yang dimana a misal sniper, b misal axe dan c adalah mirana yang tergabung dalam satu class hero sehingga a,b,c adalah object atau instance. Dengan membuat object-object kecil ini, object satu sama lain bisa berinteraksi sehingga memungkinkan adanya multitasking diantara para hero tersebut yang menjawab kekurangan dari structural programming. Biasanya menggunakan attribute dari template class dalam menjelaskan karakteristik

2. Kenapa harus ada Object Oriented Programming (OOP) ?
Konsep dasar dari OOP adalah untuk dapat melakukan interaksi antar object yang bisa terjadi kapanpun

Class merupakan template atau kumpulan dari object-object yang memiliki attribute dan method. Attribute merupakan karakteristik dari suatu objectnya dan method adalah kemampuan object dalam berinteraksi (yang bisa dilakukan oleh object)

Contoh dari class hero pada game dota:
class hero :
attribute : nama, power attack, defence armor
method : menyerang, bertahan, bergerak
"""

'''
Cara membuat class
- Harus didefinisikan sebelum digunakan
- Terdapat konvensi dari Python dimana setelah membuat class diperlukan spasi enter dua sebelum membuat program yang lain 
'''

# oop
class Hero : # template
    pass


hero1 = Hero() # object / instance (prosesnya : instansiate)
hero2 = Hero() 
hero3 = Hero()

hero1.name = "sniper" # attribute
hero1.health = 100 # attribute

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.health = 1000

print(hero1) # out : <__main__.Hero object at 0x7f64f6eecdf0> yang menyatakan hero1 adalah object dari class hero
print(hero1.__dict__) # output : {'name': 'sniper', 'health': 100}
# cara akses attribute object
print(hero1.name) # output = sniper

# structural programming
sniperName = "sniper" # dalam bentuk variabel
sniperAttack = 20
sniperHealth = 100