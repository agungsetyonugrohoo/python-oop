"""
Diamond Problem

Diamond Problem merupakan permasalahan urutan inheritance dari suatu sub class yang menginheritance dari super class sehingga apabila ditelusuri dari super class sampai ke inheritancenya maka akan terlihat hubungannya seperti diamond atau wajik.

Urutan dalam diamond problem adalah menelusuri method yang sesuai ketika dipanggil pada suatu objek, semisal contoh di bawah ini. Terdapat 4 buah class yaitu class A, B, C dan D. Class B menginherit class A B(A), class C menginherit class A C(A), dan class D menginherit class B dan C D(B,C). Pada class A, B dan C memiliki method show yang berfungsi untuk menampilkan masing-masing method pada class. Apabila suatu object dibentuk dari class D, contoh objectnya dinamakan "objek", maka apabila objek memanggil method show maka akan diambil method show pada B, apabila pada B tidak ada method show maka akan mengambil pada C dan apabila pada B dan C tidak ada method show maka akan mengambil pada A
"""

class A:

    def show(self):
        print("ini adalah show A")

class B(A):
    pass
    # apabila method show ini dihapuskan maka objek akan mencari method show di C
    # def show(self):
    #     print("ini adalah show B")

class C(A):
    pass
    # apabila method show ini dihapuskan maka objek akan mencari method show di A
    # def show(self):
    #     print("ini adalah show C")

class D(B, C):
    pass

objek = D()
objek.show() # akan menampilkan fungsi show pada class B
# help(objek) # untuk mengetahui urutan method yang terjadi pada variable objek, urutannya (method resolution order) adalah D->B->C->A