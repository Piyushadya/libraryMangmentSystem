from AvailableBooks import *
from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from ViewBooks import *
from ViewIssuedbooks import *
from DatabaseConnectivity import *

# It will display Menu form to the student after successful login
def menuForStudent(memId):
    global cur

    # It will provide database connectivity
    con=DatabaseConnectivity()
    cur = con.cursor()

    # Form sizing
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    #Background color
    Canvas1.config(bg="#ADBDFF")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    #Heading of student menu
    headingLabel = Label(headingFrame1, text="Menu For Student", bg='black', fg='white',
                         font=('Courier', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # If clicked, it will display the available books
    btn1 = Button(root, text="View Available Books ", bg='black', fg='white',command=AvailableBooks,font=('Courier', 15))
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    # If clicked, it will display the books issued to particular user
    btn2 = Button(root, text="View Issued Books ", bg='black', fg='white',command=lambda: ViewIssued(memId),font=('Courier', 15))
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    # Quit button to destroy the current event
    btn3 = Button(root,text="Quit",bg='black', fg='white', command=root.destroy,font=('Courier', 15))
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)


    root.mainloop()
