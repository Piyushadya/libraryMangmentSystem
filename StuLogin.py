from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from MenuForStudent import *
from DatabaseConnectivity import *

# This function will fetch the details from User form and match the existing data stored in database
def studentLogin():
    global studID
    memId = loginInfo1.get()
    username = loginInfo2.get()
    password = loginInfo3.get()

    if memId == "" or username == "" or password =="":
        messagebox.showinfo("Error","Please complete the required field!")
    elif memId == "100" or username == "Admin" or password =="Admin":
        messagebox.showinfo("Error","Not allowed")
    else:
        cur.execute("SELECT * FROM "+studentTable+" WHERE mem_id = '"+memId+"' and username = '"+username+"' and password = '"+password+"'")
        if cur.fetchone() is not None:
            messagebox.showinfo('success',"You Successfully Login")
            menuForStudent(memId)
            root.destroy()

        else:
            messagebox.showinfo("Error","Invalid Username or password")
    cur.close()
    con.close()
    
def stdnumber(number):
    return number

# It will display form to the user to add details of students
def login():
    global loginInfo1,loginInfo2,loginInfo3,Canvas1,con,cur,studentTable,root
    root = Tk()
    root.title("Library")
    root.minsize(width=1100, height=700)
    root.geometry("600x500")
    
    # It will provide the database connectivity
    con=DatabaseConnectivity()
    cur = con.cursor()

    studentTable = "members"

    Canvas1 = Canvas(root)
    
    #Background color
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    # Heading of Login form
    headingLabel = Label(headingFrame1, text="Login", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Field to add member ID 
    lb1 = Label(labelFrame,text="Member ID : ", bg='black', fg='white',font=('Courier', 15))
    lb1.place(relx=0.05,rely=0.05, relheight=0.08)
  
    loginInfo1 = Entry(labelFrame)
    loginInfo1.place(relx=0.3,rely=0.05, relwidth=0.62, relheight=0.08)

    # Field to add Username
    lb2 = Label(labelFrame,text="Username : ", bg='black', fg='white',font=('Courier', 15))
    lb2.place(relx=0.05,rely=0.2, relheight=0.08)

    loginInfo2 = Entry(labelFrame)
    loginInfo2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)    

     # Field to add Password
    lb3 = Label(labelFrame,text="Password : ", bg='black', fg='white',font=('Courier', 15))
    lb3.place(relx=0.05,rely=0.35, relheight=0.08)
     
    # Encrypt password
    loginInfo3 = Entry(labelFrame, show = "*")
    loginInfo3.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    # Submit button to add details of user to database
    SubmitBtn = Entry(labelFrame)
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=studentLogin,font=('Courier', 15))
    SubmitBtn.place(relx=0.3,rely=0.7, relwidth=0.18,relheight=0.08)
    
    # To destroy the current event
    quitBtn = Entry(labelFrame)
    quitBtn = Button(root,text="RETURN",bg='#f7f1e3', fg='black', command=root.destroy,font=('Courier', 15))
    quitBtn.place(relx=0.6,rely=0.7, relwidth=0.18,relheight=0.08)
    
         
    # If new user, User can register themself by clicking this Button
    registerBtn = Button(root,text="New User/ Register",bg='#d1ccc0', fg='black',command=addStudent,font=('Courier', 15))
    registerBtn.place(relx=0.2,rely=0.9, relwidth=0.62, relheight=0.08)    
    
    root.mainloop()

# This function is used to Fetch data from the register form and add them into database 
def studentRegister():
    memId = studentInfo1.get()
    username = studentInfo2.get()
    password = studentInfo3.get()
    firstname = studentInfo4.get()
    lastname = studentInfo5.get()
    print(memId)

    if memId =="" or username == "" or password == "" or firstname == "" or lastname == "":
         messagebox.showinfo("Error","Please complete the required field!")
    elif memId == "100" or username == "Admin" or password == "Admin":
        messagebox.showinfo("Error","Not allowed")
    else:
        cur.execute("SELECT * FROM "+studentTable+" WHERE `username` = '"+username+"'")
        if cur.fetchone() is not None:
            messagebox.showinfo("Error","Username is already taken")
        else:
            cur.execute("INSERT INTO "+studentTable+" (mem_id, username, password, firstname, lastname) VALUES('"+str(memId)+"','"+str(username)+"','"+str(password)+"', '"+str(firstname)+"', '"+str(lastname)+"')")
            con.commit()
            
            messagebox.showinfo('Success',"student added successfully")
            root.destroy()


def returnback():
    root.destroy()
    studentLogin()

# Form where user can add their details to register themself in LMS
def addStudent():
    global studentInfo1,studentInfo2,studentInfo3,studentInfo4,studentInfo5,Canvas1,con,cur,studentTable,root
    root = Tk()
    # Frame sizing
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    # Provide connection to the database
    con=DatabaseConnectivity()
    cur = con.cursor()
    # Table name is added here
    studentTable = "members"

    Canvas1 = Canvas(root)
    
    #Background color
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    # Heading of the form
    headingLabel = Label(headingFrame1, text="Register", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
     
    # Field to add member ID
    lb1 = Label(labelFrame,text="Member ID : ", bg='black', fg='white',font=('Courier', 15))
    lb1.place(relx=0.05,rely=0.05, relheight=0.08)
  
    studentInfo1 = Entry(labelFrame)
    studentInfo1.place(relx=0.3,rely=0.05, relwidth=0.62, relheight=0.08)

    # Field to add Username
    lb2 = Label(labelFrame,text="Username : ", bg='black', fg='white',font=('Courier', 15))
    lb2.place(relx=0.05,rely=0.2, relheight=0.08)

    studentInfo2 = Entry(labelFrame)
    studentInfo2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)    

    # Field to add Password
    lb3 = Label(labelFrame,text="Password : ", bg='black', fg='white',font=('Courier', 15))
    lb3.place(relx=0.05,rely=0.35, relheight=0.08)
      
    # Encrypt password
    studentInfo3 = Entry(labelFrame, show = "*")
    studentInfo3.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
     
    # Field to add FirstName
    lb4 = Label(labelFrame,text="Firstname : ", bg='black', fg='white',font=('Courier', 15))
    lb4.place(relx=0.05,rely=0.50, relheight=0.08)
        
    studentInfo4 = Entry(labelFrame)
    studentInfo4.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
    
    # Field to add LastName
    lb5 = Label(labelFrame,text="Lastname : ", bg='black', fg='white',font=('Courier', 15))
    lb5.place(relx=0.05,rely=0.65, relheight=0.08)
        
    studentInfo5 = Entry(labelFrame)
    studentInfo5.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    # Submit button to Register new user to LMS system
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=studentRegister,font=('Courier', 15))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit button to destroy the current event
    quitBtn = Button(root,text="RETURN",bg='#f7f1e3', fg='black', command=returnback,font=('Courier', 15))
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
