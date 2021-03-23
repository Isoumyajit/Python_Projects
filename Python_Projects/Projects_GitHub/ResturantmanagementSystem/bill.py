from tkinter import *

# classes for billing
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("BillApp")
        bg_color = "#074463"
        title = Label(self.root, text="Soumyajit & Sons Pvt Ltd.", bd=10, relief=GROOVE, bg=bg_color, font=("times new roman",30,"bold") , pady = 2).pack(fill=X)

        #  customer frame
        F1 = LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        Name_label = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        name_text = Entry(F1 , width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        Phone_label = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        phone_txt = Entry(F1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        Email_label = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        eamil_text = Entry(F1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Search", font="arial 10 bold", width=10, bd=7).grid(row=0, column=6, padx=10, pady=5)

#       Products list details
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Items", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F2.place(x=5, y=170, width=320, height=350)

root = Tk()
obj = Bill_App(root)
root.mainloop()
