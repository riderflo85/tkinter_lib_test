#coding:utf-8

# Source -> http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel

from tkinter import *

fenetre = Tk()

# Label
label = Label(fenetre, text="Hello World !!!", bg="yellow")
label.pack()



fenetre.mainloop()