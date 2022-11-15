import pymysql

def DatabaseConnectivity():

    mypass = "root1234"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    return con

print(DatabaseConnectivity())