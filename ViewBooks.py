from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from DatabaseConnectivity import *


# It display all books to the user
def View():
    global bookTable

    # It will provide database connectivity
    con=DatabaseConnectivity()
    cur = con.cursor()

    # Table name is mentioned here
    bookTable = "books"

    root = Tk()
    
    # Form sizing
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    # Heading of the form 
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    # It will display all fields as column in particular page and show the fetched values accordingly in the respective fields
    Label(labelFrame,
          text="%-10s%-20s%-20s%-20s%-20s%-20s" % ('BID', 'Title', 'Author', 'Status', 'StudentNumber', 'StudentName'),
          bg='black', fg='white',font=('Courier', 16)).place(relx=0.01, rely=0.1)
    Label(labelFrame,
          text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
          bg='black', fg='white',font=('Courier', 16)).place(relx=0, rely=0.2)
    getBooks = 'SELECT * FROM books as b left join books_issued As i on i.bid =b.bid'

    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-20s%-20s%-20s%-20s%-20s" % (i[0], i[1], i[2], i[3], i[5], i[6]), bg='black',
                  fg='white',font=('Courier', 16)).place(relx=0.01, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    # Quit button to destroy the current event 
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy,font=('Courier', 15))
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
