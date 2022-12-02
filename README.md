# Welcome to libraryMangmentSystem

## 1. Install Dependencies

Python (must be above v3): https://www.python.org/downloads/

Install any  python IDE such as Pycharm from : https://www.jetbrains.com/pycharm/download/#section=mac  
or VS Code from :https://code.visualstudio.com/Download

To check your Python version, run:
```
python --version
````

Inside a terminal:

tkinter – Please run below command to install tkinter
```
pip install tk
````
pillow – Please run below command to install tkinter
```
pip install pillow
  ````
pymysql – Please run below command to install tkinter
```
python -m pip install PyMySQL  or pip install pymysql
````


# 2. Please make sure to have MySQL Workbench installed : https://dev.mysql.com/downloads/workbench/

Also, after successfully installing the Workbench, to create the instance, please provide below credentials:

 Username :
  ```` 
  root
   ```` 
 Password :
  ```` 
  root1234
  ````
  
Please note: Please provide above credentials while creating instance of Database as our executable contains the same credentials 

After successfully creating instance, Please create database with Name = "library".
Then follow below steps:
  1. click on "Server".
  2. Click on "Data import"
  3. Select Import from Self-Contained File radio button (right side of screen)
  4. Select the path of libraryManagement.sql from our project folder
  5. select the database ("library") from "Default Target Schema:" dropbox
  6. Click Start Import button at the right bottom corner of window

We developed a Library Management System written in Python, tkinter and MySQL

1. Python : is an interpreted, high-level, general-purpose programming language.
            Python can be used in database applications.

2. tkinter : is a module that can be used to create graphical user interfaces (GUI).


3. MySQL : is one of the most common open source databases for storing Python web applications' data.


  Home Page of Application: 

As shown below, it has two buttons:
  1. Librarian Login
  2. Student Login
  
  [https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/Home.png]


For Librarian Login, please add below credentials: https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/Librarian_Login.png

  Member ID : 
  ```
  0 
  ````
  Username :
   ```
admin
  ````
  Password : 
   ```
admin
  ````


For Student Login, please add below credentials: https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/Login_Student.png
  Member ID :
   ```` 
   12 
   ```` 
  Username :
   ```` 
  Piyush
   ```` 
  Password :
   ```` 
  12345
   ```` 
  
  
 If New Student, please Register it in below page after clicking "New User/ Register" Button:
 https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/Register_New_Student.png



After successfull Library Login, the LMS system will display the below features:
  1. Add book details
  2. Delete book
  3. View book list
  4. Issue book to student
  5. Return book
  6. Quit

After clicking "Add book details", below form will open, where you can add information accordingly.
https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/Add_Book_Details.png

After clicking "Delete book", below form will open, where you can add "Book ID" to be deleted.
https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/Delete_Book_Details.png

After clicking "View book list", it will display all the books stored in the inventory.
https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/View_Books_List.png

After clicking "Issue book to student", it will display below form, where you can add information of student to whom you want to issue book
https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/Issue_Book_To_Student.png

After clicking "Return book", it will display below form, where you can add below information
https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/Return_Book.png

After clicking Quit, it will destroy the current event

After successfull Student Login, the LMS system will display the below features:
https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/Menu_For_Student.png

  1. View available books
  2. View issued books

After clicking "View available books", it will display all the books stored in the inventory whose status is "Available"
https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/View_Available_Books_Student.png

After clicking "View issued books", it will display all the books stored in the inventory whose status is "Issued"
https://github.com/Piyushadya/libraryMangmentSystem/blob/master/Images/View_Issued_Books_Student.png


