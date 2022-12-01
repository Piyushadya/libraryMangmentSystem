from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk,Image
from DatabaseConnectivity import *

# we create this "bookRegister" function to insert data into database after fetching data from form.
def bookRegister():
#fetching book details from form    
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = clicked.get()
    status = status.lower()
    
#Adding details to the desired table in database
    
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")

    root.destroy()
# we create this "addBook" function to add new book to the inventory.    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,clicked,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    # It will connect to the database 
    con=DatabaseConnectivity()
    cur = con.cursor()

    # Table name where new books data are stored
    bookTable = "books"

    Canvas1 = Canvas(root)
    
    # Background color is provided here
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
    
    # Providing heading of the Page
    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # ID of the book
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=('Courier', 15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title of the book
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white',font=('Courier', 15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Author of the Book
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white',font=('Courier', 15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Status of the book in the form of dropdown
    lb4 = Label(labelFrame,text="Status : ", bg='black', fg='white',font=('Courier', 15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
    
    #Dropdown is added here, providing two options: Available/Issued
    options = [
    "Available",
    "Issued"
    ]
    clicked = StringVar(root)
    clicked.set( "Available" )
    drop = OptionMenu( root , clicked , *options )
    drop.pack()  
     
    drop.place(relx=0.34,rely=0.66, relwidth=0.50, relheight=0.03)
  
        
    #Creating a submit button that will insert the data to database by triggering bookRegister function
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister,font=('Courier', 15))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
  
    #Creating a quit button that will destroy the event
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Courier', 15))
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
