class Hero : # template
    # magic keyword
    def __init__(self,inputName, inputHealth, inputPower, inputArmor) : # suatu fungsi yang akan dieksekusi pertama kali ketika suatu object dinstasiate / dibuat. Self merupakan alias nama parameter dalam memanggil atau menggunakan object sehingga self == hero1. Sehingga bisa digunakan dalam membuat attribute object tanpa harus spesifik contohnya self.name == hero1.name yang dimana jikalau ada hero2 jadinya self.name == hero2.name karena self ini merupakan template. fungsi init atau initialization ini biasanya berupa karakteristik attribute template dari suatu object. Fungsi init ini merupakan constructor dalam class
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("sniper",100, 10, 4) # karena hero1 menginstansiate class hero yang merupakan template dan didalamnya terdapat init. Maka secara otomatis ketika hero1 menginstanciate class hero akan langsung menjalankan init. Out : hallo. Parameter sniper akan dijadikan sebagai parameter inputName dalam fungsi init, self merupakan object dari hero1
# hero2 = Hero() # out = hallo
hero2 = Hero("mirana", 100, 15, 1)
hero3 = Hero("ucup", 1000, 100, 0)

print(hero1.__dict__) # fungsi dict untuk memberikan informasi apa saja yang ada pada object
print(hero2.__dict__)
print(hero3.__dict__)
