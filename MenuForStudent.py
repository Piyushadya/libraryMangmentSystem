from AvailableBooks import *
from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from ViewIssuedbooks import *
import DatabaseConnectivity
def menuForStudent(memId):
    global cur

    # Add your own database name and password here to reflect in the code
    # Add your own database name and password here to reflect in the code
    con=DatabaseConnectivity()
    cur = con.cursor()

    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ADD8E6")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Menu For Student", bg='black', fg='white',
                         font=('Courier', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Available Books ", bg='black', fg='white',command=AvailableBooks,font=('Courier', 15))
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="View Issued Books ", bg='black', fg='white',command=lambda: ViewIssued(memId),font=('Courier', 15))
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)


    root.mainloop()
