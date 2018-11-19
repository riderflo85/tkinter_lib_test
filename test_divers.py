#coding:utf-8

import os
from tkinter import *

fenetre = Tk()

def callback():
    print("tu as click ;) ")
    new_fenetre = Tk()
    label2 = Label(new_fenetre, text="bien jouer", bg="#88b4fc")
    label2.pack()
    new_fenetre.mainloop()

label = Label(fenetre, text="Test de fonction", bg="#cdfc88")
label.pack()

bouton = Button(fenetre, text="action", command=callback)
bouton.pack()

bouton2 = Button(fenetre, text="quit", command=fenetre.quit)
bouton2.pack()

fenetre.mainloop()

