#coding:utf-8

import os
from tkinter import *

fenetre = Tk()

data_file = open("/home/florent/Documents/Script_Réalisé/test_read_write.txt", "r")

def lectureDeFichiers():
    label3 = Label(fenetre, text=data_file.read(), bg="#61ff4c")
    label3.pack()
    data_file.close()

def callback():
    print("tu as click ;) ")
    new_fenetre = Tk()
    label2 = Label(new_fenetre, text="bien jouer", bg="#88b4fc")
    label2.pack()
    new_fenetre.mainloop()


label = Label(fenetre, text="Test de fonction", bg="#cdfc88")
label.pack()

bouton = Button(fenetre, text="action", bg="#c45819", command=callback)
bouton.pack()

bouton2 = Button(fenetre, text="quit", command=fenetre.quit)
bouton2.pack()

bouton3 = Button(fenetre, text="Lecture de fichiers", command=lectureDeFichiers)
bouton3.pack()

fenetre.mainloop()