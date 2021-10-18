#IMPORTATION DES BIB ET DOSSIER


#BIB
from tkinter import *
import os
from typing import Sized


#DOSSIER IMPORTATION dans un sous dossier
from LAUNCHER import expirationmdp
from LAUNCHER import policy


#Definition des actions sur boutons
def bouton1():#Ouverture appli
    expirationmdp.launch()
def bouton2():#Feremeture launcher
    fenetre.destroy()
def bouton3():
    print("NON DEV")
    
fenetre = Tk()
fenetre.title("Outils d'Administration")


#Photo
photo = PhotoImage(file="IMAGES/application.png")
canvas = Canvas(fenetre,width=400, height=400)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()


#Definition des boutons
Frame_outils = Frame(fenetre, borderwidth=25, relief=FLAT,height=300, width=300, bg='#4B99FF')
Frame_outils.pack(side=LEFT, padx=50, pady=50)
label_1 = Label(Frame_outils, text="Test", relief="solid", fg="White", bg="black", width="20")
label_1.pack()

bouton=Button(Frame_outils, text="Expiration de mot de passe", relief=RAISED, command=bouton1)
bouton.pack()

fermer_bouton=Button(Frame_outils, text="Fermer", relief=RAISED, command=bouton2)
fermer_bouton.pack()

bouton=Button(Frame_outils, text="Policy PS1", relief=RAISED, command=bouton3)
bouton.pack()

def showmdp():
    p = mdp.get() #get password from entry
    print(p)

#Formulaire de connexion
utilisateur = StringVar() #Utilisateur variable
mdp = StringVar() #Password variable
#Conteneur connexion
Frame_connexion = Frame(fenetre, borderwidth=25, relief=FLAT,height=300, width=300, bg='#ccffcc')
Frame_connexion.pack(side=RIGHT, padx=50, pady=50)
#Utilisateur
utilisateur_label = Label(Frame_connexion, text="Utilisateur :")
utilisateur_label.pack(fill='x', expand=True)
saisieutilisateur = Entry(Frame_connexion, textvariable=utilisateur, ).pack()
#Mot de passe
mdp_label = Label(Frame_connexion, text="Mot de passe :")
mdp_label.pack(fill='x', expand=True)
saisiemdp = Entry(Frame_connexion, textvariable=mdp, show='*').pack()
submit = Button(Frame_connexion, text='Show Console',command=showmdp).pack()

#FIn
fenetre.mainloop()