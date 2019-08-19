""" Main interface ; by weld
"""
from tkinter import *
from tkinter.ttk import *

import sys
sys.path.insert(0, "./model/")
sys.path.insert(0, "./view/")
sys.path.insert(0, "./controller/")

from add_bills_UI import init as add_bill

def testCallback():
    print("no callback")

def init():
    # init
    window = Tk()

    window.title("at_facturation")
    window.iconbitmap("./rsrc/favicon.ico")

    # livre des recettes
    tree = Treeview(window)
    tree['show'] = 'headings'

    tree["columns"]=("date","reference", "client", "nature", "montant", "reglement")
    tree.column("date", width=100, anchor='center')
    tree.column("reference", width=100, anchor='center')
    tree.column("client", width=100, anchor='center')
    tree.column("nature", width=100, anchor='center')
    tree.column("montant", width=100, anchor='center')
    tree.column("reglement", width=100, anchor='center')
    
    tree.heading("date", text="date")
    tree.heading("reference", text="reference")
    tree.heading("client", text="client")
    tree.heading("nature", text="nature")
    tree.heading("montant", text="montant HT (€)")
    tree.heading("reglement", text="reglement")

    tree.insert("", 1, iid=None, text="lol", values=("30/04/16", "2016-04-002007", "M. Abraham Lincoln", "soutien scolaire", "30", "espèces"))
    tree.insert("", 2, iid=None, text="lol", values=("31/04/16", "2016-04-003300", "M. Donald Trump", "soutien scolaire", "80", "chèque"))

    tree.grid(row= 0, column=0, columnspan=3, sticky="nsew")

    # imprimer les recettes
    print_all_bills = Button(window, text="Imprimer", command=testCallback)
    print_all_bills.grid(row=1, column=0, sticky="sw")

    # ajouter une facture
    add_new_bill = Button(window, text="Ajouter", command=lambda: add_bill(window))
    add_new_bill.grid(row=1, column=1, sticky="se")

    # supprimer une facture
    remove_old_bill = Button(window, text="Supprimer", command=testCallback)
    remove_old_bill.grid(row=1, column=2, sticky="se")

    window.grid_columnconfigure(0, weight=1)
    window.mainloop()