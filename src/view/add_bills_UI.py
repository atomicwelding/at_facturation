""" Add bills to the cashbook ; by weld
"""

""" I used "place()" methods instead of "grid()" or "pack()", because I think they are less consistent and accurate.
As a result, the code is less pretty but allows me to position widgets, pixel perfect.
"""

""" Find a method to validate every entries
"""

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from validating_entry import *
from add_bills import *

def init(master):
    
    id = StringVar()
    name = StringVar()
    street = StringVar()
    zip = StringVar()
    city = StringVar()

    date = StringVar()
    temp1, temp2, temp3 = StringVar(), StringVar(), StringVar()

    hourly_rate = StringVar()
    quantity = StringVar()
    paymeth = StringVar()
    
    window = Toplevel(master)
    window.geometry("545x175+300+300")
    window.title("Ajouter une nouvelle facture")
    window.iconbitmap("./rsrc/favicon.ico")

#########   

    # id
    Label(window, text="ID :").place(x=0, y=0, height=20)
    #  MaxLengthEntry(window, maxlength=4, textvariable=id).place(x=25, y=0, height=21, width=48)
    Entry(window, textvariable=id).place(x=25, y=0, height=21, width=48)

#########
    
    # name
    Label(window, text="Nom :").place(x=0, y=40, height=20)
    Entry(window, textvariable=name).place(x=40, y=40, height=21, width=100)


    # street
    Label(window, text="Voie :").place(x=140, y=40, height=20)
    Entry(window, textvariable=street).place(x=179, y=40, height=21, width=100)
    
    # zip
    Label(window, text="CP :").place(x=278, y=40, height=20)
    # MaxLengthEntry(window, maxlength=5).place(x=307, y=40, height=21, width=60)
    Entry(window, textvariable=zip).place(x=307, y=40, height=21, width=60)

    # city
    Label(window, text="Ville :").place(x=370, y=40, height=20)
    Entry(window, textvariable=city).place(x=409, y=40, height=21, width=122)

#########

    # date
    Label(window, text="Date :").place(x=0, y=80, height=20)
    # MaxLengthEntry(window, maxlength=2).place(x=40, y=80, height=21, width=28)
    Entry(window, textvariable=temp1).place(x=40, y=80, height=21, width=28)

    Label(window, text="/").place(x=67, y=75, height=30)
    # MaxLengthEntry(window, maxlength=2).place(x=77, y=80, height=21, width=28)
    Entry(window, textvariable=temp2).place(x=77, y=80, height=21, width=28)

    Label(window, text="/").place(x=105, y=75, height=30)
    # MaxLengthEntry(window, maxlength=4).place(x=115, y=80, height=21, width=52)
    Entry(window, textvariable=temp3).place(x=115, y=80, height=21, width=52)

    # hourly rate
    Label(window, text="€/h :").place(x=220, y=80, height=20)
    # MaxLengthEntry(window, maxlength=4).place(x=250, y=80, height=21, width=52)
    Entry(window, textvariable=hourly_rate).place(x=250, y=80, height=21, width=52)
    
    # quantity
    Label(window, text="Qté :").place(x=305, y=80, height=20)
    # MaxLengthEntry(window, maxlength=4).place(x=340, y=80, height=21, width=52)
    Entry(window, textvariable=quantity).place(x=340, y=80, height=21, width=52)

    # payment method
    Label(window, text="Règ. :").place(x=395, y=80, height=20)
    Entry(window, textvariable=paymeth).place(x=430, y=80, height=21, width=100)

    def update():
        """ Retrieve the contents of every entry and send'em to the right managers.
        """
        miss_val = False
        date.set(temp1.get() + "/" + temp2.get() + "/" + temp3.get())
        
        for x in [id, name, street, zip, city, date, hourly_rate, quantity, paymeth]:
            if not x.get():
                miss_val = True
        
        if miss_val:
            messagebox.showinfo("Valeurs manquantes", "Veuillez renseigner les valeurs manquantes")
        else:
            # print_client([id, name, street, zip, city, date, hourly_rate, quantity, paymeth])
            add_client(int(id.get()), name.get(), street.get(), int(zip.get()), city.get())
            add_bill(int(id.get()), date.get(), int(hourly_rate.get()), int(quantity.get()), paymeth.get())

    # validate
    Button(window, text="Valider", command=update).place(x=450, y=120, height=21)

    window.mainloop()