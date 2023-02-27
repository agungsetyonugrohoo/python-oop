"""
Method Resolution Order

Method Resolution Order memiliki hubungan dengan multiple inheritance. Method resolution order ini memiliki kapabilitas untuk dapat melihat urutan eksekusi dari sebuah method dengan cara menggunakan method help

Challenge :
Bagaimana jika class A dan class B memiliki method yang sama yaitu sama-sama show (tanpa spesifik A atau B) dan C melakukan inheritance terhadap keduanya maka method show mana yang akan dieksekusi? Apakah show A? Atau show B?
"""

class A:
    
    def show(self):
        print("ini adalah show A")

class B:

    def show(self):
        print("ini adalah show B")

class C(B,A):
    # class C(A,B) : urutan method dari C, ke A, ke B
    # class C(B,A) : urutan method dari C, ke B, ke A

    pass

    # apabila class C memiliki method shownya sendiri, maka secara tidak langsung class C tidak menginherit method show dari super class lain
    # def show(self):
    #     print("ini adalah show C")

objek = C()
# objek.show_A() # ini merupakan method show_A yang diinheritance dari class A
# objek.show_B() # ini merupakan method show_B yang diinheritance dari class B

# bagaimana jika kedua super class memiliki method yang sama yaitu sama-sama show?
objek.show() # jika di eksekusi maka method show yang akan diambil adalah method show dari class A. Kenapa? Karena dapat diketahui bahwa kedudukan dari class A di atas dari class B berdasarkan urutan argument inheritance pada class C yaitu (A,B) yang mana bisa kita ketahui bahwa class A diinheritance terlebih dahulu dari class B

# method resoultion order untuk mengetahui kedudukan tiap-tiap method pada class C dengan menggunakan method help yang memiliki argument variable object dari class C

# help(objek) # melalui ini bisa diketahui bahwa method resolution order atau urutan dari eksekusi method dari variable object adalah dari C ke A baru ke B berdasarkan urutan inheritance dari class C yaitu (A, B) maka yang pertama adalah C, ke A baru ke B. Untuk exit dari help object ini press "Q" dari keyboard