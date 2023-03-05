"""
Class Abstract and Decorator

Permasalahan : Bagaimana jika kita tidak mengetahui abstract classnya itu seperti apa? Dan tiba-tiba kita bisa menggunakan salah satu dari methodnya maka akan terasa ada magic seperti implisit yang menandakan "kok bisa ya ada variable ini?"
"""

from abc import ABC, abstractmethod

class Button(ABC):
    # dalam abstract class dapat menggabungkan abstract method dan non-abstract method

    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    # solusi untuk memaksakan implementasi dari self.link agar secara eksplisit dari subclass ke class abstract dengan cara getter dan setter
    @property
    @abstractmethod
    # urutan dalam membuat property abstract method yang mengubungkan link method dengan self.link adalah property dulu baru abstractmethod
    def link(self):
        # link ini merupakan sebuah method yang kita paksa untuk dapat diimplementasikan untuk dapat berperilaku sebagai attribute yang menyambungkan dengan self.link
        pass

class PushButton(Button):

    def click(self):
        # kalau kita tidak mengetahui class abstractnya seperti apa, maka akan dirasa implisit dimana variable self.link ini darimana kalau kita tidak tahu abstract classnya seolah-olah ada magic yang sudah di set dari abstract class salah satu contohnya adalah self.link
        print("Go To: {}".format(self.link)) # karena self.link ini merupakan getter yaitu memperoleh nilai dari suatu variable maka diperlukan setter dan getter

    # untuk mengakses property dari Button yaitu link maka perlu menambahkan Button pada decoratornya
    @Button.link.setter
    def link(self, input):
        self.__link = input

    # getter dari property button
    @link.getter # tidak perlu pakai button lagi dikarenakan kita sudah tahu bahwa link sudah terhubung dengan button
    def link(self):
        return self.__link

    

tombol1 = PushButton("www.kelasterbuka.id")
tombol1.click()