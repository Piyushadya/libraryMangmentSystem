from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

import DatabaseConnectivity



def AvailableBooks():
    # Add your own database name and password here to reflect in the code
    con=DatabaseConnectivity()
    cur = con.cursor()
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFC0CB")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Availables Books", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0,rely=0.3,relwidth=1,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-10s%-20s%-20s"%('BID','Title','Author'),bg='black',fg='white',font=('Courier', 20)).place(relx=0.01,rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white',font=('Courier',20)).place(relx=0,rely=0.2)
    getBooks = "SELECT * FROM books where status ='avail'"; # change books with your table name
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-20s%-20s"%(i[0],i[1],i[2]),bg='black',fg='white',font=('Courier', 20)).place(relx=0.01,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Courier', 15))
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()