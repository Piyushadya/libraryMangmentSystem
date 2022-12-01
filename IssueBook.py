from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from DatabaseConnectivity import *

# Table name is added here
issueTable = "books_issued" 
bookTable = "books"
    
# it will list all the Book IDs whose details we want to store
allBid = []

# It will issue Book to the user after fetching particular details
def issue():
    # It will provide connectivity to the database
    con=DatabaseConnectivity()
    cur = con.cursor()

    global issueBtn, labelFrame, lb1, inf1, inf2, inf4, quitBtn, root, Canvas1, status, studentname, mem_id, show
    
    # Fetching details from the form
    bid = inf1.get()
    mem_id = inf2.get()
    studentname=inf4.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    inf4.destroy()
    
    # Select bookId from "bookTable" to issue specific book to the user
    extractBid = "select bid from "+bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
            
        # Check if particular book ID is available in all list of book.
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
            # Check if the status is "Avaiable/ Issue"    
            if check == 'available':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
        
    # Inserting data into "issueTable"
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+mem_id+"','"+studentname+"')"
    show = "select * from "+issueTable
    # Updating the status of the particular book 
    updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

    
    allBid.clear()
    
# This function will issue specific book to the user
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,inf4,quitBtn,root,Canvas1,status
    
    # Form sizing
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    # Background color
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    # Heading of the current form 
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Adding book Id
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=('Courier', 15))
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Member id is added here
    lb2 = Label(labelFrame,text="Member ID : ", bg='black', fg='white',font=('Courier', 15))
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)

    # Issued To Student name
    lb3 = Label(labelFrame, text="Student Name : ", bg='black', fg='white',font=('Courier', 15))
    lb3.place(relx=0.05, rely=0.6)

    inf4 = Entry(labelFrame)
    inf4.place(relx=0.3, rely=0.6, relwidth=0.62)

    #Issue button is added here 
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue,font=('Courier', 15))
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit button is added to destroy current event and return to previous form
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy,font=('Courier', 15))
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
