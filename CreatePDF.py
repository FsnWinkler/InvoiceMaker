import sqlite3
from datetime import date
from fpdf import FPDF
from fpdf.enums import XPos, YPos



class PDF(FPDF):
    def __init__(self, number_rows, self_info_id, product_data_id, company_id, bill_number, product_amount):
        super().__init__()
        self.rows = number_rows
        self.company_id = company_id
        self.bill_number = bill_number
        self.self_info_id = self_info_id
        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT company_name FROM self_info WHERE oid={}".format(self.self_info_id))
        data = cursor.fetchone()
        self.title = data[0]
        self.product_data_id = product_data_id
        self.product_amount = product_amount
        self.add_page()
        self.my_company()
        self.output("test.pdf")

    def header(self):
        self.set_font("helvetica", "B", 20)
        title_w = self.get_string_width(self.title)+6
        doc_w = self.w
        self.set_x((doc_w - title_w)/2)
        self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(20)

    def footer(self):
        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM self_info WHERE oid={}".format(self.self_info_id))
        list = []
        for f in cursor.fetchall():
            list.append(f)

        dict = {"name": list[0][1],
                "lastname": list[0][2],
                "company": list[0][3],
                "address": list[0][4],
                "tel": list[0][5],
                "email": list[0][6],
                "web": list[0][7],
                "zip": list[0][8],
                "ort": list[0][9],
                "bank": list[0][10],
                "bic": list[0][11],
                "iban": list[0][12],
                }
        self.set_xy(40, -23)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, txt=dict["company"])
        self.set_xy(40, -19)
        self.cell(0, 10, txt=dict["name"]+" "+ dict["lastname"])
        self.set_xy(40, -15)
        self.cell(0, 10, txt=dict["address"])
        self.set_xy(40, -11)
        self.cell(0, 10, txt=str(dict["zip"])+ " " + dict["ort"])

        self.set_xy(80, -23)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, txt="Tel.: " +  str(dict["tel"]))
        self.set_xy(80, -19)
        self.cell(0, 10, txt="Email: " + dict["email"])
        self.set_xy(80, -15)
        if list[0][6] != "":
            self.cell(0, 10, txt="Web: " + dict["web"])

        self.set_xy(130, -23)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, txt="Bank: "+ dict["bank"])
        self.set_xy(130, -19)
        self.cell(0, 10, txt="SWIFT/BIC: "+ dict["bic"])
        self.set_xy(130, -15)
        self.cell(0, 10, txt="IBAN: "+ dict["iban"])

        self.set_xy(30, -26)
        self.cell(100, 5, txt="_" * 95)


    def my_company(self):
        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customer_data WHERE oid={}".format(self.company_id))
        data = cursor.fetchone()
        today = date.today()
        current_date = today.strftime("%B %d, %Y")
        border_on= False
        widht_size = 5
        height_size = 100
        self.set_font("helvetica", size=10)
        self.cell(height_size, widht_size, txt=data[3], border=border_on)
        self.cell(height_size, widht_size, txt="Rechnunsnummer:" + " " + self.bill_number, border=border_on, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(height_size, widht_size, txt=data[4] , border=border_on)
        self.cell(height_size, widht_size, txt="Rechnungsdatum:" + " " + current_date, border=border_on, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(height_size, widht_size, txt=str(data[5]) + " " + data[6], border=border_on)
        self.cell(height_size, widht_size, txt="", border=border_on, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_xy(10,100)
        self.set_font("helvetica", size=20)
        self.cell(height_size, widht_size, txt="Rechnung", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font("helvetica", size=10)
        self.cell(200,5,txt="_"*95)
        self.set_font("helvetica", "B", size=10)
        self.set_xy(10,111)
        self.cell(20, 8,txt="Pos.", border=border_on)
        self.set_xy(20,111)
        # self.cell(20, 8, txt="Artkel-Nr.", border=border_on)
        # self.set_xy(40, 111)
        self.cell(80, 8, txt="Produktbezeichnung", border=border_on)
        self.set_xy(90, 111)
        self.cell(20, 8, txt="Menge", border=border_on)
        self.set_xy(110, 111)
        self.cell(20, 8, txt="Einheit", border=border_on)
        self.set_xy(130, 111)
        self.cell(40, 8, txt="Einzelpreis()", border=border_on)
        self.set_xy(155, 111)
        self.cell(20, 8, txt="USt.", border=border_on)
        self.set_xy(170, 111)
        self.cell(30, 8, txt="Summe netto()", border=border_on)
        self.set_xy(10, 116)
        self.set_font("helvetica", size=10)
        self.cell(200, 5, txt="_" * 95)
        connection = sqlite3.connect("C:\\Users\\ffff\\PycharmProjects\\pythonProject1\\customer_data.db")
        cursor = connection.cursor()
        summe = 0
        ust_summe = 0

        def int_to_comma(int):
            return ('%.2f' % int).replace('.', ',')
        for i in range(self.rows):
            cursor.execute("SELECT * FROM product_data WHERE oid={}".format(self.product_data_id[i]))
            data = cursor.fetchall()
            index_rows = [121, 133, 147]
            index_note_rows = [126, 138, 152]

            row_1 = index_rows[i]
            #self.product_amount[i] = [i]
            #POS.
            self.set_font("helvetica", size=10)
            self.set_xy(10, row_1)
            self.cell(20, 8, txt=str(i+1), border=border_on)
            #Artikel-Nr.
            # self.set_xy(20, row_1)
            # self.cell(20, 8, txt="100332", border=border_on)
            #Produktbezeichnung
            self.set_font("helvetica", "B", size=10)
            self.set_xy(20, row_1)
            self.cell(80, 8, txt=data[0][1], border=border_on)
            #Menge
            self.set_font("helvetica", size=10)
            self.set_xy(90, row_1)
            self.cell(20, 8, txt=str(int_to_comma(self.product_amount[i])), border=border_on)
            #Einheit
            self.set_xy(110, row_1)
            self.cell(20, 8, txt=data[0][3], border=border_on)
            #Einzelpreis
            self.set_xy(130, row_1)
            self.cell(40, 8, txt=str(int_to_comma(data[0][4])), border=border_on)
            #USt.
            self.set_xy(155, row_1)
            self.cell(20, 8, txt=data[0][5], border=border_on)
            #Summe
            self.set_xy(170, row_1)
            self.cell(30, 8, txt=str(int_to_comma(data[0][4]*self.product_amount[i])) ,border=border_on)
            summe = data[0][4]*self.product_amount[i]+summe
            ust_summe = ((data[0][4]*self.product_amount[i])/100)*20+ust_summe
            #Notiz
            self.set_xy(20, index_note_rows[i])
            self.cell(80, 8, txt=str(data[0][2]), border=border_on)

        list_of_sum = [128, 134, 140, 142, 147]
        i = 0
        for item in list_of_sum:
            list_of_sum[i] = item +13*(self.rows-1)
            i += 1
        self.set_xy(10, list_of_sum[0])
        self.cell(100, 8, txt="_" * 95)
        self.set_xy(140, list_of_sum[1])
        self.cell(100, 8, txt="Nettobetrag:")
        self.set_xy(140, list_of_sum[2])
        self.cell(100, 8, txt="USt.:")
        self.set_xy(170, list_of_sum[1])
        self.cell(100, 8, txt=str(int_to_comma(summe)))
        self.set_xy(170, list_of_sum[2])
        self.cell(100, 8, txt=str(int_to_comma(ust_summe)))
        self.set_font("helvetica", "B", size=10)
        self.set_xy(140, list_of_sum[3])
        self.cell(100, 8, txt="_" * 30)
        self.set_xy(140, list_of_sum[4])
        self.cell(100, 8, txt="Gesamtbetrag:")
        self.set_xy(170, list_of_sum[4])
        self.cell(100, 8, txt=str(int_to_comma(ust_summe+ summe)))






