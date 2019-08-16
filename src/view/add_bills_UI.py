""" Add bills to the cashbook ; by weld
"""

""" I used "place()" methods instead of "grid()" or "pack()", because I think they are less consistent and accurate.
As a result, the code is less pretty but allows me to position widgets, pixel perfect.
"""

from tkinter import *
from tkinter.ttk import *

from validating_entry import *

import add_bills as ab


# def test__(name):
#     try:
#         ab.add_user(0, name, "John st", "00000", "Barbès")
#     except Exception as e:
#         print(e)

def init(master):
    
    #id, zip = (IntVar,)*2
    name, street, city = (StringVar(),)*3

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
    Entry(window, textvariable=name).place(x=40, y=40, height=21, width=100)


    # adresse
    Label(window, text="Voie :").place(x=140, y=40, height=20)
    Entry(window).place(x=179, y=40, height=21, width=100)
    
    # code postal
    Label(window, text="CP :").place(x=278, y=40, height=20)
    MaxLengthEntry(window, maxlength=5).place(x=307, y=40, height=21, width=60)

    # ville
    Label(window, text="Ville :").place(x=370, y=40, height=20)
    Entry(window).place(x=409, y=40, height=21, width=122)

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

    # nature du règlement
    Label(window, text="Règ. :").place(x=395, y=80, height=20)
    Entry(window).place(x=430, y=80, height=21, width=100)

    def update():
        print(name.get())

    # valider
    Button(window, text="Valider", command=update).place(x=450, y=120, height=21)

    window.mainloop()