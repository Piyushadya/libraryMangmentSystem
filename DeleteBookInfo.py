from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from DatabaseConnectivity import *

# It will provide connectivity to the database
con=DatabaseConnectivity()

cur = con.cursor()

# Table names are listed here
issueTable = "books_issued" 
bookTable = "books" 

allBid = [] #List To store all Book IDs

# This function will delete specific book from "bookTable/issueTable" table
def deleteBookInfo():
    
    # Fetch book id from specific table
    bid = bookInfo1.get()

    extractBid = "select bid from " + bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            # Fetching details from specifc table and delete as per the book ID
            deleteSql = "delete from " + bookTable + " where bid = '" + bid + "'"
            deleteIssue = "delete from " + issueTable + " where bid = '" + bid + "'"
            cur.execute(deleteSql)
            con.commit()
            cur.execute(deleteIssue)
            con.commit()
            messagebox.showinfo('Success', "Book Deleted Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please enter the correct book ID")
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    allBid.clear()
    root.destroy()

    bookInfo1.delete(0, END)
    root.destroy()
 
# This will show form to the user, where user can add "BOOK ID", whose details they want to delete
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    #Form sizing
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#75B9BE")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
     
    # Heading of the form 
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Adding book ID 
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=('Courier', 15))
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    # Submit button is added and it will trigger "deleteBookInfo" function
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBookInfo,font=('Courier', 15))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit button is added and it will destroy the current event and return user to previous form
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Courier', 15))
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
