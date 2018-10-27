#coding:utf-8

# Source -> http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel

from tkinter import *

fenetre = Tk()

# Label
label = Label(fenetre, text="Hello World !!!", bg="yellow")
label.pack()

# Bouton de sortie
bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

# Case à cocher / checkbutton
check = Checkbutton(fenetre, text="Nouveau??")
check.pack()

# Radio bouton / radiobutton
# Les boutons radio sont des cases à cocher qui sont dans un groupe et dans ce groupe seul un élément peut être sélectionné.
value = StringVar()
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peut être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()


fenetre.mainloop()