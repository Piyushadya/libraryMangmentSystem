from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from MenuForLibrarian import *
from DatabaseConnectivity import *

# This function is added to fetch the data from the user form and check if the credentials are Valid or not
def librarianLogin():
    memId = loginInfo1.get()
    username = loginInfo2.get()
    password = loginInfo3.get()
    if memId == "" or username == "" or password =="":
        messagebox.showinfo("Error","Please complete the required field!")
    else:
      if memId=="0" and username=="admin" and password == "admin"  :
          messagebox.showinfo('success',"You Successfully Login")
          menuForLibrarian()
          root.destroy()
      else:
            messagebox.showinfo("Error","Invalid Username or password")
    cur.close()
    con.close()

def returnback():

    root.destroy()

# This function is added to display the form to the user, where they can add login credentials
def loginLibrarian():
    global loginInfo1,loginInfo2,loginInfo3,Canvas1,con,cur,studentTable,root
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")
    
    # It will provide database connectivity
    con=DatabaseConnectivity()
    cur = con.cursor()

    Canvas1 = Canvas(root)

    #Background color
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    # Heading of the form
    headingLabel = Label(headingFrame1, text="Login for Librarian", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Login ID for librarian
    lb1 = Label(labelFrame,text="Member ID : ", bg='black', fg='white',font=('Courier', 15))
    lb1.place(relx=0.05,rely=0.05, relheight=0.08)
  
    loginInfo1 = Entry(labelFrame)
    loginInfo1.place(relx=0.3,rely=0.05, relwidth=0.62, relheight=0.08)

    # Username of librarian
    lb2 = Label(labelFrame,text="Username : ", bg='black', fg='white',font=('Courier', 15))
    lb2.place(relx=0.05,rely=0.2, relheight=0.08)

    loginInfo2 = Entry(labelFrame)
    loginInfo2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)    

    lb3 = Label(labelFrame,text="Password : ", bg='black', fg='white',font=('Courier', 15))
    lb3.place(relx=0.05,rely=0.35, relheight=0.08)
     
    # Encryption for the password
    loginInfo3 = Entry(labelFrame, show = "*")
    loginInfo3.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
    
            
        
    # submit button will trigger LibrarianLogin function, where credentials are checked
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=librarianLogin,font=('Courier', 15))
    SubmitBtn.place(relx=0.23,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Return button is added and will return user to the main window of the application
    quitBtn = Button(root,text="RETURN",bg='#f7f1e3', fg='black', command=returnback,font=('Courier', 15))
    quitBtn.place(relx=0.46,rely=0.9, relwidth=0.18,relheight=0.08)
