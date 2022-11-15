from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from LibLogin import *
from StuLogin import *
from DatabaseConnectivity import *

print(DatabaseConnectivity())
def main():
    global cur
    con=DatabaseConnectivity()
    cur = con.cursor()

    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")

    # Take n greater than 0.25 and less than 5
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

    headingLabel = Label(headingFrame1, text="Welcome to \n Library Management System", bg='black', fg='white',
                         font=('Courier', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Librarian Login", bg='black', fg='white',font=('Courier', 15), command=loginLibrarian)
    btn1.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Student Login", bg='black', fg='white',font=('Courier', 15), command=login)
    btn2.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    root.mainloop()

main()