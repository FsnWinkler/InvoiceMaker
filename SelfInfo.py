import os
import tkinter as tk
import json
from tkinter import ttk
import sqlite3
from os import path
from tkinter.messagebox import showinfo
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkPDFViewer import tkPDFViewer as pdf
import pdf_maker
import MainWin


def main():
    MainWindow("Rechnungs-Erstellungs-Software", "1000x700", True)





class MainWindow:
    selected_id_self_info = 0
    selected_customer_id = 0
    selected_product_id = []
    product_count = 0
    def __init__(self, title, geometry, active_menu):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        if active_menu:
            self.createMenu()
        #self.createMainWindowContent()
        self.root.mainloop()
        MainWin()




    def createMainWindowContent(self):

        # def view_pdf():
        #     root = Tk()
        #     root.geometry("1000x800")
        #     variable1 = pdf.ShowPdf()
        #     # Add your pdf location and width and height.
        #     variable2 = variable1.pdf_view(root, pdf_location=r"C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\test.pdf", width=50, height=100)
        #     variable2.pack()
        #
        #     root.mainloop()
        #
        # pdfViewButton = Button(self.root, text="view pdf", command=view_pdf)
        # pdfViewButton.pack()

        def create_pdf():
            pdf_maker.PDF(self.product_count, "GMBH", self.selected_id_self_info, self.selected_product_id)



        def selcted():
            print("id self= " + str(self.selected_id_self_info))
            print("id customer= " + str(self.selected_customer_id))
            print("id product= " + str(self.selected_product_id))
            print("product count= " + str(self.product_count))

        def show_customer():
            try:
                connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM customer_data WHERE oid=?", (self.selected_customer_id, ))
                data = cursor.fetchone()
                customer_label1["text"] = data[1]
                customer_label2["text"] = data[2]
                customer_label3["text"] = data[3]
            except:
                showinfo("Info", "Bitte wähle einen Kunden aus")

        titleFrame = Frame(self.root)
        titleFrame.pack()

        mainFrame = Frame(self.root)
        mainFrame.place(x=10, y= 100)

        buttonFrame = LabelFrame(self.root)
        buttonFrame.pack(side=BOTTOM, padx=5, pady=5, fill=X)

        buttonFrame2 = LabelFrame(self.root)
        buttonFrame2.pack(side=BOTTOM, padx=5, pady=5, fill=X)




        #title
        createPdf_label = Label(titleFrame, text="PDF Rechnung erstellen", font="Helvetica 20")
        createPdf_label.grid(column=0, row=0)

        #Kunden Label
        customer_label = Label(mainFrame, text="Kunde:", font="Helvetica 13")
        customer_label.grid(column=0, row=0, sticky="W", padx=10)

        customer_label1 = Label(mainFrame, text="", font="Helvetica 11")
        customer_label1.grid(column=1, row=0, sticky="W", padx=5)

        customer_label2 = Label(mainFrame, text="", font="Helvetica 11")
        customer_label2.grid(column=2, row=0, sticky="W", padx=5)

        customer_label3 = Label(mainFrame, text="", font="Helvetica 11")
        customer_label3.grid(column=3, row=0, sticky="W", padx=5)



        show_customer_button = Button(buttonFrame2, text="Kunden Anzeigen", command=show_customer)
        show_customer_button.grid(column=0, row=0, padx=10, pady=10)

        show_customer_button1 = Button(buttonFrame2, text="show selected ids", command=selcted)
        show_customer_button1.grid(column=1, row=0, padx=10, pady=10)











        createPdf_button = Button(buttonFrame, text="+", command=create_pdf)
        createPdf_button.grid(column=0, row=0, padx=10, pady=10)







        #PDF(2, "hey", 1, [29,30])


        self_info_id = 0
        customer_id = 0
        product_id = []

        self_info_button = Button(buttonFrame, text="self info", command=self.selfinfo_window)
        self_info_button.grid(column=1, row=0, padx=10, pady=10)
        customer_button = Button(buttonFrame, text="customer", command=self.customer_window)
        customer_button.grid(column=2, row=0, padx=10, pady=10)
        product_button = Button(buttonFrame, text="product", command=self.product_window)
        product_button.grid(column=3, row=0, padx=10, pady=10)




    def createMenu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Eigene Daten", command=self.selfinfo_window)
        file_menu.add_command(label="Kundenliste", command=self.customer_window)
        file_menu.add_command(label="Neues Produkt", command=self.product_window)
        menubar.add_cascade(label="File", menu=file_menu)

    def db_connection(self, name):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(THIS_FOLDER, name)
        connection = sqlite3.connect(db_path)
        return connection

    def popup_showinfo(self, win_name, win_message):
        showinfo(win_name, win_message)

    def product_window(self):
        root = Tk()
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

        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM product_data")
        data = cursor.fetchall()

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#BDBDBD",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white"
                        )

        style.map("Treeview",
                  background=[("selected", "#347083")]
                  )

        tree_frame = Frame(root)
        tree_frame.pack(fill="x", anchor="w", expand=0, padx=20, pady=40)

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

        my_tree.tag_configure("oddrow", background="white")
        my_tree.tag_configure("evenrow", background="white")

        data_frame = LabelFrame(root, text="Record")
        data_frame.pack(fill="x", expand=0, padx=20)

        description_label = Label(data_frame, text="Beschreibung:")
        description_label.grid(row=0, column=0, padx=10, pady=10)
        description_entry = Entry(data_frame)
        description_entry.grid(row=0, column=1, padx=10, pady=10)

        note_label = Label(data_frame, text="Notiz:")
        note_label.grid(row=0, column=2, padx=10, pady=10)
        note_entry = Entry(data_frame)
        note_entry.grid(row=0, column=3, padx=10, pady=10)

        unit_label = Label(data_frame, text="Einheit:")
        unit_label.grid(row=0, column=4, padx=10, pady=10)
        options_unit = ["h", "stk.", "cm", "kg", "km", "m"]
        unit_entry = ttk.Combobox(data_frame, values=options_unit, width=18)
        unit_entry.set("h")
        unit_entry.config(state="readonly")
        unit_entry.grid(row=0, column=5, padx=10, pady=10)

        price_label = Label(data_frame, text="Preis:")
        price_label.grid(row=1, column=0, padx=10, pady=10)
        price_entry = Entry(data_frame)
        price_entry.grid(row=1, column=1, padx=10, pady=10)

        ust_label = Label(data_frame, text="Ust.:")
        ust_label.grid(row=1, column=2, padx=10, pady=10)
        options_ust = ["20%", "18%", "16%"]
        ust_entry = ttk.Combobox(data_frame, values=options_ust, width=18)
        ust_entry.set("20%")
        ust_entry.config(state="readonly")
        ust_entry.grid(row=1, column=3, padx=10, pady=10)

        ust_entry_apply = Label(data_frame, text="Preis basierend auf:")
        ust_entry_apply.grid(row=1, column=4, padx=10, pady=10)
        options_ust = ["Preis exkl. USt.", "Preis inkl. USt.", ]
        ust_entry_apply = ttk.Combobox(data_frame, values=options_ust, width=18)
        ust_entry_apply.set("Preis exkl. USt.")
        ust_entry_apply.config(state="readonly")
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

                connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM product_data WHERE oid=?", (values[8],))
                connection.commit()
                clear_boxes()
                tree_frame.update()

        def add_product():
            if is_string():
                if is_number():
                    connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
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
                    product_window()
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
                            "C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
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
                        product_window()
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

        button_frame = LabelFrame(root, text="Commands")
        button_frame.pack(fill="x", expand=0, padx=20)

        update_button = Button(button_frame, text="Aktualisieren", command=update_record)
        update_button.grid(row=0, column=0, padx=10, pady=10)

        add_button = Button(button_frame, text="Hinzufügen", command=add_product)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        remove_many_button = Button(button_frame, text="Löschen", command=delete_record)
        remove_many_button.grid(row=0, column=2, padx=10, pady=10)

        select_button = Button(button_frame, text="Eingabefelder Löschen", command=clear_boxes)
        select_button.grid(row=0, column=5, padx=10, pady=10)

        select_product_button = Button(button_frame, text="Diesen Eintrag nehmen", command=choose)
        select_product_button.grid(row=0, column=5, padx=10, pady=10)


        my_tree.bind("<ButtonRelease-1>", select_record)
        my_tree.pack()

        root.mainloop()

    def customer_window(self):
        root = Tk()
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

        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customer_data")
        data = cursor.fetchall()

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#BDBDBD",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white"
                        )

        style.map("Treeview",
                  background=[("selected", "#347083")]
                  )

        tree_frame = Frame(root)
        tree_frame.pack(fill="x", anchor="w", expand=0, padx=20, pady=40)

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


        data_frame = LabelFrame(root, text="Record")
        data_frame.pack(fill="x", expand=0, padx=20)

        fname_label = Label(data_frame, text="Name:")
        fname_label.grid(row=0, column=0, padx=10, pady=10)
        fname_entry = Entry(data_frame)
        fname_entry.grid(row=0, column=1, padx=10, pady=10)

        lname_label = Label(data_frame, text="Nachname:")
        lname_label.grid(row=0, column=2, padx=10, pady=10)
        lname_entry = Entry(data_frame)
        lname_entry.grid(row=0, column=3, padx=10, pady=10)

        company_name_label = Label(data_frame, text="Firmenname:")
        company_name_label.grid(row=0, column=4, padx=10, pady=10)
        company_name_entry = Entry(data_frame)
        company_name_entry.grid(row=0, column=5, padx=10, pady=10)

        adress_label = Label(data_frame, text="Adresse:")
        adress_label.grid(row=1, column=0, padx=10, pady=10)
        adress_entry = Entry(data_frame)
        adress_entry.grid(row=1, column=1, padx=10, pady=10)

        zip_code_label = Label(data_frame, text="Postleitzahl:")
        zip_code_label.grid(row=1, column=2, padx=10, pady=10)
        zip_code_entry = Entry(data_frame)
        zip_code_entry.grid(row=1, column=3, padx=10, pady=10)

        ort_label = Label(data_frame, text="Ort:")
        ort_label.grid(row=1, column=4, padx=10, pady=10)
        ort_entry = Entry(data_frame)
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

                connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM customer_data WHERE oid=?", (values[7],))
                connection.commit()
                clear_boxes()
                tree_frame.update()


        def add_product():
            if is_string():
                if is_number():
                    connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
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
                            "C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
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

        button_frame = LabelFrame(root, text="Commands")
        button_frame.pack(fill="x", expand=0, padx=20)

        update_button = Button(button_frame, text="Aktualisieren", command=update_record)
        update_button.grid(row=0, column=0, padx=10, pady=10)

        add_button = Button(button_frame, text="Hinzufügen", command=add_product)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        remove_many_button = Button(button_frame, text="Löschen", command=delete_record)
        remove_many_button.grid(row=0, column=2, padx=10, pady=10)

        select_button = Button(button_frame, text="Eingabefelder Löschen", command=clear_boxes)
        select_button.grid(row=0, column=5, padx=10, pady=10)

        select_customer_button = Button(button_frame, text="Diesen Eintrag nehmen", command=choose)
        select_customer_button.grid(row=0, column=5, padx=10, pady=10)

        my_tree.bind("<ButtonRelease-1>", select_record)
        my_tree.pack()

        root.mainloop()



    def selfinfo_window(self):
        root = Tk()
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

        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
        cursor = connection.cursor()


        cursor.execute(
            """CREATE TABLE IF NOT EXISTS self_info (id integer primary key autoincrement, firstname text,
                                                     lastname text, company_name text, address text,
                                                     phone_number integer, email text, website text, zip_code integer, 
                                                     ort text, bank text, bic text, iban text)""")
        connection.commit()


        cursor.execute("SELECT * FROM self_info")
        data = cursor.fetchall()

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#BDBDBD",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white"
                        )

        style.map("Treeview",
                  background=[("selected", "#347083")]
                  )

        tree_frame = Frame(root)
        tree_frame.pack(fill="x", anchor="w", expand=0, padx=20, pady=40)

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
            "Nr.", "Name", "Nachname", "Firmenname", "Adresse", "Zip", "Ort", "ID", "Tel", "Email", "Web", "Bank", "BIC", "IBAN")
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
                i + 1, data[i][1], data[i][2], data[i][3], data[i][4], data[i][8], data[i][9], data[i][0], data[i][5], data[i][6], data[i][7], data[i][10], data[i][11], data[i][12]))

        data_frame = LabelFrame(root, text="Record")
        data_frame.pack(fill="x", expand=0, padx=20)

        fname_label = Label(data_frame, text="Name:")
        fname_label.grid(row=0, column=0, padx=10, pady=10)
        fname_entry = Entry(data_frame)
        fname_entry.grid(row=0, column=1, padx=10, pady=10)

        lname_label = Label(data_frame, text="Nachname:")
        lname_label.grid(row=0, column=2, padx=10, pady=10)
        lname_entry = Entry(data_frame)
        lname_entry.grid(row=0, column=3, padx=10, pady=10)

        company_name_label = Label(data_frame, text="Firmenname:")
        company_name_label.grid(row=0, column=4, padx=10, pady=10)
        company_name_entry = Entry(data_frame)
        company_name_entry.grid(row=0, column=5, padx=10, pady=10)

        adress_label = Label(data_frame, text="Adresse:")
        adress_label.grid(row=0, column=6, padx=10, pady=10)
        adress_entry = Entry(data_frame, width= 23)
        adress_entry.grid(row=0, column=7, padx=10, pady=10)

        tel_label = Label(data_frame, text="Tel:")
        tel_label.grid(row=1, column=0, padx=10, pady=10)
        tel_entry = Entry(data_frame)
        tel_entry.grid(row=1, column=1, padx=10, pady=10)

        email_label = Label(data_frame, text="Email:")
        email_label.grid(row=1, column=2, padx=10, pady=10)
        email_entry = Entry(data_frame)
        email_entry.grid(row=1, column=3, padx=10, pady=10)

        web_label = Label(data_frame, text="Web:")
        web_label.grid(row=1, column=4, padx=10, pady=10)
        web_entry = Entry(data_frame)
        web_entry.grid(row=1, column=5, padx=10, pady=10)

        zip_code_label = Label(data_frame, text="Postleitzahl:")
        zip_code_label.grid(row=1, column=6, padx=10, pady=10)
        zip_code_entry = Entry(data_frame, width= 23)
        zip_code_entry.grid(row=1, column=7, padx=10, pady=10)

        ort_label = Label(data_frame, text="Ort:")
        ort_label.grid(row=2, column=0, padx=10, pady=10)
        ort_entry = Entry(data_frame)
        ort_entry.grid(row=2, column=1, padx=10, pady=10)

        bank_label = Label(data_frame, text="Bank:")
        bank_label.grid(row=2, column=2, padx=10, pady=10)
        bank_entry = Entry(data_frame)
        bank_entry.grid(row=2, column=3, padx=10, pady=10)

        bic_label = Label(data_frame, text="BIC:")
        bic_label.grid(row=2, column=4, padx=10, pady=10)
        bic_entry = Entry(data_frame)
        bic_entry.grid(row=2, column=5, padx=10, pady=10)

        iban_label = Label(data_frame, text="IBAN:")
        iban_label.grid(row=2, column=6, padx=10, pady=10)
        iban_entry = Entry(data_frame, width= 23)
        iban_entry.grid(row=2, column=7, padx=10, pady=10)

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

                connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM customer_data WHERE oid=?", (values[7],))
                connection.commit()
                clear_boxes()
                tree_frame.update()

        def add_product():
            if is_string():
                if is_number():
                    connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
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
                    self.self_info()
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
                            "C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
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

        button_frame = LabelFrame(root, text="Commands")
        button_frame.pack(fill="x", expand=0, padx=20)

        update_button = Button(button_frame, text="Aktualisieren", command=update_record)
        update_button.grid(row=0, column=0, padx=10, pady=10)

        add_button = Button(button_frame, text="Hinzufügen", command=add_product)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        remove_many_button = Button(button_frame, text="Löschen", command=delete_record)
        remove_many_button.grid(row=0, column=2, padx=10, pady=10)

        select_button = Button(button_frame, text="Eingabefelder Löschen", command=clear_boxes)
        select_button.grid(row=0, column=3, padx=10, pady=10)

        selected_button = Button(button_frame, text="Diesen Eintrag nehmen", command=choose)
        selected_button.grid(row=0, column=4, padx=10, pady=10)

        my_tree.bind("<ButtonRelease-1>", select_record)
        my_tree.pack()

        root.mainloop()


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
        self_info = Tk()
        self_info.title("Eigene Daten")
        self_info.geometry("500x700")
        frame = Frame(self_info)


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
