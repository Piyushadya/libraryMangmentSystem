from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from LibLogin import *
from StuLogin import *
from DatabaseConnectivity import *

# We created this "main" funtion that will view to users as the first page when they run this application 
def main():
    global cur
# This will create a connection with the database
    con=DatabaseConnectivity()
    cur = con.cursor()

# Adding Frame size for the current page
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    same = True
    n = 1.2

# Adding a background image
    background_image = Image.open("img.jpeg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    if same:
        newImageSizeHeight = int(imageSizeHeight * n)
    else:
        newImageSizeHeight = int(imageSizeHeight / n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(340,300, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    
# Adding heading for the current page
    headingLabel = Label(headingFrame1, text="Welcome to \n Library Management System", bg='black', fg='white',
                         font=('Courier', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
# Creating button to link login for the librarian 
    btn1 = Button(root, text="Librarian Login", bg='black', fg='white',font=('Courier', 15), command=loginLibrarian)
    btn1.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
    
# Creating button to link login for the student
    btn2 = Button(root, text="Student Login", bg='black', fg='white',font=('Courier', 15), command=login)
    btn2.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    root.mainloop()

main()
