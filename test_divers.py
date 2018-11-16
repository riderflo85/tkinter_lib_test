#coding:utf-8

import os
from tkinter import *

fenetre = Tk()

def callback():
    print("clique-moi")
    new_fenetre = Tk()
    label2 = Label(new_fenetre, text="bien jouer", bg="yellow")
    label2.pack()
    new_fenetre.mainloop()

label = Label(fenetre, text="Test de fonction", bg="white")
label.pack()

bouton = Button(fenetre, text="test", command=callback)
bouton.pack()

bouton2 = Button(fenetre, text="quit", command=fenetre.quit)
bouton2.pack()

fenetre.mainloop()

