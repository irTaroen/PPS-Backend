import mysql.connector

if __name__=="__main__":
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Root",
        database="pps")
    
    mycursor = db.cursor()
    