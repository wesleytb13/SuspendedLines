import datetime
import mysql.connector
from mysql.connector import Error
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

def add_phone_line():
    phoneNum = input("Please enter phone number (xxx-xxx-xxxx): ")
    inputDate = input("Please enter date suspended (DD-MM-YYYY): ")
    suspendDate = parse(inputDate).strftime("%Y-%m-%d")
    tempDate = parse(inputDate)+ relativedelta(days=90)
    activeDate = tempDate.strftime("%Y-%m-%d")
    cursor = connection.cursor()
    result = cursor.execute("INSERT INTO numbers (PhoneNumber, SuspendDate, ActivateDate) VALUES (%s, %s, %s)", (phoneNum, suspendDate, activeDate))
    connection.commit()
    print("Number added successfully.")
    print("")


def del_phone_line():
    phoneNum = input("Please enter phone number to delete (xxx-xxx-xxxx): ")
    cursor = connection.cursor()
    result = cursor.execute("DELETE FROM numbers where PhoneNumber = %s", (phoneNum,))
    connection.commit()
    print("Number removed successfully.")
    print("")

def change_dates():
    phoneNum = input("Please enter phone number to edit (xxx-xxx-xxxx): ")
    inputDate = input("Enter new suspension date (MM-DD-YYYY): ")
    newDate = parse(inputDate).strftime("%Y-%m-%d")
    tempDate = parse(inputDate)+ relativedelta(days=90)
    activeDate = tempDate.strftime("%Y-%m-%d")
    cursor = connection.cursor()
    result = cursor.execute("UPDATE numbers SET SuspendDate = %s WHERE PhoneNumber = %s", (newDate, phoneNum))
    result1 = cursor.execute("UPDATE numbers SET ActivateDate = %s where PhoneNumber = %s", (activeDate, phoneNum))
    print("Number updated successfully.")
    print("")


def view_overdue():
    todayDate = datetime.datetime.now()
    now = todayDate.strftime("%Y-%m-%d")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM numbers where ActivateDate < %s", (todayDate, ))
    result = cursor.fetchall()
    if not result:
        print("")
        print("There are no numbers that need to be suspended at this time!")
        print("")
    else:
        print("PhoneNumber    SuspendDate    ActivateDate   ")
        for row in result:
            print(row[0], " ", row[1], "     ", row[2], "   ", "\n")


def view_number():
    phoneNum = input("Please enter the phone number you want to check (xxx-xxx-xxxx): ")
    print(phoneNum)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM numbers where PhoneNumber = %s", (phoneNum, ))
    result = cursor.fetchall()
    if not result:
        print("")
        print("There was no entry that matches that number.")
        print("")
    else:
        print("PhoneNumber    SuspendDate    ActivateDate   ")
        for row in result:
            print(row[0], " ", row[1], "     ", row[2], "   ", "\n")

try:
    connection = mysql.connector.connect(host='', database='', user="", password='')
    print("Welcome to the Suspended Lines App")
    print("------------------------------------")
    print("Please choose an option below(1-5): ")
    print("1. Add a suspended line.")
    print("2. Remove line from database.")
    print("3. Edit suspension date for an existing line.")
    print("4. View overdue lines.")
    print("5. View specific line status.")
    print(" ")
    userOption = input("Enter option to continue or 'quit' to exit: ")
    while userOption != "quit":
        if userOption == '1':
            add_phone_line()
        elif userOption == '2':
            del_phone_line()
        elif userOption == '3':
            change_dates()
        elif userOption == '4':
            view_overdue()
        elif userOption == '5':
            view_number()
        print("Please choose an option below(1-5): ")
        print("1. Add a suspended line.")
        print("2. Remove line from database.")
        print("3. Edit suspension date for an existing line.")
        print("4. View overdue lines.")
        print("5. View specific line status.")
        print(" ")
        userOption = input("Enter option to continue or 'quit' to exit: ")



except Error as e :
    print("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if connection.is_connected():
        connection.close()
