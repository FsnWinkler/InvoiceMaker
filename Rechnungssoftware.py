import os
import tkinter as tk
import json
from tkinter import ttk
import sqlite3
from os import path
from tkinter.messagebox import showinfo


def main():
    MainWindow("Rechnungs-Erstellungs-Software", "1000x700", True)





class MainWindow:
    def __init__(self, title, geometry, active_menu):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        if active_menu:
            self.createMenu()

        self.root.mainloop()

    def createMenu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Neuer Kunde", command=self.add_customer_window)
        file_menu.add_command(label="Eigene Daten", command=self.self_info)
        file_menu.add_command(label="Kundenliste", command=self.customer)
        file_menu.add_command(label="Neues Produkt", command=self.add_pruduct_window)
        menubar.add_cascade(label="File", menu=file_menu)

    def db_connection(self, name):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(THIS_FOLDER, name)
        connection = sqlite3.connect(db_path)
        return connection

    def popup_showinfo(self, win_name, win_message):
        showinfo(win_name, win_message)


    def add_pruduct_window(self):
        add_product_win = tk.Tk()
        add_product_win.title("Neues Produkt")
        add_product_win.geometry("350x250")
        add_product_win.resizable(False, False)

        add_product_win.columnconfigure(0, weight=2)
        add_product_win.columnconfigure(1, weight=2)
        add_product_win.rowconfigure(0, weight=2)
        add_product_win.rowconfigure(1, weight=2)

        frame = ttk.Frame(add_product_win)
        font = "Helvetica 12"

        def delete_entrys():
            name_entry.delete(0, "end")
            note_entry.delete(0, "end")
            unit_entry.delete(0, "end")
            price_entry.delete(0, "end")
            ust_entry.delete(0, "end")


        def submit():
            connection = self.db_connection("customer_data.db")
            cursor = connection.cursor()


            cursor.execute(
                "CREATE TABLE IF NOT EXISTS product_data (id integer primary key autoincrement, name text, note text, unit text, price integer, ust integer, ust_apply numeric)")
            connection.commit()

            cursor.execute("INSERT INTO product_data VALUES(NULL,?,?,?,?,?,?)",
                           [
                            name_entry.get(),
                            note_entry.get(),
                            unit_entry.get(),
                            price_entry.get(),
                            ust_entry.get(),
                            ust_entry_apply.get()
                            ]
                           )
            cursor.execute("SELECT * FROM product_data")
            for f in cursor.fetchall():
                print(f)

            connection.commit()
            connection.close()
            showinfo("info", "Erfolgreich neues Produkt erstellt!")
            add_product_win.destroy()

        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(0, weight=1)

        ttk.Label(frame, text="Neues Produkt anlegen:", font="Helvetica 14").grid(columnspan=2, row=0,
                                                                                           sticky=tk.W)

        ttk.Label(frame, text="Name:", font=font).grid(column=0, row=1, sticky=tk.W)
        name_entry = ttk.Entry(frame, width=30)
        name_entry.focus()
        name_entry.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(frame, text="Notiz:", font=font).grid(column=0, row=2, sticky=tk.W)
        note_entry = ttk.Entry(frame, width=30)
        note_entry.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(frame, text="Einheit:", font=font).grid(column=0, row=3, sticky=tk.W)
        options_unit = ["h", "stk.", "cm", "kg", "km", "m"]
        unit_entry = ttk.Combobox(frame, values=options_unit, width=27)
        unit_entry.set("h")
        unit_entry.config(state="readonly")
        unit_entry.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(frame, text="Preis:", font=font).grid(column=0, row=4, sticky=tk.W)
        price_entry = ttk.Entry(frame, width=30)
        price_entry.grid(column=1, row=4, sticky=tk.W)

        ttk.Label(frame, text="Ust.:", font=font).grid(column=0, row=5, sticky=tk.W)
        options_ust = ["20%", "18%", "16%"]
        ust_entry = ttk.Combobox(frame, values=options_ust, width=27)
        ust_entry.set("20%")
        ust_entry.config(state="readonly")
        ust_entry.grid(column=1, row=5, sticky=tk.W)

        ttk.Label(frame, text="Preis basierend auf", font=font).grid(column=0, row=6, sticky=tk.W)
        options_ust = ["Preis exkl. USt.", "Preis inkl. USt.",]
        ust_entry_apply = ttk.Combobox(frame, values=options_ust, width=27)
        ust_entry_apply.set("Preis exkl. USt.")
        ust_entry_apply.config(state="readonly")
        ust_entry_apply.grid(column=1, row=6, sticky=tk.W)

        ttk.Button(frame, text='Daten speichern', command=submit).grid(column=0, row=7, ipadx=10, ipady=8, sticky=tk.W)
        ttk.Button(frame, text='Alles löschen', command=delete_entrys).grid(column=1, row=7, sticky=tk.W, ipadx=20,
                                                                            ipady=8)

        for widget in frame.winfo_children():
            widget.grid(padx=0, pady=2)

        frame.grid(column=0, row=0, padx=0, pady=0)

        add_product_win.mainloop()

    def customer(self):
        all_customer_win = tk.Toplevel()
        all_customer_win.title("Kundenliste")
        all_customer_win.geometry("700x600")
        topframe = ttk.Frame(all_customer_win)
        frame = ttk.Frame(all_customer_win)

        list = ("Vorname", "Nachname", "Firmenname", "Postleitzahl")

        for x in range(0, 4):
            tk.Label(frame, text=list[x], font="Helvetica 14", bg="#BDBDBD").grid(column=x, row=0, sticky=tk.W)






        connection = self.db_connection("customer_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customer_data")
        rows = cursor.fetchall()


        # i = 1
        # for row in rows:
        #     for col in range(len(row)):
        #         entrybox = ttk.Entry(frame,width=15, font="Helvetica 12")
        #         entrybox.grid(column=col, row=i, sticky=tk.W)
        #         entrybox.insert("end", row[col])
        #         entrybox.config(state="readonly")
        #         i = i + 1

        i = 1
        for row in rows:
            for col in range(len(row)):
                entrybox = ttk.Label(frame, text=row[col], width=15, font="Helvetica 12")
                entrybox.grid(column=col, row=i, sticky=tk.W)
                #entrybox.insert("end", row[col])
                #entrybox.config(state="readonly")
            i = i + 1

        def delete_customer():
            num_of_selected_with0 = []

            for i in range (len(rows)):
                num_of_selected_with0.append(vars[i].get())
            num_of_selected = [i for i in num_of_selected_with0 if i != 0]#clear all zeros out of the array of the selected checkbuttons
            print(len(num_of_selected))
            print(num_of_selected)
            connection = self.db_connection("customer_data.db")
            cursor = connection.cursor()
            cursor.execute("SELECT rowid FROM customer_data")#get all row ids
            data = cursor.fetchall()
            list_of_rowids = []
            for x in data:
                list_of_rowids.append(x[0])

            for x in range(len(num_of_selected)):#len of array of selected checkbuttons
                to_delete = list_of_rowids[num_of_selected[x-1]-1]#get position of rowid from the list of selected via checkbuttons
                connection = self.db_connection("customer_data.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM customer_data where rowid=?", (to_delete,))
                connection.commit()
                showinfo("Löschen erfolgreich", "Kunde erfolgreich gelöscht")

        vars = []
        for i in range(len(rows)):
            vars.append("vars"+ str(i))
            print(vars[i])
        checks = []
        for i in range(len(rows)):
            checks.append("check"+ str(i))

        for x in range(len(rows)):
            vars[x] = tk.IntVar()
            checks[x] = ttk.Checkbutton(frame, text="row"+" "+str(x+1), variable=vars[x], onvalue=x+1, offvalue=0)
            checks[x].state(["!alternate"])
            checks[x].grid(column=5, row=x+1, sticky=tk.W)


        ttk.Button(frame, text='Löschen', command=delete_customer).grid(column=5, row=10, ipadx=10, ipady=8, sticky=tk.W)



        topframe.grid(column=0,row=0)
        frame.grid(column=0, row=1, padx=10, pady=10)


    def add_customer_window(self):
        add_customer_win = tk.Tk()
        add_customer_win.title("Neuer Kunde")
        add_customer_win.geometry("350x250")
        add_customer_win.resizable(False, False)

        add_customer_win.columnconfigure(0, weight=2)
        add_customer_win.columnconfigure(1, weight=2)

        frame = ttk.Frame(add_customer_win)
        font = "Helvetica 12"

        def delete_entrys():
            firstname_entry.delete(0, "end")
            lastname_entry.delete(0, "end")
            companyname_entry.delete(0, "end")
            zip_entry.delete(0, "end")

        def submit():
            connection = self.db_connection("customer_data.db")
            cursor = connection.cursor()


            cursor.execute(
                "CREATE TABLE IF NOT EXISTS customer_data (firstname text, lastname text, company_name text, zip_code integer)")
            connection.commit()

            cursor.execute("INSERT INTO customer_data VALUES(:firstname, :lastname, :company_name, :zip_code)",
                           {
                            'firstname': firstname_entry.get(),
                            'lastname': lastname_entry.get(),
                            'company_name': companyname_entry.get(),
                            'zip_code': zip_entry.get()
                            }
                           )
            cursor.execute("SELECT * FROM customer_data")
            for f in cursor.fetchall():
                print(f)

            connection.commit()
            connection.close()
            self.popup_showinfo("info", "Erfolgreich neuer Kunde erstellt!")
            add_customer_win.destroy()

        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(0, weight=1)

        ttk.Label(frame, text="Neuen Kunden anlegen:", font="Helvetica 14").grid(columnspan=2, row=0,
                                                                                           sticky=tk.W)

        ttk.Label(frame, text="Vorname:", font=font).grid(column=0, row=1, sticky=tk.W)
        firstname_entry = ttk.Entry(frame, width=30)
        firstname_entry.focus()
        firstname_entry.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(frame, text="Nachname:", font=font).grid(column=0, row=2, sticky=tk.W)
        lastname_entry = ttk.Entry(frame, width=30)
        lastname_entry.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(frame, text="Firmenname:", font=font).grid(column=0, row=3, sticky=tk.W)
        companyname_entry = ttk.Entry(frame, width=30)
        companyname_entry.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(frame, text="Postleitzahl:", font=font).grid(column=0, row=4, sticky=tk.W)
        zip_entry = ttk.Entry(frame, width=30)
        zip_entry.grid(column=1, row=4, sticky=tk.W)

        ttk.Button(frame, text='Daten speichern', command=submit).grid(column=0, row=5, ipadx=10, ipady=8, sticky=tk.W)
        ttk.Button(frame, text='Alles löschen', command=delete_entrys).grid(column=1, row=5, sticky=tk.W, ipadx=20,
                                                                            ipady=8)

        for widget in frame.winfo_children():
            widget.grid(padx=0, pady=2)

        frame.grid(column=0, row=0, padx=0, pady=0)

        add_customer_win.mainloop()

        # def submit():
        #     with open('customer_data.json', "w", encoding="utf-8") as f:
        #         customer_information = {'name': fn.get(), 'lastname': ln.get(), 'address': company_name.get(),
        #                                 "zipcode": zip.get()}
        #         f.write(
        #             json.dumps(customer_information, indent=0)
        #         )
        #     if customer_information != None:
        #         add_customer_win.destroy()
        #
        # reg = Button(frame, text="Register", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),
        #              command=submit)
        # reg.grid(row=5, column=1)

    def self_info(self):
        self_info = tk.Toplevel()
        self_info.title("Eigene Daten")
        self_info.geometry("500x700")
        frame = ttk.Frame(self_info)


        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(0, weight=1)
        font = "Helvetica 11"

        ttk.Label(frame, text="Geben Sie bitte Ihre Daten ein:", font="Helvetica 14").grid(columnspan=2, row=0,
                                                                                           sticky=tk.W)
        list = (
            "Vorname", "Nachname", "Firmenname", "Adresse", "Telefonnummer", "E-Mail", "Webseite", "Postleitzahl")

        for i in range(len(list)):
            ttk.Label(frame, text=list[i], font=font).grid(column=0, row=i + 1, sticky=tk.W)

        firstname_entry = ttk.Entry(frame, width=30)
        firstname_entry.focus()
        firstname_entry.grid(column=1, row=1, sticky=tk.W)

        lastname_entry = ttk.Entry(frame, width=30)
        lastname_entry.grid(column=1, row=2, sticky=tk.W)

        companyname_entry = ttk.Entry(frame, width=30)
        companyname_entry.grid(column=1, row=3, sticky=tk.W)

        address_entry = ttk.Entry(frame, width=30)
        address_entry.grid(column=1, row=4, sticky=tk.W)

        phone_number_entry = ttk.Entry(frame, width=30)
        phone_number_entry.grid(column=1, row=5, sticky=tk.W)

        email_entry = ttk.Entry(frame, width=30)
        email_entry.grid(column=1, row=6, sticky=tk.W)

        website_entry = ttk.Entry(frame, width=30)
        website_entry.grid(column=1, row=7, sticky=tk.W)

        zip_entry = ttk.Entry(frame, width=30)
        zip_entry.grid(column=1, row=8, sticky=tk.W)

        def submit():
            connection = self.db_connection("customer_data.db")
            cursor = connection.cursor()

            cursor.execute(
                "CREATE TABLE IF NOT EXISTS self_info (firstname text, lastname text, company_name text, address text, phone_number integer, email text, website text, zip_code integer)")
            connection.commit()

            cursor.execute(
                "INSERT INTO self_info VALUES(:firstname, :lastname, :company_name,:address, :phone_number, :email, :website, :zip_code)",
                {
                    'firstname': firstname_entry.get(),
                    'lastname': lastname_entry.get(),
                    'company_name': companyname_entry.get(),
                    'address': address_entry.get(),
                    'phone_number': phone_number_entry.get(),
                    'email': email_entry.get(),
                    'website': website_entry.get(),
                    'zip_code': zip_entry.get()
                }
                )
            cursor.execute("SELECT * FROM self_info")
            for f in cursor.fetchall():
                print(f)

            connection.commit()
            connection.close()
            self.popup_showinfo("info", "Erfolgreich neuer Kunde erstellt!")
            self_info.destroy()

        def clrd():
            firstname_entry.delete(0, "end")
            lastname_entry.delete(0, "end")
            companyname_entry.delete(0, "end")
            address_entry.delete(0, "end")
            phone_number_entry.delete(0, "end")
            email_entry.delete(0, "end")
            website_entry.delete(0, "end")
            zip_entry.delete(0, "end")

        ttk.Button(frame, text='Daten speichern', command=submit).grid(column=0, row=9, ipadx=10, ipady=8,
                                                                       sticky=tk.W)
        ttk.Button(frame, text='Alles löschen', command=clrd).grid(column=1, row=9, sticky=tk.W, ipadx=20,
                                                                   ipady=8)

        for widget in frame.winfo_children():
            widget.grid(padx=0, pady=4)

        frame.grid(column=0, row=0, padx=10, pady=10)






main()
