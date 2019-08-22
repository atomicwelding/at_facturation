""" Main interface ; by weld
"""
from tkinter import *
from tkinter.ttk import *

import sys
sys.path.insert(0, "./model/")
sys.path.insert(0, "./view/")
sys.path.insert(0, "./controller/")

from add_bills_UI import init as add_bill
from retrieve_bills import retrieve_all_bills, replace_id_by_name

def testCallback():
    retrieve_all_bills()

def init():
    # init
    window = Tk()

    window.title("at_facturation")
    window.iconbitmap("./rsrc/favicon.ico")

    # cashbook
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

    def refresh():
        tree.delete(*tree.get_children())
        for i, x in enumerate(retrieve_all_bills()):
            tree.insert("", i+1, iid=None, text="lol", values=(x[2], x[0], replace_id_by_name(x[1]), "soutien scolaire", int(x[3])*int(x[4]), x[5]))
        # window.after(16, refresh)

    tree.grid(row= 0, column=0, columnspan=3, sticky="nsew")

    # print the bill
    print_all_bills = Button(window, text="Actualiser", command=testCallback)
    print_all_bills.grid(row=1, column=0, sticky="sw")

    # add a bill
    add_new_bill = Button(window, text="Ajouter", command=lambda: add_bill(window))
    add_new_bill.grid(row=1, column=1, sticky="se")

    # remove a bill
    remove_old_bill = Button(window, text="Supprimer", command=testCallback)
    remove_old_bill.grid(row=1, column=2, sticky="se")

    window.grid_columnconfigure(0, weight=1)
    window.after(16, refresh)
    window.mainloop()