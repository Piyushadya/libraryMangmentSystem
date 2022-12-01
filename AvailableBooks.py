from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from DatabaseConnectivity import *

# This function will fetch details from the database and show "Available books" to the user 
def AvailableBooks():
    # It will provided connectivity to the database
    con=DatabaseConnectivity()
    cur = con.cursor()
    root = Tk()
    
    # Frame sizing
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    # Adding Background color
    Canvas1.config(bg="#FFC0CB")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    
    #Heading of the current Page
    headingLabel = Label(headingFrame1, text="Available Books", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    # It will provide the column fields of the form where respective data is displayed
    Label(labelFrame, text="%-10s%-20s%-20s"%('BID','Title','Author'),bg='black',fg='white',font=('Courier', 20)).place(relx=0.01,rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white',font=('Courier',20)).place(relx=0,rely=0.2)
    
    # Fetching data from the "books" table where book status is "Available"
    getBooks = "SELECT * FROM books where status ='available'";
    try:
        cur.execute(getBooks)
        con.commit()
        
        # Loop to show respective books details
        for i in cur:
            Label(labelFrame, text="%-10s%-20s%-20s"%(i[0],i[1],i[2]),bg='black',fg='white',font=('Courier', 20)).place(relx=0.01,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
   
# To return to the previous page
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Courier', 15))
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
