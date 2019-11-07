# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JRiley,11.1.2019,Added code to work on assignment 5
# JRiley,11.6.2019,Finished adding code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python Dictionary.
read = open(objFile, "r")
for row in read:
    strData = row.split(",")
    dicRow = {"TASK":strData[0], "PRIORITY":strData[1].strip()}
read.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for row in lstTable:
            print(row["TASK"] + ", " + row["PRIORITY"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        Task = str(input("Add a task please: "))
        print()
        Priority = str(input("Add a priority please: "))
        print()
        dicRow = {"TASK": Task, "PRIORITY": Priority.strip()}
        lstTable.append(dicRow)
        print("adding to list... \nAdded. \n")
        continue

    # Step 5 - Remove new item from the list/Table
    elif strChoice.strip() == '3':
        delete = input("Are you sure you want to delete: Yes or No? ")
        if delete.lower() == "yes":
            del lstTable[len(lstTable)-1]
            print(" \n Task was deleted from list... \n")
        else:
            print(" \n Nothing was deleted because you chickened out... \n")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        save = open(objFile, "w")
        for row in lstTable:
            save.write(row["TASK"]+ ", " + row["PRIORITY"] + "\n")
        save.close()
        print("The data was saved to your .txt file \n")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Program has closed \n")
        break  # and Exit the program
