#coding:utf-8

import os
from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

data_file = open("/home/florent/Documents/Script_Réalisé/test_read_write.txt", "r")

def lectureDeFichiers():
    label3 = Label(fenetre, text=data_file.read(), bg="#61ff4c")
    label3.pack()
    data_file.close()

def callback():
    showinfo("infos", "Bien ouéj")

def alertMenu():
    showinfo("alerte", "Bravo!")

def lectureFichierMenu():
    showinfo("Data", data_file.read())
    data_file.close()


label = Label(fenetre, text="Test de fonction", bg="#cdfc88")
label.pack()

bouton = Button(fenetre, text="action", bg="#c45819", command=callback)
bouton.pack()

bouton2 = Button(fenetre, text="quit", fg="#f91b1b", command=fenetre.quit)
bouton2.pack()

bouton3 = Button(fenetre, activebackground="#1fb201", activeforeground="#ffffff", text="Lecture de fichiers", underline=0, command=lectureDeFichiers)
bouton3.pack()

menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alertMenu)
menu1.add_command(label="Editer", command=alertMenu)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alertMenu)
menu2.add_command(label="Copier", command=alertMenu)
menu2.add_command(label="Coller", command=alertMenu)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=lectureFichierMenu)
menu3.add_command(label="Aide", command=alertMenu)
menu3.add_command(label="Licence", command=alertMenu)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)
fenetre.mainloop()