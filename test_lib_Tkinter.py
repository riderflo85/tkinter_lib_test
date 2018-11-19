#coding:utf-8

# Source -> http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel

from tkinter import *

fenetre = Tk()

# Label (POUR LA COULEUR DU BACKGROUND (bg) LES CODES COULEUR HEX FONCRTIONNE AUSSI (ex:#88b4fc))
label = Label(fenetre, text="Hello World !!!", bg="yellow")
label.pack()

# Bouton de sortie -> POUR METTRE UNE ACTION SOUHAITER QUI N'EST PAS DANS LES FONCIONS DE BASE, UTILISER DES FUNCTIONS (def maFonction():)
# Peut prendre d'autre parametre comme par exemple: bg=""
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

# Liste
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "C++")
liste.insert(3, "JavaScript")
liste.insert(4, "HTML")
liste.insert(5, "PHP")
liste.pack()

# Canvas / Toile, tableau de dessin
canvas = Canvas(fenetre, width=150, height=128, background="green")
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="red")
canvas.pack()

# Scale
# Le widget scale permet de récupérer une valeur numérique via un scroll
value2 = DoubleVar()
scale = Scale(fenetre, variable=value2)
scale.pack()

fenetre.mainloop()