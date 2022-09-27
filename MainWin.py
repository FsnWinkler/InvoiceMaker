import tkinter
from tkinter.messagebox import showinfo

import customtkinter
import sqlite3


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Easy Rechnungserstellung")
        self.create_mainwindow()

    def create_mainwindow(self):
        self.selected_customer_id =2
        self.selected_id_self_info = 2
        self.selected_product_id = [29, 30]
        def show_customer():
            try:
                connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM customer_data WHERE oid=?", (self.selected_customer_id, ))
                data = cursor.fetchone()
                print(data)
                show_data = str(data[1] + " " + data[2] + " " + data[3])
                self.customer_label1.set_text(show_data)
                print(data[1] + " " + data[2] + " " + data[3])
            except:
                showinfo("Info", "Bitte wähle einen Kunden aus")

        def show_self_info():

            connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM self_info WHERE oid=?", (self.selected_id_self_info, ))
            data = cursor.fetchone()
            print(data)
            show_data = str(data[1] + " " + data[2] + " " + data[3] + " " + data[4] + " " + str(data[8]) + " " + data[9])
            self.self_info_label1.set_text(show_data)
            print(data[1] + " " + data[2] + " " + data[3])

        def show_product():

            connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
            cursor = connection.cursor()
            for i in range(len(self.selected_product_id)):
                cursor.execute("SELECT * FROM product_data WHERE oid=?", (self.selected_product_id[i], ))
                data = cursor.fetchone()
                print(data)
                show_data = str(data[1] + " " + data[2] + " " + data[3] + " " + str(data[4]) + " " + data[5] + " " + data[6])
                if i+1 == 1:
                    self.product_label1.set_text(show_data)
                if i+1 == 2:
                    self.product_label2.set_text(show_data)
                if i+1 == 3:
                    self.product_label3.set_text(show_data)
                if i+1 == 4:
                    self.product_label4.set_text(show_data)



                print(data[1] + " " + data[2] + " " + data[3])



        #head
        self.header_label = customtkinter.CTkLabel(self, text="Rechnungserstellungs Programm")
        self.header_label.grid(row=0, column=0)
        #dataframe/mainframe
        self.frame = customtkinter.CTkFrame(self, height=400, width=200, border_width=0)
        self.frame.grid(sticky='nsew',row=1, column=0, padx=20, pady=50 , ipadx=300)

        # self.frame.columnconfigure(0, weight=1)
        # self.columnconfigure(2, weight=1)

        #buttonframe
        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(sticky='nsew', row= 10, column=0, padx=20 , ipadx=300 , pady=25 )


        #customer data
        self.customer_label = customtkinter.CTkLabel(self.frame, text="Kundendaten: ", borderwidth=0)
        self.customer_label.grid(row=0, column=0, pady=0, sticky='w')
        self.customer_label1 = customtkinter.CTkLabel(self.frame, text="")
        self.customer_label1.grid(row=0, column=1, pady=10)

        #self info data
        self.self_info_label = customtkinter.CTkLabel(self.frame, text="Eigene Daten: ", borderwidth=0)
        self.self_info_label.grid(row=1, column=0, pady=0, sticky='w')
        self.self_info_label1 = customtkinter.CTkLabel(self.frame, text="")
        self.self_info_label1.grid(row=1, column=1, pady=10,columnspan=50)

        #product data
        self.product_label = customtkinter.CTkLabel(self.frame, text="Produkte: ")
        self.product_label.grid(row=2, column=0, pady=0 , sticky='w')
        self.product_label1 = customtkinter.CTkLabel(self.frame, text="")
        self.product_label1.grid(row=2, column=1, pady=10, columnspan=22)

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

        self.button = customtkinter.CTkButton(self.button_frame, text="Kunden Anzeigen", command=show_customer)
        self.button.grid(row=0, column=0, padx=10, pady=10)
        self.button1 = customtkinter.CTkButton(self.button_frame, text="Eigene Daten Anzeigen", command=show_self_info)
        self.button1.grid(row=0, column=1, padx=10, pady=10)
        self.button2 = customtkinter.CTkButton(self.button_frame, text="Produkte Anzeigen", command=show_product)
        self.button2.grid(row=0, column=2, padx=10, pady=10)


    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x200")

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)






app = MainWindow()
app.mainloop()

