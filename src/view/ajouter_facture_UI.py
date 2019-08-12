""" Ouvre une nouvelle fenêtre pour ajouter une facture
"""
from tkinter import *
from tkinter.ttk import *

def init(master):
    window = Toplevel(master)
    window.geometry("700x250+300+300")
    window.title("Ajouter une nouvelle facture")

#########   
   
    # id
    Label(window, text="ID :").grid(row=0, column=0, pady=5)
    Entry(window).grid(row=0, column=1, pady=5)

#########

    # nom
    Label(window, text="Nom :").grid(row=2, column=0, pady=10)
    Entry(window).grid(row=2, column=1, pady=5)

    # adresse
    Label(window, text="Voie :").grid(row=2, column=3, pady=10)
    Entry(window).grid(row=2, column=4, pady=10)

    # code postal
    Label(window, text="CP:").grid(row=2, column=5, pady=10)
    Entry(window).grid(row=2, column=6, pady=10)

    # ville
    Label(window, text="Ville :").grid(row=2, column=7, pady=10)
    Entry(window).grid(row=2, column=8, pady=10)

#########

    # date


    Label(window, text="date :").grid(row=3, column=0, pady=10)
    Entry(window, width=2).grid(row=3, column=1, pady=10)

    Label(window, text="/").grid(row=3, column=2, pady=10)
    Entry(window, width=2).grid(row=3, column=2, pady=10)

    Label(window, text="/").grid(row=3, column=4, pady=10)
    Entry(window, width=2).grid(row=3, column=5, pady=10)



    # tarif
    # Label(window, text="tarif :").grid(row=4, column=0, pady=5)
    # Entry(window).grid(row=4, column=1, pady=5)

    # quantité
    # Label(window, text="quantité :").grid(row=5, column=0, pady=5)
    # Entry(window).grid(row=5, column=1, pady=5)

    # nature de la prestation
    # Label(window, text="nature :").grid(row=6, column=0, pady=5)
    # Entry(window).grid(row=6, column=1, pady=5)

    # valider
    #Button(window, text="Valider").grid(row=7, column=0, pady=5)

    
    window.mainloop()