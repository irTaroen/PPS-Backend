import mysql.connector

if __name__=="__main__":
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Root",
        database="pps")
    
    mycursor = db.cursor()
    
    # Create Database PPS 
    mycursor.execute("CREATE DATABASE pps")

    # Create Table Orders
    mycursor.execute("CREATE TABLE Orders (first_name VARCHAR (50), mobile_number VARCHAR (50), email VARCHAR (50), weight DECIMAL(10, 2), method VARCHAR (50), description VARCHAR (200), order_id int PRIMARY KEY AUTO_INCREMENT)")