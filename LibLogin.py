from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from MenuForLibrarian import *
import DatabaseConnectivity

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


def loginLibrarian():
    global loginInfo1,loginInfo2,loginInfo3,Canvas1,con,cur,studentTable,root
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")
    # Add your own database name and password here to reflect in the code
    con=DatabaseConnectivity()
    cur = con.cursor()


    studentTable = "members" 

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Login for Librarian", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # student ID
    lb1 = Label(labelFrame,text="Member ID : ", bg='black', fg='white',font=('Courier', 15))
    lb1.place(relx=0.05,rely=0.05, relheight=0.08)
  
    loginInfo1 = Entry(labelFrame)
    loginInfo1.place(relx=0.3,rely=0.05, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame,text="Username : ", bg='black', fg='white',font=('Courier', 15))
    lb2.place(relx=0.05,rely=0.2, relheight=0.08)

    loginInfo2 = Entry(labelFrame)
    loginInfo2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)    

    lb3 = Label(labelFrame,text="Password : ", bg='black', fg='white',font=('Courier', 15))
    lb3.place(relx=0.05,rely=0.35, relheight=0.08)
        
    loginInfo3 = Entry(labelFrame)
    loginInfo3.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
    
            
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=librarianLogin,font=('Courier', 15))
    SubmitBtn.place(relx=0.23,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="RETURN",bg='#f7f1e3', fg='black', command=returnback,font=('Courier', 15))
    quitBtn.place(relx=0.46,rely=0.9, relwidth=0.18,relheight=0.08)
