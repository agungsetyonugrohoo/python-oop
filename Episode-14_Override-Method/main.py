"""
Override Method dalam Python

Override Method dalam python adalah suatu teknik dalam melakukan penimpaan terhadap method-method yang diinheritance kepada sub class sehingga sub class dapat memiliki sebuah method unik daripada super classnya berdasarkan method dari super classnya. Ketika method yang ada di super class di override oleh sub class maka ketika ada object yang dibentuk dengan sub class maka yang akan dieksekusi methodnya yaitu dari sub class yang telah mengoverride method dari super class. Perlu diketahui bahwa teknik override bisa dilakukan ketika yang dioverride memiliki penamaan dan argumen yang sama, contoh :
def showInfo(self) pada super class dioverride pada sub class dengan penamaan yang sama def showInfo(self). Dan mengapa def __init__ pada super class tidak di override walaupun sama di dalam sub classnya? Hal ini dikarenakan argumen yang digunakan pada penamaan fungsi berbeda dan juga terdapat super yang menunjukkan kita menggunakan/mengambil method dari super class
"""

class Hero :
    def __init__(self, name, health) :
        self.name = name
        self.health = health
    
    def showInfo(self) :
        print("showInfo di class Hero")
        print("{} health : {}".format(
            self.name,
            self.health
            )
        )
    
class Hero_intelligent(Hero) :
    def __init__(self, name):
        super().__init__(name, 100) # mengambil method dari super class

    # override
    # melakukan override method showInfo() dari super class
    def showInfo(self): # mengoverride method dari super class
        # super().showInfo("intelligent") # caranya sama seperti init sebelumnya hanya saja menurut Mas Faqihza ini ribet lho, solusinya adalah dengan menggunakan override method dengan cara menimpa fungsi dari super class
        print("showInfo di subclass Hero_intelligent")
        print("{} \n\tTipe : intelligent,\n\thealth : {}".format(
            self.name,
            self.health
            )
        )



class Hero_strength(Hero) :
    def __init__(self, name):
        super().__init__(name, 200)
    # tidak melakukan override method showInfo() dari super class

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

lina.showInfo() # karena telah adanya override method maka yang akan dieksekusi fungsi showInfonya yaitu yang ada di dalam class Hero_intelligent (sub class)
axe.showInfo() # karena belum adanya override maka yang akan dieksekusi fungsi showInfonya yaitu yang ada di dalam class Hero (super class)