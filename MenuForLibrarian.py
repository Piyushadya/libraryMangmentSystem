from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBookInfo import *
from DeleteBookInfo import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from DatabaseConnectivity import *

# This function will display the menu to the user after successfull login.
def menuForLibrarian():
    global cur

    # It will provide database connectivity
    con=DatabaseConnectivity()
    cur = con.cursor()

    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    # Background color
    Canvas1.config(bg="#00FFFF")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.16)

    # Heading of the MENU Form
    headingLabel = Label(headingFrame1, text="Menu For Librarian", bg='black', fg='white',
                         font=('Courier', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # To add book
    btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBookInfo,font=('Courier', 15))
    btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    # To delete book
    btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete,font=('Courier', 15))
    btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    # To view book
    btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View,font=('Courier', 15))
    btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    # To issue book
    btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook,font=('Courier', 15))
    btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    # To return book
    btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook,font=('Courier', 15))
    btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    # Quit button to destroy the current event
    btn6 = Button(root,text="Quit",bg='black', fg='white', command=root.destroy,font=('Courier', 15))
    btn6.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

    root.mainloop()
