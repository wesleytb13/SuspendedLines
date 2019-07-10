import mysql.connector
from mysql.connector import Error
from datetime import date, datetime, timedelta

def add_phone_line():
    phoneNum = input("Please enter phone number (xxx-xxx-xxxx): ")
    suspendDate = input("Please enter date suspended (YYYY-MM-DD): ")
    print(suspendDate)
    #sql_insert_query = """INSERT INTO `numbers` (`PhoneNumber`, `SuspendDate`) VALUES ('phoneNum', 'suspendDate')"""
    #cursor = connection.cursor()
    #result = cursor.execute(sql_insert_query)
    #connection.commit()
    #print("Number added successfully.")
    #print("")

try:
    connection = mysql.connector.connect(host='192.168.20.87', database='suspended', user="", password='l1n3 t3st *6')
    print("Welcome to the Suspended Lines App")
    print("------------------------------------")
    print("Please choose an option below(1-4): ")
    print("1. Add a suspended line.")
    print("2. Remove line from database.")
    print("3. Edit dates for an existing line.")
    print("4. View overdue lines.")
    print(" ")
    userOption = input("Enter option: ")

    if userOption == '1':
        add_phone_line()
    else:
        print("Boo")



except Error as e :
    print("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if connection.is_connected():
        connection.close()
