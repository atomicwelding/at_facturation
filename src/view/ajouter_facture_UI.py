""" Ajouter une nouvelle facture au livre des recettes
"""

""" J'ai utilisé les méthodes "place()" plutôt que grid() ou pack() car ces dernières me semblent approximatives.
Le résultat en est un code un peu moins joli, mais qui me permet de placer au pixel près tous mes widgets.
"""
from tkinter import *
from tkinter.ttk import *

from validating_entry import * 

def init(master):
    window = Toplevel(master)
    window.geometry("545x175+300+300")
    window.title("Ajouter une nouvelle facture")

#########   

    # id
    Label(window, text="ID :").place(x=0, y=0, height=20)
    MaxLengthEntry(window, maxlength=4).place(x=25, y=0, height=21, width=48)

#########

    # nom
    Label(window, text="Nom :").place(x=0, y=40, height=20)
    Entry(window).place(x=40, y=40, height=21, width=100)

    # adresse
    Label(window, text="Voie :").place(x=140, y=40, height=20)
    Entry(window).place(x=179, y=40, height=21, width=100)
    
    # code postal
    Label(window, text="CP :").place(x=278, y=40, height=20)
    MaxLengthEntry(window, maxlength=5).place(x=307, y=40, height=21, width=60)

    # ville
    Label(window, text="Ville :").place(x=370, y=40, height=20)
    Entry(window).place(x=409, y=40, height=21, width=120)

#########

    # date
    Label(window, text="Date :").place(x=0, y=80, height=20)
    MaxLengthEntry(window, maxlength=2).place(x=40, y=80, height=21, width=28)

    Label(window, text="/").place(x=67, y=75, height=30)
    MaxLengthEntry(window, maxlength=2).place(x=77, y=80, height=21, width=28)

    Label(window, text="/").place(x=105, y=75, height=30)
    MaxLengthEntry(window, maxlength=4).place(x=115, y=80, height=21, width=52)

    # tarif horaire
    Label(window, text="€/h :").place(x=220, y=80, height=20)
    MaxLengthEntry(window, maxlength=4).place(x=250, y=80, height=21, width=52)

    # quantité
    Label(window, text="Qté :").place(x=305, y=80, height=20)
    MaxLengthEntry(window, maxlength=4).place(x=340, y=80, height=21, width=52)

    # valider
    Button(window, text="Valider").place(x=450, y=120, height=21)

    
    window.mainloop()