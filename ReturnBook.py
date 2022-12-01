from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

from DatabaseConnectivity import *

# It will provide the database connectivity
con=DatabaseConnectivity()
cur = con.cursor()


# Table name for issued books and all books is provided
issueTable = "books_issued" #Issue Table
bookTable = "books" #Book Table


allBid = [] #List To store all Book IDs

# This function will get the book ID from the Form 
def return_book():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()

    # It will store bid fetched from issueTable in temporary variable for further use
    extractBid = "select bid from "+issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
        
        # It will check the status of particular book from list of all books on the basis of ID entered by user
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
    issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"
  
    print(bid in allBid)
    print(status)
    
    # It will change the status to "Avaialble" after book is retured successfully
    updateStatus = "update "+bookTable+" set status = 'available' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allBid.clear()
    root.destroy()
    
   
# Display the form to the user to return book    
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    # Form sizing
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    #Background color
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
      
    # Form heading
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Enter book ID whose info you want to modify
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=('Courier', 15))
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    # submit button is added to trigger the return_book function
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=return_book,font=('Courier', 15))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit button is added to destroy the current event and redirect the user to previous page
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Courier', 15))
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
