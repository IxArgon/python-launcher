#IMPORTATION DES BIB ET DOSSIER

#BIB
from tkinter import *
import os

#DOSSIER IMPORTATION dans un sous dossier
from LAUNCHER import expirationmdp
from LAUNCHER import policy

#Definition des actions sur boutons
def bouton1():
    expirationmdp.launch()
def bouton2():
    fenetre.destroy()
def bouton3():
    print("NON DEV")
    
fenetre = Tk()

label = Label(fenetre, text="Outils d'Administration")
label.pack()

#Photo
photo = PhotoImage(file="IMAGES/application.png")
canvas = Canvas(fenetre,width=500, height=500)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

#Definition des boutons
bouton=Button(fenetre, text="Expiration de mot de passe", relief=GROOVE, command=bouton1)
bouton.pack()

bouton=Button(fenetre, text="Fermer", relief=GROOVE, command=bouton2)
bouton.pack()

bouton=Button(fenetre, text="Policy PS1", relief=GROOVE, command=bouton3)
bouton.pack()


#FIn
fenetre.mainloop()
