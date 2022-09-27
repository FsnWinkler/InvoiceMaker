from tkinter import *
import json



def clrd():
    fn.delete(0, END)
    ln.delete(0, END)
    add.delete(0, END)
    zip.delete(0, END)


def newwin():
    newWin = Tk()
    newWin.title("your Data")
    newWin.geometry("500x400")
    f = open("data.json", "r")
    data = json.load(f)

    Label(newWin,
          text=data["name"] +" "+data["lastname"]+" "+data["address"]+" "+data["zipcode"]).pack()
    f.close()
    add_customer = Button(newWin, text="Add Customer", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=new_customer)
    add_customer.pack()

def new_customer():
    add_customer_win = Tk()
    add_customer_win.title("new customer")
    add_customer_win.geometry("500x400")
    frame = Frame(add_customer_win, padx=10, pady=10)
    frame.pack(expand=True)
    Label(
        frame,
        text="Enter your Data",
        font=("Times", "24", "bold")
    ).grid(row=0, columnspan=3, pady=10)
    Label(
        frame,
        text='First Name',
        font=("Times", "14")
    ).grid(row=1, column=0, pady=5)

    Label(
        frame,
        text='Last Name',
        font=("Times", "14")
    ).grid(row=2, column=0, pady=5)

    Label(
        frame,
        text='Company Name',
        font=("Times", "14")
    ).grid(row=3, column=0, pady=5)

    Label(
        frame,
        text='Zip Code',
        font=("Times", "14")
    ).grid(row=4, column=0, pady=5)

    fn = Entry(frame, width=35)
    ln = Entry(frame, width=35)
    company_name = Entry(frame, width=35)
    zip = Entry(frame, width=35)

    fn.grid(row=1, column=1)
    ln.grid(row=2, column=1)
    company_name.grid(row=3, column=1)
    zip.grid(row=4, column=1)

    def submit():
        with open('customer_data.json', "w", encoding="utf-8") as f:
            customer_information = {'name': fn.get(), 'lastname': ln.get(), 'address': company_name.get(), "zipcode": zip.get()}
            f.write(
                json.dumps(customer_information, indent=0)
            )
        if customer_information != None:
            add_customer_win.destroy()

    reg = Button(frame, text="Register", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=submit)
    reg.grid(row=5, column=1)



def registration():
    def submit():
        with open('data.json', "w", encoding="utf-8") as f:
            my_information = {'name': fn.get(), 'lastname': ln.get(), 'address': add.get(), "zipcode": zip.get()}
            f.write(
                json.dumps(my_information)
            )
        root.destroy()
        newwin()
    root = Tk()
    root.title('registration')
    root.geometry("500x400")
    frame = Frame(root, padx=10, pady=10)
    frame.pack(expand=True)


    Label(
    frame,
    text="Enter your Data",
    font=("Times", "24", "bold")
    ).grid(row=0, columnspan=3, pady=10)
    Label(
    frame,
    text='First Name',
    font=("Times", "14")
    ).grid(row=1, column=0, pady=5)

    Label(
    frame,
    text='Last Name',
    font=("Times", "14")
    ).grid(row=2, column=0, pady=5)

    Label(
    frame,
    text='Address',
    font=("Times", "14")
    ).grid(row=3, column=0, pady=5)

    Label(
    frame,
    text='Zip Code',
    font=("Times", "14")
    ).grid(row=4, column=0, pady=5)


    fn = Entry(frame, width=35)
    ln = Entry(frame, width=35)
    add = Entry(frame, width=35)
    zip = Entry(frame , width=35)




    fn.grid(row=1, column=1)
    ln.grid(row=2, column=1)
    add.grid(row=3, column=1)
    zip.grid(row=4, column=1)

    clr = Button(frame, text="Clear", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=clrd)
    reg = Button(frame, text="Register", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=submit)
    ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: root.destroy())

    clr.grid(row=6, column=0, pady=20)
    reg.grid(row=6, column=1, pady=20)
    ext.grid(row=6, column=2, pady=20)
    root.mainloop()



if __name__ == "__main__":
    registration()

