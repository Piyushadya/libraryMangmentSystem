import pymysql

# It will provide connection to the database
def DatabaseConnectivity():

    # Provide Database credentials
    mypass = "root1234"
    mydatabase = "library"

    # Connection to the database
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    return con

print(DatabaseConnectivity())
