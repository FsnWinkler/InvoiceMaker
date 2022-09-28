import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import customtkinter
import CreatePDF


class MainWindow(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Easy Rechnungserstellung")
        self.create_mainwindow()


    def create_mainwindow(self):

        self.selected_customer_id = 0
        self.selected_id_self_info = 0
        self.selected_product_id = []
        self.product_count = 0
        self.addedProductCounter = 0
        self.productDict = []
        self.self_dict = {}
        self.product_dict = {}
        self.customer_dict = {}
        self.product_ids = []
        self.productAmount = []
        self.productAmount2 = []

        def createPdf():

            customer_keys = [k for k, v in self.customer_dict.items() if v == str(customerVar.get())]
            #print("Kunden IDs= " + str(customer_keys[0]))
            self_info_keys = [k for k, v in self.self_dict.items() if v == str(selfInfoVar.get())]
            #print("Eigene Daten IDs= " + str(self_info_keys[0]))

            product_keys = [k for k, v in self.product_dict.items() if v == str(productVar.get())]
            self.product_ids.append(product_keys)
            # print(self.productDict[0].get())
            for i in range(len(self.productDict)):
                product_keys = [k for k, v in self.product_dict.items() if v == str(self.productDict[i].get())]
                self.product_ids.append(product_keys)
            self.productAmount2.append(self.quantityEntry.get())

            for i in range(len(self.productAmount)):
                self.productAmount2.append(self.productAmount[i].get())

            # for i in range(len(self.product_ids)):
            #     print("Product IDs= " + str(self.product_ids[i][0]) + " Menge= " + (str(self.productAmount2[i])))
            #
            # print("Product counter= " + str(self.addedProductCounter + 1))
            rows = self.addedProductCounter + 1
            productID = []
            for i in range(len(self.product_ids)):
                productID.append(self.product_ids[i][0])
            # print(productID)
            # print(self.productAmount2)
            # print(rows)
            productQ = []
            for i in range(len(self.productAmount2)):
                productQ.append(int(self.productAmount2[i]))

            filename = "output"

            CreatePDF.PDF(rows, self_info_keys[0], productID, customer_keys[0], "1", productQ, filename)
            # except:
            #     showinfo("Info", "Bitte  wählen Sie alle erforderlichen Daten aus")
            showinfo("Info", "PDF erfolgreich erstellt")





        # def show_customer():
        #     db_url = "C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db"
        #     try:
        #         connection = sqlite3.connect(db_url)
        #         cursor = connection.cursor()
        #         cursor.execute("SELECT * FROM customer_data WHERE oid=?", (self.selected_customer_id, ))
        #         data = cursor.fetchone()
        #         print(data)
        #         show_data = str(data[1] + " " + data[2] + " " + data[3])
        #         self.customer_label1.set_text(show_data)
        #         print(data[1] + " " + data[2] + " " + data[3])
        #     except:
        #         showinfo("Info", "Bitte wähle einen Kunden aus")
        #
        # def show_self_info():
        #     db_url = "C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db"
        #
        #     connection = sqlite3.connect(db_url)
        #     cursor = connection.cursor()
        #     cursor.execute("SELECT * FROM self_info WHERE oid=?", (self.selected_id_self_info, ))
        #     data = cursor.fetchone()
        #     print(data)
        #     show_data = str(data[1] + " " + data[2] + " " + data[3] + " " + data[4] + " " + str(data[8]) + " " + data[9])
        #     self.self_info_label1.set_text(show_data)
        #     print(data[1] + " " + data[2] + " " + data[3])

        # def show_product():
        #
        #     connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
        #     cursor = connection.cursor()
        #     for i in range(len(self.selected_product_id)):
        #         cursor.execute("SELECT * FROM product_data WHERE oid=?", (self.selected_product_id[i], ))
        #         data = cursor.fetchone()
        #         print(data)
        #         show_data = str(data[1] + " " + data[2] + " " + data[3] + " " + str(data[4]) + " " + data[5] + " " + data[6])
        #         if i+1 == 1:
        #             self.product_label1.set_text(show_data)
        #         if i+1 == 2:
        #             self.product_label2.set_text(show_data)
        #         if i+1 == 3:
        #             self.product_label3.set_text(show_data)
        #         if i+1 == 4:
        #             self.product_label4.set_text(show_data)
        #
        #         print(data[1] + " " + data[2] + " " + data[3])
        #
        # def reset():
        #     self.__init__()

        def get_customer_rowid():
            listRowid = []
            connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM customer_data")
            data = cursor.fetchall()
            for i in data:
                listRowid.append(i[0])

            return listRowid
        def get_self_rowid():
            listRowid = []
            connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM self_info")
            data = cursor.fetchall()
            for i in data:
                listRowid.append(i[0])

            return listRowid

        def get_product_rowid():
            listRowid = []
            connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM product_data")
            data = cursor.fetchall()
            for i in data:
                listRowid.append(i[0])

            return listRowid

        def get_products():
            connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
            cursor = connection.cursor()
            for i in get_product_rowid():
                cursor.execute("SELECT * FROM product_data WHERE oid={}".format(i))
                data = cursor.fetchall()
                string = data[0][1] + " " + data[0][2] + " " + data[0][3] + " " + str(data[0][4]) + " " + data[0][5] + " " + data[0][6]
                self.product_dict[i] = string
                productOptions.append(string)


        def get_customers():
            connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
            cursor = connection.cursor()
            for i in get_customer_rowid():
                cursor.execute("SELECT * FROM customer_data WHERE oid={}".format(i))
                data = cursor.fetchall()
                string = data[0][1] + " " + data[0][2] + " " + data[0][3] + " " + data[0][4] + " " + str(data[0][5]) + " " + data[0][6]
                self.customer_dict[i] = string
                #print(self.customer_dict)
                customerOptions.append(string)


        def get_self():
            connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
            cursor = connection.cursor()
            for i in get_self_rowid():
                cursor.execute("SELECT * FROM self_info WHERE oid={}".format(i))
                data = cursor.fetchall()
                string = data[0][1] + " " + data[0][2] + " " + data[0][3] + " " + data[0][4] + " " + str(
                    data[0][5]) + " " + data[0][6]
                self.self_dict[i] = string
                #print(self.self_dict)
                selfOptions.append(string)

        def make_product_optionmenu():
            if self.addedProductCounter <= 6:

                self.productVarx = StringVar(self)

                self.productDict.append(customtkinter.CTkOptionMenu(self.frame,variable=self.productVarx, values=list(self.product_dict.values()), width=800))
                self.productDict[self.addedProductCounter].grid(row=3+self.addedProductCounter, column=1)

                self.productAmount.append(customtkinter.CTkEntry(self.frame))
                self.productAmount[self.addedProductCounter].grid(row=3 + self.addedProductCounter, column=2)
                self.productAmount[self.addedProductCounter].insert(0, "Menge")
                self.addedProductCounter += 1


        def show_all_choosen():
            try:
                print("-"*40)
                customer_keys = [k for k, v in self.customer_dict.items() if v == str(customerVar.get())]
                print("Kunden IDs= " + str(customer_keys[0]))
                self_info_keys = [k for k, v in self.self_dict.items() if v == str(selfInfoVar.get())]
                print("Eigene Daten IDs= " + str(self_info_keys[0]))

                product_keys = [k for k, v in self.product_dict.items() if v == str(productVar.get())]
                self.product_ids.append(product_keys)

                for i in range(len(self.productDict)):
                    product_keys = [k for k, v in self.product_dict.items() if v == str(self.productDict[i].get())]
                    self.product_ids.append(product_keys)
                self.productAmount2.append(self.quantityEntry.get())

                for i in range(len(self.productAmount)):
                    self.productAmount2.append(self.productAmount[i].get())

                for i in range(len(self.product_ids)):
                    print("Product IDs= " + str(self.product_ids[i][0]) + " Menge= " + (str(self.productAmount2[i])))

                print("Product counter= " + str(self.addedProductCounter+1))
            except:
                showinfo("info", "Bitte wählen Sie ihre Daten aus!")




        font  = "Verdana 12 bold"
        #head
        self.header_label = customtkinter.CTkLabel(self, text="Rechnungserstellungs Programm", text_font=("Verdana 25 bold"))
        self.header_label.grid(row=0, column=0)
        #dataframe/mainframe
        self.frame = customtkinter.CTkFrame(self, height=400, width=200, border_width=0)
        self.frame.grid(sticky='nsew',row=1, column=0, padx=20, pady=50 , ipadx=300)

        #buttonframe
        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(sticky='nsew', row= 10, column=0, padx=20 , ipadx=300 , pady=25 )


        #customer data
        self.customer_label = customtkinter.CTkLabel(self.frame, text="Kundendaten: ", borderwidth=0, text_font=font)
        self.customer_label.grid(row=0, column=0, pady=10, sticky='w')

        customerOptions = []
        get_customers()
        customerVar = StringVar(self)
        self.optionMenuCustomer = customtkinter.CTkOptionMenu(self.frame,variable=customerVar, values=list(self.customer_dict.values()), width=800)

        self.optionMenuCustomer.grid(row=0, column=1)

        #self info data
        self.self_info_label = customtkinter.CTkLabel(self.frame, text="Eigene Daten: ", borderwidth=0, text_font=font)
        self.self_info_label.grid(row=1, column=0, pady=10, sticky='w')
        selfOptions = []
        get_self()
        selfInfoVar = StringVar(self)

        self.optionMenuSelf = customtkinter.CTkOptionMenu(self.frame,variable=selfInfoVar, values=list(self.self_dict.values()), width=800)
        self.optionMenuSelf.grid(row=1, column=1)

        #product data
        self.product_label = customtkinter.CTkLabel(self.frame, text="Produkte: ", text_font=font)
        self.product_label.grid(row=2, column=0, pady=10 , sticky='w')
        productOptions = []
        get_products()
        productVar = StringVar(self)
        self.optionMenuProduct = customtkinter.CTkOptionMenu(self.frame,variable=productVar, values=list(self.product_dict.values()), width=800)
        self.optionMenuProduct.grid(row=2, column=1)
        self.quantityEntry = customtkinter.CTkEntry(self.frame)
        self.quantityEntry.insert(0, "Menge")
        self.quantityEntry.grid(row=2, column=2, padx= 10)



        self.addProduct = customtkinter.CTkButton(self.button_frame, text="Product hinzufügen", command=make_product_optionmenu)
        self.addProduct.grid(row=0, column=6, padx=10)

        self.product_label2 = customtkinter.CTkLabel(self.frame, text="")
        self.product_label2.grid(row=3, column=1, pady=10, columnspan=22)

        self.product_label3 = customtkinter.CTkLabel(self.frame, text="")
        self.product_label3.grid(row=4, column=1, pady=10, columnspan=20)

        self.product_label4 = customtkinter.CTkLabel(self.frame, text="")
        self.product_label4.grid(row=5, column=1, pady=10, columnspan=50)

        self.product_label5 = customtkinter.CTkLabel(self.frame, text="")
        self.product_label5.grid(row=6, column=1, pady=10, columnspan=50)

        self.product_label6 = customtkinter.CTkLabel(self.frame, text="")
        self.product_label6.grid(row=7, column=1, pady=10, columnspan=50)

        self.product_label7 = customtkinter.CTkLabel(self.frame, text="")
        self.product_label7.grid(row=8, column=1, pady=10, columnspan=50)

        self.product_label8 = customtkinter.CTkLabel(self.frame, text="")
        self.product_label8.grid(row=9, column=1, pady=10, columnspan=50)

        self.product_label9 = customtkinter.CTkLabel(self.frame, text="")
        self.product_label9.grid(row=10, column=1, pady=10, columnspan=50)

        self.button = customtkinter.CTkButton(self.button_frame, text="Kundenliste", command=self.customer_window)
        self.button.grid(row=0, column=0, padx=10, pady=10)
        self.button1 = customtkinter.CTkButton(self.button_frame, text="Eigene Daten", command=self.selfinfo_window)
        self.button1.grid(row=0, column=1, padx=10, pady=10)
        # self.button2 = customtkinter.CTkButton(self.button_frame, text="Produkte Anzeigen", command=show_product)
        # self.button2.grid(row=0, column=2, padx=10, pady=10)
        self.button3 = customtkinter.CTkButton(self.button_frame, text="Produkte", command=self.product_window)
        self.button3.grid(row=0, column=2, padx=10, pady=10)
        self.button3 = customtkinter.CTkButton(self.button_frame, text="Show ", command=show_all_choosen)
        self.button3.grid(row=0, column=3, padx=10, pady=10)
        self.button5 = customtkinter.CTkButton(self.button_frame, text="PDF erstellen ", command=createPdf)
        self.button5.grid(row=0, column=4, padx=10, pady=10)


    def product_window(self):
        root = customtkinter.CTkToplevel(self)
        root.title("Produkte")

        def center_window(size, window):
            window_width = size[
                0]  # Fetches the width you gave as arg. Alternatively window.winfo_width can be used if width is not to be fixed by you.
            window_height = size[
                1]  # Fetches the height you gave as arg. Alternatively window.winfo_height can be used if height is not to be fixed by you.
            window_x = int((window.winfo_screenwidth() / 2) - (
                    window_width / 2))  # Calculates the x for the window to be in the centre
            window_y = int((window.winfo_screenheight() / 2) - (
                    window_height / 2))  # Calculates the y for the window to be in the centre

            window_geometry = str(window_width) + 'x' + str(window_height) + '+' + str(window_x) + '+' + str(
                window_y)  # Creates a geometric string argument
            window.geometry(window_geometry)  # Sets the geometry accordingly.
            return

        root.geometry(center_window((1080, 800), root))
        root.resizable(False, False)

        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM product_data")
        data = cursor.fetchall()

        style = ttk.Style(root)



        style.theme_use("default")
        style.configure("Treeview", background="#2A2D2E",
                              foreground="white", fieldbackground="#2A2D2E")
        style.configure("Treeview.Heading", background="black", foreground="white")






        style.map("Treeview",
                  background=[("selected", "#1F6AA5")]
                  )

        tree_frame = customtkinter.CTkFrame(root)
        tree_frame.pack(fill=tk.BOTH, expand=0, padx=10, pady=30, ipady=10, ipadx=10)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        if len(data) <= 20 and len(data) >= 4:
            height_treeview = len(data)
        elif len(data) <= 4:
            height_treeview = 4
        else:
            height_treeview = 20
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height=height_treeview,
                               selectmode="extended")
        my_tree = ttk.Treeview(tree_frame)

        tree_scroll.config(command=my_tree.yview)

        my_tree["columns"] = (
        "Nr.", "Beschreibung", "Notiz", "Einheit", "Preis", "USt.", "Preis basierend auf", "Gesamtpreis", "ID")
        my_tree["show"] = 'headings'

        my_tree.column("#0", width=0, minwidth=0, stretch=NO)
        my_tree.column("Nr.", width=40, minwidth=40, stretch=NO)
        my_tree.column("Beschreibung", width=300, minwidth=300, stretch=NO)
        my_tree.column("Notiz", width=200, minwidth=200, stretch=NO)
        my_tree.column("Einheit", width=60, minwidth=60, stretch=NO)
        my_tree.column("Preis", width=60, minwidth=60, stretch=NO)
        my_tree.column("USt.", width=40, minwidth=40, stretch=NO)
        my_tree.column("Preis basierend auf", width=120, minwidth=120, stretch=NO)
        my_tree.column("Gesamtpreis", width=100, minwidth=100, stretch=NO)
        my_tree.column("ID", width=0, minwidth=0, stretch=NO)

        my_tree.heading("#0", text="")
        my_tree.heading("Nr.", text="Nr.")
        my_tree.heading("Beschreibung", text="Beschreibung")
        my_tree.heading("Notiz", text="Notiz")
        my_tree.heading("Einheit", text="Einheit")
        my_tree.heading("Preis", text="Preis")
        my_tree.heading("USt.", text="USt.")
        my_tree.heading("Preis basierend auf", text="Preis basierend auf")
        my_tree.heading("Gesamtpreis", text="Gesamtpreis")
        my_tree.heading("ID", text="")

        count = 0
        for i in range(len(data)):
            if count % 2 == 0:
                tag = ("evenrow",)
            else:
                tag = ("oddrow",)

            if "exkl" in str(data[i][6]):
                my_tree.insert(parent="", index="end", iid=str(i), text="", values=(
                    i + 1, data[i][1], data[i][2], data[i][3], str(data[i][4]) + " €", data[i][5], data[i][6],
                    str(float(data[i][4])) + " €", data[i][0]), tags=tag)
                count += 1
                continue

            if "inkl" in str(data[i][6]):
                factor = int(data[i][5].replace("%", ""))
                my_tree.insert(parent="", index="end", iid=str(i), text="", values=(
                    i + 1, data[i][1], data[i][2], data[i][3], str(data[i][4]) + " €", data[i][5], data[i][6],
                    str((data[i][4] / 100) * factor + data[i][4]) + " €", data[i][0]), tags=tag)
                count += 1
                continue

        my_tree.tag_configure("oddrow", background="#2A2D2E")
        my_tree.tag_configure("evenrow", background="#2A2D2E")

        data_frame = customtkinter.CTkFrame(root)
        data_frame.pack(fill=tk.BOTH, expand=0, padx=10)

        description_label = customtkinter.CTkLabel(data_frame, text="Beschreibung:")
        description_label.grid(row=0, column=0, padx=10, pady=10)
        description_entry = customtkinter.CTkEntry(data_frame)
        description_entry.grid(row=0, column=1, padx=10, pady=10)

        note_label = customtkinter.CTkLabel(data_frame, text="Notiz:")
        note_label.grid(row=0, column=2, padx=10, pady=10)
        note_entry = customtkinter.CTkEntry(data_frame)
        note_entry.grid(row=0, column=3, padx=10, pady=10)

        unit_label = customtkinter.CTkLabel(data_frame, text="Einheit:")
        unit_label.grid(row=0, column=4, padx=10, pady=10)
        options_unit = ["h", "stk.", "cm", "kg", "km", "m"]
        unit_entry = customtkinter.CTkOptionMenu(data_frame, values=options_unit, width=145)
        unit_entry.set("h")

        unit_entry.grid(row=0, column=5, padx=10, pady=10)

        price_label = customtkinter.CTkLabel(data_frame, text="Preis:")
        price_label.grid(row=1, column=0, padx=10, pady=10)
        price_entry = customtkinter.CTkEntry(data_frame)
        price_entry.grid(row=1, column=1, padx=10, pady=10)

        ust_label = customtkinter.CTkLabel(data_frame, text="Ust.:")
        ust_label.grid(row=1, column=2, padx=10, pady=10)
        options_ust = ["20%", "18%", "16%"]
        ust_entry = customtkinter.CTkOptionMenu(data_frame, values=options_ust, width=145)
        ust_entry.set("20%")
        ust_entry.grid(row=1, column=3, padx=10, pady=10)

        ust_entry_apply = customtkinter.CTkLabel(data_frame, text="Preis basierend auf:")
        ust_entry_apply.grid(row=1, column=4, padx=10, pady=10)
        options_ust_is = ["Preis exkl. USt.", "Preis inkl. USt.", ]
        ust_entry_apply = customtkinter.CTkOptionMenu(data_frame, values=options_ust_is, width=145)
        ust_entry_apply.set("Preis exkl. USt.")
        ust_entry_apply.grid(row=1, column=5, padx=10, pady=10)

        def is_number():
            try:
                float(price_entry.get())
                return True
            except:
                return False

        def is_string():
            try:
                if description_entry.get().isdigit():
                    raise NameError
                else:
                    return True
            except:
                return False

        def select_record(e):
            description_entry.delete(0, "end")
            note_entry.delete(0, "end")
            price_entry.delete(0, "end")

            selected = my_tree.focus()
            values = my_tree.item(selected, "values")

            description_entry.insert(0, values[1])
            note_entry.insert(0, values[2])
            remove_euro = values[4].replace(" €", "")
            price_entry.insert(0, remove_euro)
            unit_entry.set(values[3])
            ust_entry.set(values[5])
            ust_entry_apply.set(values[6])

        def clear_boxes():
            description_entry.delete(0, "end")
            note_entry.delete(0, "end")
            price_entry.delete(0, "end")
            unit_entry.set("h")
            ust_entry.set("20%")
            ust_entry_apply.set("Preis exkl. USt.")

            for i in my_tree.selection():
                my_tree.selection_remove(i)

        def delete_record():
            selected = my_tree.focus()
            if selected != "":
                values = my_tree.item(selected, "values")
                my_tree.delete(selected)

                connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM product_data WHERE oid=?", (values[8],))
                connection.commit()
                clear_boxes()
                tree_frame.update()

        def add_product():
            if is_string():
                if is_number():
                    connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
                    cursor = connection.cursor()
                    cursor.execute(
                        "CREATE TABLE IF NOT EXISTS product_data (id integer primary key autoincrement, name text, note text, unit text, price integer, ust integer, ust_apply numeric)")
                    connection.commit()

                    cursor.execute("INSERT INTO product_data VALUES(NULL,?,?,?,?,?,?)",
                                   [
                                       description_entry.get(),
                                       note_entry.get(),
                                       unit_entry.get(),
                                       price_entry.get(),
                                       ust_entry.get(),
                                       ust_entry_apply.get()
                                   ]
                                   )
                    connection.commit()
                    connection.close()
                    showinfo("info", "Erfolgreich neues Produkt erstellt!")
                    clear_boxes()
                    root.destroy()
                    self.product_window()
                else:
                    showinfo("info", "Bitte als Preis eine Nummer eingeben!")
            else:
                showinfo("info", "Bitte keine Nummer als Beschreibung eingeben!")

        def update_record():
            if is_string():
                if is_number():
                    selected = my_tree.focus()
                    if selected != "":
                        values = my_tree.item(selected, "values")
                        my_tree.delete(selected)

                        connection = sqlite3.connect(
                            "C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
                        cursor = connection.cursor()
                        cursor.execute(
                            "UPDATE product_data SET name=?, note=?, unit=?, price=?, ust=?, ust_apply=? WHERE oid=?",
                            [
                                description_entry.get(),
                                note_entry.get(),
                                unit_entry.get(),
                                price_entry.get(),
                                ust_entry.get(),
                                ust_entry_apply.get(),
                                values[8]
                            ]

                            )
                        connection.commit()
                        clear_boxes()
                        root.destroy()
                        self.product_window()
                else:
                    showinfo("info", "Bitte als Preis eine Nummer eingeben!")
            else:
                showinfo("info", "Bitte keine Nummer als Beschreibung eingeben!")

        def prevent_resize(event):
            if my_tree.identify_region(event.x, event.y) == "separator":
                return "break"

        def choose():
            selected = my_tree.focus()
            if selected != "":
                values = my_tree.item(selected, "values")
                self.selected_product_id.append(values[8])
                self.product_count += 1
                root.destroy()

        my_tree.bind('<Button-1>', prevent_resize)
        my_tree.bind('<Motion>', prevent_resize)

        button_frame = customtkinter.CTkFrame(root)
        pack = button_frame.pack(fill=tk.BOTH, expand=0, padx=10, pady=10)

        update_button = customtkinter.CTkButton(button_frame, text="Aktualisieren", command=update_record)
        update_button.grid(row=0, column=0, padx=10, pady=10)

        add_button = customtkinter.CTkButton(button_frame, text="Hinzufügen", command=add_product)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        remove_many_button = customtkinter.CTkButton(button_frame, text="Löschen", command=delete_record)
        remove_many_button.grid(row=0, column=2, padx=10, pady=10)

        select_button = customtkinter.CTkButton(button_frame, text="Eingabefelder Löschen", command=clear_boxes)
        select_button.grid(row=0, column=5, padx=10, pady=10)

        select_product_button = customtkinter.CTkButton(button_frame, text="Diesen Eintrag nehmen", command=choose)
        select_product_button.grid(row=0, column=5, padx=10, pady=10)


        my_tree.bind("<ButtonRelease-1>", select_record)
        my_tree.pack()

        root.mainloop()

    def customer_window(self):
        root = customtkinter.CTkToplevel(self)
        root.title("Kundenliste")

        def center_window(size, window):
            window_width = size[
                0]  # Fetches the width you gave as arg. Alternatively window.winfo_width can be used if width is not to be fixed by you.
            window_height = size[
                1]  # Fetches the height you gave as arg. Alternatively window.winfo_height can be used if height is not to be fixed by you.
            window_x = int((window.winfo_screenwidth() / 2) - (
                    window_width / 2))  # Calculates the x for the window to be in the centre
            window_y = int((window.winfo_screenheight() / 2) - (
                    window_height / 2))  # Calculates the y for the window to be in the centre

            window_geometry = str(window_width) + 'x' + str(window_height) + '+' + str(window_x) + '+' + str(
                window_y)  # Creates a geometric string argument
            window.geometry(window_geometry)  # Sets the geometry accordingly.
            return

        root.geometry(center_window((1080, 800), root))
        root.resizable(False, False)

        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customer_data")
        data = cursor.fetchall()

        style = ttk.Style(root)

        style.theme_use("default")
        style.configure("Treeview", background="#2A2D2E",
                        foreground="white", fieldbackground="#2A2D2E")
        style.configure("Treeview.Heading", background="black", foreground="white")

        style.map("Treeview",
                  background=[("selected", "#1F6AA5")]
                  )

        tree_frame = customtkinter.CTkFrame(root)
        tree_frame.pack(fill=tk.BOTH, expand=0, padx=10, pady=30, ipady=10, ipadx=10)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        if len(data) <= 20 and len(data) >= 4:
            height_treeview = len(data)
        elif len(data) <= 4:
            height_treeview = 4
        else:
            height_treeview = 20
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height=height_treeview,
                               selectmode="extended")

        tree_scroll.config(command=my_tree.yview)

        my_tree["columns"] = (
            "Nr.", "Name", "Nachname", "Firmenname", "Adresse", "Postleitzahl", "Ort", "ID")
        my_tree["show"] = 'headings'

        my_tree.column("#0", width=0, minwidth=0, stretch=NO)
        my_tree.column("Nr.", width=40, minwidth=40, stretch=NO)
        my_tree.column("Name", width=140, minwidth=140, stretch=NO)
        my_tree.column("Nachname", width=140, minwidth=140, stretch=NO)
        my_tree.column("Firmenname", width=180, minwidth=180, stretch=NO)
        my_tree.column("Adresse", width=240, minwidth=240, stretch=NO)
        my_tree.column("Postleitzahl", width=80, minwidth=80, stretch=NO)
        my_tree.column("Ort", width=120, minwidth=120, stretch=NO)
        my_tree.column("ID", width=0, minwidth=0, stretch=NO)

        my_tree.heading("#0", text="")
        my_tree.heading("Nr.", text="Nr.")
        my_tree.heading("Name", text="Name")
        my_tree.heading("Nachname", text="Nachname")
        my_tree.heading("Firmenname", text="Firmenname")
        my_tree.heading("Adresse", text="Adresse")
        my_tree.heading("Postleitzahl", text="Postleitzahl")
        my_tree.heading("Ort", text="Ort")
        my_tree.heading("ID", text="")


        for i in range(len(data)):
            my_tree.insert(parent="", index="end", iid=str(i), text="", values=(
                i + 1, data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][0]))


        data_frame = customtkinter.CTkFrame(root)
        data_frame.pack(fill=tk.BOTH, expand=0, padx=10)

        fname_label = customtkinter.CTkLabel(data_frame, text="Name:")
        fname_label.grid(row=0, column=0, padx=10, pady=10)
        fname_entry = customtkinter.CTkEntry(data_frame)
        fname_entry.grid(row=0, column=1, padx=10, pady=10)

        lname_label = customtkinter.CTkLabel(data_frame, text="Nachname:")
        lname_label.grid(row=0, column=2, padx=10, pady=10)
        lname_entry = customtkinter.CTkEntry(data_frame)
        lname_entry.grid(row=0, column=3, padx=10, pady=10)

        company_name_label = customtkinter.CTkLabel(data_frame, text="Firmenname:")
        company_name_label.grid(row=0, column=4, padx=10, pady=10)
        company_name_entry = customtkinter.CTkEntry(data_frame)
        company_name_entry.grid(row=0, column=5, padx=10, pady=10)

        adress_label = customtkinter.CTkLabel(data_frame, text="Adresse:")
        adress_label.grid(row=1, column=0, padx=10, pady=10)
        adress_entry = customtkinter.CTkEntry(data_frame)
        adress_entry.grid(row=1, column=1, padx=10, pady=10)

        zip_code_label = customtkinter.CTkLabel(data_frame, text="Postleitzahl:")
        zip_code_label.grid(row=1, column=2, padx=10, pady=10)
        zip_code_entry = customtkinter.CTkEntry(data_frame)
        zip_code_entry.grid(row=1, column=3, padx=10, pady=10)

        ort_label = customtkinter.CTkLabel(data_frame, text="Ort:")
        ort_label.grid(row=1, column=4, padx=10, pady=10)
        ort_entry = customtkinter.CTkEntry(data_frame)
        ort_entry.grid(row=1, column=5, padx=10, pady=10)

        def is_number():
            try:
                float(zip_code_entry.get())
                return True
            except:
                return False

        def is_string():
            try:
                if fname_entry.get().isdigit():
                    raise NameError
                else:
                    return True
            except:
                return False

        def select_record(e):

            fname_entry.delete(0, "end")
            lname_entry.delete(0, "end")
            company_name_entry.delete(0, "end")
            adress_entry.delete(0, "end")
            zip_code_entry.delete(0, "end")
            ort_entry.delete(0, "end")

            selected = my_tree.focus()
            if selected != "":
                values = my_tree.item(selected, "values")
                fname_entry.insert(0, values[1])
                lname_entry.insert(0, values[2])
                company_name_entry.insert(0, values[3])
                adress_entry.insert(0, values[4])
                zip_code_entry.insert(0, values[5])
                ort_entry.insert(0, values[6])




        def clear_boxes():
            fname_entry.delete(0, "end")
            lname_entry.delete(0, "end")
            company_name_entry.delete(0, "end")
            adress_entry.delete(0, "end")
            zip_code_entry.delete(0, "end")
            ort_entry.delete(0, "end")

            for i in my_tree.selection():
                my_tree.selection_remove(i)



        def delete_record():
            selected = my_tree.focus()
            if selected != "":
                values = my_tree.item(selected, "values")
                my_tree.delete(selected)

                connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM customer_data WHERE oid=?", (values[7],))
                connection.commit()
                clear_boxes()
                tree_frame.update()


        def add_product():
            if is_string():
                if is_number():
                    connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
                    cursor = connection.cursor()
                    cursor.execute(
                        "CREATE TABLE IF NOT EXISTS customer_data (id integer primary key autoincrement, name text, lastname text, company_name text, adress text, zip_code integer, ort text)")
                    connection.commit()

                    cursor.execute("INSERT INTO customer_data VALUES(NULL,?,?,?,?,?,?)",
                                   [
                                       fname_entry.get(),
                                       lname_entry.get(),
                                       company_name_entry.get(),
                                       adress_entry.get(),
                                       zip_code_entry.get(),
                                       ort_entry.get()
                                   ]
                                   )
                    connection.commit()
                    connection.close()
                    showinfo("info", "Erfolgreich neuen Kunden erstellt!")
                    clear_boxes()
                    root.destroy()
                    self.customer_window()
                else:
                    showinfo("info", "Bitte als Preis eine Nummer eingeben!")
            else:
                showinfo("info", "Bitte keine Nummer als Beschreibung eingeben!")

        # ----------------------------------------------------------------------------------------------------------------

        def update_record():
            if is_string():
                if is_number():
                    selected = my_tree.focus()
                    if selected != "":
                        values = my_tree.item(selected, "values")
                        my_tree.delete(selected)

                        connection = sqlite3.connect(
                            "C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
                        cursor = connection.cursor()
                        cursor.execute(
                            "UPDATE customer_data SET  name=?, lastname=?, company_name=?, adress=?, zip_code=?, ort=? WHERE oid=?",
                            [
                                fname_entry.get(),
                                lname_entry.get(),
                                company_name_entry.get(),
                                adress_entry.get(),
                                zip_code_entry.get(),
                                ort_entry.get(),
                                values[7]
                            ]

                        )
                        connection.commit()
                        clear_boxes()
                        root.destroy()
                        self.customer_window()
                else:
                    showinfo("info", "Bitte als Postleitzahl eine Nummer eingeben!")
            else:
                showinfo("info", "Bitte keine Nummer als Name eingeben!")

        def prevent_resize(event):
            if my_tree.identify_region(event.x, event.y) == "separator":
                return "break"

        def choose():
            selected = my_tree.focus()
            if selected != "":
                values = my_tree.item(selected, "values")
                self.selected_customer_id = values[7]
                root.destroy()

        my_tree.bind('<Button-1>', prevent_resize)
        my_tree.bind('<Motion>', prevent_resize)

        button_frame = customtkinter.CTkFrame(root)
        button_frame.pack(fill=tk.BOTH, expand=0, padx=10, pady=10)

        update_button = customtkinter.CTkButton(button_frame, text="Aktualisieren", command=update_record)
        update_button.grid(row=0, column=0, padx=10, pady=20)

        add_button = customtkinter.CTkButton(button_frame, text="Hinzufügen", command=add_product)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        remove_many_button = customtkinter.CTkButton(button_frame, text="Löschen", command=delete_record)
        remove_many_button.grid(row=0, column=2, padx=10, pady=10)

        select_button = customtkinter.CTkButton(button_frame, text="Eingabefelder Löschen", command=clear_boxes)
        select_button.grid(row=0, column=5, padx=10, pady=10)

        select_customer_button = customtkinter.CTkButton(button_frame, text="Diesen Eintrag nehmen", command=choose)
        select_customer_button.grid(row=0, column=5, padx=10, pady=10)

        my_tree.bind("<ButtonRelease-1>", select_record)
        my_tree.pack()

        root.mainloop()

    def selfinfo_window(self):
        root = customtkinter.CTkToplevel(self)
        root.title("Persönliche Daten")

        def center_window(size, window):
            window_width = size[
                0]  # Fetches the width you gave as arg. Alternatively window.winfo_width can be used if width is not to be fixed by you.
            window_height = size[
                1]  # Fetches the height you gave as arg. Alternatively window.winfo_height can be used if height is not to be fixed by you.
            window_x = int((window.winfo_screenwidth() / 2) - (
                    window_width / 2))  # Calculates the x for the window to be in the centre
            window_y = int((window.winfo_screenheight() / 2) - (
                    window_height / 2))  # Calculates the y for the window to be in the centre

            window_geometry = str(window_width) + 'x' + str(window_height) + '+' + str(window_x) + '+' + str(
                window_y)  # Creates a geometric string argument
            window.geometry(window_geometry)  # Sets the geometry accordingly.
            return

        root.geometry(center_window((1080, 800), root))
        root.resizable(False, False)

        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
        cursor = connection.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS self_info (id integer primary key autoincrement, firstname text,
                                                     lastname text, company_name text, address text,
                                                     phone_number integer, email text, website text, zip_code integer, 
                                                     ort text, bank text, bic text, iban text)""")
        connection.commit()

        cursor.execute("SELECT * FROM self_info")
        data = cursor.fetchall()

        style = ttk.Style(root)



        style.theme_use("default")
        style.configure("Treeview", background="#2A2D2E",
                              foreground="white", fieldbackground="#2A2D2E")
        style.configure("Treeview.Heading", background="black", foreground="white")



        style.map("Treeview",
                  background=[("selected", "#1F6AA5")]
                  )

        tree_frame = customtkinter.CTkFrame(root)
        tree_frame.pack(fill=tk.BOTH, expand=0, padx=10, pady=30, ipady=10, ipadx=10)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        if len(data) <= 20 and len(data) >= 4:
            height_treeview = len(data)
        elif len(data) <= 4:
            height_treeview = 4
        else:
            height_treeview = 20
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height=height_treeview,
                               selectmode="extended")

        tree_scroll.config(command=my_tree.yview)

        my_tree["columns"] = (
            "Nr.", "Name", "Nachname", "Firmenname", "Adresse", "Zip", "Ort", "ID", "Tel", "Email", "Web", "Bank",
            "BIC", "IBAN")
        my_tree["show"] = 'headings'

        my_tree.column("#0", width=0, minwidth=0, stretch=NO)
        my_tree.column("Nr.", width=40, minwidth=40, stretch=NO)
        my_tree.column("Name", width=140, minwidth=140, stretch=NO)
        my_tree.column("Nachname", width=140, minwidth=140, stretch=NO)
        my_tree.column("Firmenname", width=180, minwidth=180, stretch=NO)
        my_tree.column("Adresse", width=140, minwidth=140, stretch=NO)
        my_tree.column("Zip", width=80, minwidth=80, stretch=NO)
        my_tree.column("Ort", width=120, minwidth=120, stretch=NO)
        my_tree.column("ID", width=0, minwidth=0, stretch=NO)
        my_tree.column("Tel", width=0, minwidth=0, stretch=NO)
        my_tree.column("Email", width=0, minwidth=0, stretch=NO)
        my_tree.column("Web", width=0, minwidth=0, stretch=NO)
        my_tree.column("Bank", width=0, minwidth=0, stretch=NO)
        my_tree.column("BIC", width=0, minwidth=0, stretch=NO)
        my_tree.column("IBAN", width=0, minwidth=0, stretch=NO)

        my_tree.heading("#0", text="")
        my_tree.heading("Nr.", text="Nr.")
        my_tree.heading("Name", text="Name")
        my_tree.heading("Nachname", text="Nachname")
        my_tree.heading("Firmenname", text="Firmenname")
        my_tree.heading("Adresse", text="Adresse")
        my_tree.heading("Zip", text="Postleitzahl")
        my_tree.heading("Ort", text="Ort")
        my_tree.heading("ID", text="")
        my_tree.heading("Tel", text="")
        my_tree.heading("Email", text="")
        my_tree.heading("Web", text="")
        my_tree.heading("Bank", text="")
        my_tree.heading("BIC", text="")
        my_tree.heading("IBAN", text="")

        for i in range(len(data)):
            my_tree.insert(parent="", index="end", iid=str(i), text="", values=(
                i + 1, data[i][1], data[i][2], data[i][3], data[i][4], data[i][8], data[i][9], data[i][0], data[i][5],
                data[i][6], data[i][7], data[i][10], data[i][11], data[i][12]))

        data_frame = customtkinter.CTkFrame(root)
        data_frame.pack(fill="x", expand=0, padx=20)

        fname_label = customtkinter.CTkLabel(data_frame, text="Name:")
        fname_label.grid(row=0, column=0, padx=10, pady=10)
        fname_entry = customtkinter.CTkEntry(data_frame)
        fname_entry.grid(row=0, column=1, padx=10, pady=10)

        lname_label = customtkinter.CTkLabel(data_frame, text="Nachname:")
        lname_label.grid(row=0, column=2, padx=10, pady=10)
        lname_entry = customtkinter.CTkEntry(data_frame)
        lname_entry.grid(row=0, column=3, padx=10, pady=10)

        company_name_label = customtkinter.CTkLabel(data_frame, text="Firmenname:")
        company_name_label.grid(row=0, column=4, padx=10, pady=10)
        company_name_entry = customtkinter.CTkEntry(data_frame)
        company_name_entry.grid(row=0, column=5, padx=10, pady=10)

        adress_label = customtkinter.CTkLabel(data_frame, text="Adresse:")
        adress_label.grid(row=1, column=0, padx=10, pady=10)
        adress_entry = customtkinter.CTkEntry(data_frame)
        adress_entry.grid(row=1, column=1, padx=10, pady=10)

        tel_label = customtkinter.CTkLabel(data_frame, text="Tel:")
        tel_label.grid(row=1, column=2, padx=10, pady=10)
        tel_entry = customtkinter.CTkEntry(data_frame)
        tel_entry.grid(row=1, column=3, padx=10, pady=10)

        email_label = customtkinter.CTkLabel(data_frame, text="Email:")
        email_label.grid(row=1, column=4, padx=10, pady=10)
        email_entry = customtkinter.CTkEntry(data_frame)
        email_entry.grid(row=1, column=5, padx=10, pady=10)

        web_label = customtkinter.CTkLabel(data_frame, text="Web:")
        web_label.grid(row=2, column=0, padx=10, pady=10)
        web_entry = customtkinter.CTkEntry(data_frame)
        web_entry.grid(row=2, column=1, padx=10, pady=10)

        zip_code_label = customtkinter.CTkLabel(data_frame, text="Postleitzahl:")
        zip_code_label.grid(row=2, column=2, padx=10, pady=10)
        zip_code_entry = customtkinter.CTkEntry(data_frame)
        zip_code_entry.grid(row=2, column=3, padx=10, pady=10)

        ort_label = customtkinter.CTkLabel(data_frame, text="Ort:")
        ort_label.grid(row=2, column=4, padx=10, pady=10)
        ort_entry = customtkinter.CTkEntry(data_frame)
        ort_entry.grid(row=2, column=5, padx=10, pady=10)

        bank_label = customtkinter.CTkLabel(data_frame, text="Bank:")
        bank_label.grid(row=3, column=0, padx=10, pady=10)
        bank_entry = customtkinter.CTkEntry(data_frame)
        bank_entry.grid(row=3, column=1, padx=10, pady=10)

        bic_label = customtkinter.CTkLabel(data_frame, text="BIC:")
        bic_label.grid(row=3, column=2, padx=10, pady=10)
        bic_entry = customtkinter.CTkEntry(data_frame)
        bic_entry.grid(row=3, column=3, padx=10, pady=10)

        iban_label = customtkinter.CTkLabel(data_frame, text="IBAN:")
        iban_label.grid(row=3, column=4, padx=10, pady=10)
        iban_entry = customtkinter.CTkEntry(data_frame)
        iban_entry.grid(row=3, column=5, padx=10, pady=10)

        def is_number():
            try:
                float(zip_code_entry.get())
                return True
            except:
                return False

        def is_string():
            try:
                if fname_entry.get().isdigit():
                    raise NameError
                else:
                    return True
            except:
                return False

        def select_record(e):
            fname_entry.delete(0, "end")
            lname_entry.delete(0, "end")
            company_name_entry.delete(0, "end")
            adress_entry.delete(0, "end")
            tel_entry.delete(0, "end")
            email_entry.delete(0, "end")
            web_entry.delete(0, "end")
            zip_code_entry.delete(0, "end")
            ort_entry.delete(0, "end")
            bank_entry.delete(0, "end")
            bic_entry.delete(0, "end")
            iban_entry.delete(0, "end")

            selected = my_tree.focus()
            if selected != "":
                values = my_tree.item(selected, "values")

                fname_entry.insert(0, values[1])
                lname_entry.insert(0, values[2])
                company_name_entry.insert(0, values[3])
                adress_entry.insert(0, values[4])
                tel_entry.insert(0, values[8])
                email_entry.insert(0, values[9])
                web_entry.insert(0, values[10])
                zip_code_entry.insert(0, values[5])
                ort_entry.insert(0, values[6])
                bank_entry.insert(0, values[11])
                bic_entry.insert(0, values[12])
                iban_entry.insert(0, values[13])

        def clear_boxes():
            fname_entry.delete(0, "end")
            lname_entry.delete(0, "end")
            company_name_entry.delete(0, "end")
            adress_entry.delete(0, "end")
            tel_entry.delete(0, "end")
            email_entry.delete(0, "end")
            web_entry.delete(0, "end")
            zip_code_entry.delete(0, "end")
            ort_entry.delete(0, "end")
            bank_entry.delete(0, "end")
            bic_entry.delete(0, "end")
            iban_entry.delete(0, "end")

        for i in my_tree.selection():
            my_tree.selection_remove(i)

        def delete_record():
            selected = my_tree.focus()
            if selected != "":
                values = my_tree.item(selected, "values")
                my_tree.delete(selected)

                connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM customer_data WHERE oid=?", (values[7],))
                connection.commit()
                clear_boxes()
                tree_frame.update()

        def add_product():
            if is_string():
                if is_number():
                    connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
                    cursor = connection.cursor()
                    cursor.execute(
                        "CREATE TABLE IF NOT EXISTS customer_data (id integer primary key autoincrement, name text, lastname text, company_name text, adress text, zip_code integer, ort text)")
                    connection.commit()

                    cursor.execute("INSERT INTO self_info VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?)",
                                   [
                                       fname_entry.get(),
                                       lname_entry.get(),
                                       company_name_entry.get(),
                                       adress_entry.get(),
                                       tel_entry.get(),
                                       email_entry.get(),
                                       web_entry.get(),
                                       zip_code_entry.get(),
                                       ort_entry.get(),
                                       bank_entry.get(),
                                       bic_entry.get(),
                                       iban_entry.get()
                                   ]
                                   )
                    connection.commit()
                    connection.close()
                    showinfo("info", "Erfolgreich neue Persönliche Daten angelegt!")
                    clear_boxes()
                    root.destroy()
                    #self.self_info()
                else:
                    showinfo("info", "Bitte nur Nummern als Postleitzahl eingeben!")
            else:
                showinfo("info", "Bitte keine Nummer als Beschreibung eingeben!")

        # ----------------------------------------------------------------------------------------------------------------

        def update_record():
            if is_string():
                if is_number():
                    selected = my_tree.focus()
                    if selected != "":
                        values = my_tree.item(selected, "values")
                        my_tree.delete(selected)

                        connection = sqlite3.connect(
                            "C:\\Users\\ffff\\PycharmProjects\\InvoiceMaker\\customer_data.db")
                        cursor = connection.cursor()
                        cursor.execute(
                            "UPDATE self_info SET  firstname=?, lastname=?, company_name=?, address=?, phone_number=?, email=?,website=?, zip_code=?, ort=?, bank=?, bic=?, iban=? WHERE oid=?",
                            [
                                fname_entry.get(),
                                lname_entry.get(),
                                company_name_entry.get(),
                                adress_entry.get(),
                                tel_entry.get(),
                                email_entry.get(),
                                web_entry.get(),
                                zip_code_entry.get(),
                                ort_entry.get(),
                                bank_entry.get(),
                                bic_entry.get(),
                                iban_entry.get(),
                                values[7]
                            ]

                        )
                        connection.commit()
                        clear_boxes()
                        root.destroy()
                        self.selfinfo_window()
                else:
                    showinfo("info", "Bitte als Postleitzahl eine Nummer eingeben!")
            else:
                showinfo("info", "Bitte keine Nummer als Name eingeben!")

        def prevent_resize(event):
            if my_tree.identify_region(event.x, event.y) == "separator":
                return "break"

        def choose():
            selected = my_tree.focus()
            if selected != "":
                values = my_tree.item(selected, "values")
                self.selected_id_self_info = values[7]
                root.destroy()

        my_tree.bind('<Button-1>', prevent_resize)
        my_tree.bind('<Motion>', prevent_resize)

        button_frame = customtkinter.CTkFrame(root)
        button_frame.pack(fill="x", expand=0, padx=20)

        update_button = customtkinter.CTkButton(button_frame, text="Aktualisieren", command=update_record)
        update_button.grid(row=0, column=0, padx=10, pady=10)

        add_button = customtkinter.CTkButton(button_frame, text="Hinzufügen", command=add_product)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        remove_many_button = customtkinter.CTkButton(button_frame, text="Löschen", command=delete_record)
        remove_many_button.grid(row=0, column=2, padx=10, pady=10)

        select_button = customtkinter.CTkButton(button_frame, text="Eingabefelder Löschen", command=clear_boxes)
        select_button.grid(row=0, column=3, padx=10, pady=10)

        selected_button = customtkinter.CTkButton(button_frame, text="Diesen Eintrag nehmen", command=choose)
        selected_button.grid(row=0, column=4, padx=10, pady=10)

        my_tree.bind("<ButtonRelease-1>", select_record)
        my_tree.pack()

        root.mainloop()





app = MainWindow()
app.mainloop()

