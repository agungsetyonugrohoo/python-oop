"""
Latihan OOP dalam Tkinter

-> Bener ga sih kalau OOP itu memiliki fungsi reusable (bisa dipakai oleh orang lain atau di dalam script lain) ?

Hint :
- Secara konvensi, setiap class dalam library python biasanya menggunakan huruf besar di awal huruf nama classnya
- Secara konvensi, setiap fungsi atau method pada python biasanya menggunakan huruf kecil semua dalam penamaannya
"""

import tkinter

main_window = tkinter.Tk() # method Tk pada tkinter merupakan object dari class tkapp

# print(main_window.__dict__)

label1 = tkinter.Label(main_window, text= "label1") # pada library tkinter ada class Label yang memiliki fungsi init sebagai attribute pada object
label2 = tkinter.Label(main_window, text= "label2")

tombol1 = tkinter.Button(main_window, text= "tombol1")
tombol2 = tkinter.Button(main_window, text= "tombol2")

# method positioning
label1.pack() # memposisikan label1 pada main_window, method pack tidak punya return dan argumen
label2.pack()

tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_window.mainloop()
