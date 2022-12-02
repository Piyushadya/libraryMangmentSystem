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
 ```` Username = root
  Password = root1234
  ````
  
Please note: Please provide above credentials while creating instance of Database as our executable contains the same credentials 

We developed a Library Management System written in Python, tkinter and MySQL

1. Python : is an interpreted, high-level, general-purpose programming language.
            Python can be used in database applications.

2. tkinter : is a module that can be used to create graphical user interfaces (GUI).


3. MySQL : is one of the most common open source databases for storing Python web applications' data.


  Home Page of Application:

As shown below, it has two buttons:
  1. Librarian Login
  2. Student Login


For Librarian Login, please add below credentials:
```
  Member ID : 0
  Username : admin
  Password : admin
 ````

For Student Login, please add below credentials:
```
  Member ID : 12
  Username : Piyush
  Password : 12345
  ````
  
  
 If New Student, please Register it in below page after clicking "New User/ Register" Button:

![admin](https://user-images.githubusercontent.com/73725029/109415230-cd94f700-79b7-11eb-9869-e345a1e575cd.png)


After successfull Library Login, the LMS system will display the below features:
  1. Add book details
  2. Delete book
  3. View book list
  4. Issue book to student
  5. Return book
  6. Quit

After clicking "Add book details", below form will open, where you can add information accordingly.
After clicking "Delete book", below form will open, where you can add "Book ID" to be deleted.
After clicking "View book list", it will display all the books stored in the inventory.
After clicking "Issue book to student", it will display below form, where you can add information of student to whom you want to issue book
After clicking "Return book", it will display below form, where you can add below information
After clicking Quit, it will destroy the current event

After successfull Student Login, the LMS system will display the below features:
  1. View available books
  2. View issued books

After clicking "View available books", it will display all the books stored in the inventory whose status is "Available"
After clicking "View issued books", it will display all the books stored in the inventory whose status is "Issued"


