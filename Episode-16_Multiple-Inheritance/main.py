"""
Multiple Inheritance : melakukan inheritance tidak hanya dari satu kelas akan tetapi bisa lebih sehingga memiliki kemampuan method yang lebih tidak hanya dari satu super class saja

Ciri-ciri multiple inheritance adalah terdapat lebih dari satu super class dalam sub class yang diinherit
"""

class A:
    def method_A(self):
        print("ini adalah method A")

class B:
    def method_B(self):
        print("ini adalah method B")

class C(A,B):
    # class C ini menginherit dari dua buah super class yaitu class A dan class B sehingga memiliki representasi perilaku dari class A dan class B
    pass

object = C()
# mengambil method_A dari super class A
object.method_A()
# mengambil method_B dari super class B
object.method_B()