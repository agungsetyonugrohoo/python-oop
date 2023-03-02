"""
Class Abstract / Base Class

Class abstract merupakan blueprint dalam membuat sebuah class sehingga instancenya adalah class. Tidak seperti class biasa yang dimana merupakan blueprint dari sebuah object dan instancenya adalah object. Class abstract akan memaksa class (yang di instance atau inheritance dari class abstract) untuk mengimplementasikan methodnya. Perbedaan dengan inheritance subclass dan superclass terhadap class abstract adalah pada inheritance subclass, subclass masih dapat memilih method dari super class mana yang dipilih atau dioverwrite sedangkan class abstract mewajibkan class yang menginheritancenya untuk mengimplementasikan methodnya.

Class abstract tidak bisa diinheritance terhadap object.

Cara membuat class abstract :
- Melakukan import dari abc (abstract base class) yang dimana hal ini digunakan untuk mendeklarasikan class abstract pada python dikarenakan pada python tidak adanya keyword untuk membuat class abstract
- Untuk membuat class biasa menjadi class abstract dalam python maka kita perlu menginherit class abstract ke class biasa
- Untuk membuat method class abstract untuk dapat memaksakan dalam mengimplementasikan terhadap class yang diinheritnya, maka perlu property @abstractmethod

Fungsi dari Class Abstract : Untuk memudahkan dalam pembuatan object-object dari class-class yang seragam fungsi basic methodnya terhadap induknya yaitu class abstract. Akan sangat berguna ketika mendesain sebuah structur object oriented design contohnya single turn, strategy pattern, observer pattern yang dimana idenya berasal dari abstract class ini
"""

# membuat class abstract
# abc = abstract base class, fungsi abc ini untuk mendeklarasikan class abstract karena pada python tidak ada keyword untuk class abstract
from abc import ABC, abstractmethod


class Button(ABC):
    # skrg menjadi class abstract dikarenakan menginherit dari class ABC

    @abstractmethod # dekorator untuk membuat abstract method dalam class abstract untuk dapat diimplementasikan dalam class inherit lainnya
    def click(self):
        pass
        # print("button click")


class PushButton(Button):
    # pass # akan error karena belum mengimplementasikan method dari class abstract
    # def click(self):
    #     print("push button click")

    # mengimplementasi method dari class abstract
    def click(self):
        print("push button click") # akan berjalan dikarenakan sudah mengimplementasikan method dari class abstract

class RadioButton(Button):
    # class kedua yang menginherit class abstract sehingga akan mengimplementasikan hal yang sama seperti pushbutton
    def click(self):
        print("radio button click")

tombol1 = PushButton() # akan tetap error dikarenakan class PushButton ini harus mengimpelemntasikan method dari class abstract Button

# tombol2 = Button() # tidak bisa diinherit karena class Button sudah menjadi class abstract (TypeError)

tombol1.click() # mengambil method dari class PushButton dan apabila pada class PushButton tidak berisi method click maka yang akan dieksekusi adalah method class Button, dan akan error apabila sudah dilakukan inheritance terhadap class abstract karena class PushButton harus mengimplementasikan method pada class abstract

# tombol2.click() # pada class Button masih bisa dilakukan instance terhadap object ketika masih menjadi class biasa akan tetapi ketika class Button menginherit ABC sehingga menjadi class abstract maka tidak bisa diinherit

# help(tombol1) # untuk memberikan informasi class PushButton yang menginherit class abstract dimana urutan inheritancenya : pushbutton, button, abc.ABC, builtins.object

# contoh bahwa dari class abstract akan seragam terhadap berbagai class yang menginheritnya
tombol2 = RadioButton()
tombol2.click()