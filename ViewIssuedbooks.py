from StuLogin import *
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from DatabaseConnectivity import *


# It will fetch data from database and show details of books issued to particular user
def ViewIssued(id):
    global bookTable

    # It will provide database connectivity
    con=DatabaseConnectivity()
    cur = con.cursor()

    # Table name is mentioned here
    bookTable = "books"
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#D7C0D0")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
      
    # Heading of the form 
    headingLabel = Label(headingFrame1, text="Issued Books", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    # Fields are displayed in the current window as mentioned below and data are displayed accordingly in each field
    Label(labelFrame, text="%-10s%-20s%-20s"%('BID','Title','Author'),bg='black',fg='white',font=('Courier', 20)).place(relx=0.01,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------------------------------------------------",bg='black',fg='white',font=('Courier', 20)).place(relx=0,rely=0.2)
    getBooks = 'SELECT * FROM books as b left join books_issued as i on i.bid =b.bid where i.mem_id="'+id+'"'
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-20s%-20s"%(i[0],i[1],i[2]),bg='black',fg='white',font=('Courier', 20)).place(relx=0.01,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    # Quit button is added to destroy the current event
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Courier', 15))
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
