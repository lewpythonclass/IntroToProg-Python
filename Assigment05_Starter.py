#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Laura Wick, 02/2019, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user
def showToDo(): 
    for item in lstTable:
        tasklist = ''
        for mykey,myvalue in item.items():
            #print(mykey, " = " , myvalue)
            tasklist = tasklist + mykey + " = " + myvalue + " "
        print(tasklist)
         
# Step 4
# Add a new item to the list/Table
def addToDo():
    newtask = input("What do you want to do?")
    newpriority = input("What is the priority level?")
    newDic = {"Task": newtask, "Priority": newpriority}
    lstTable.append(newDic)
    
    
# Step 5
# Remove a new item to the list/Table
def removeToDo():
    whichone = input("Which task do you want to remove?")
    for item in lstTable:
        if item.get("Task") == whichone:
            lstTable.remove(item)
    print(lstTable)     
    
# Step 6
# Save tasks to the ToDo.txt file
def saveTasks():
    fn = open(objFileName, "w")
    for item in lstTable:
        print(item.get("Task") + "," + item.get("Priority") + '\n')
        fn.write(item.get("Task") + "," + item.get("Priority") + '\n')
        
# Step 7


#declarations#
objFileName = "C:\_PythonClass\Assignment05_LauraWick\Todo.txt"  # 02/2010 changed to my specific folder
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add each dictionary "row" to a python list "table"
    
with open(objFileName, "r+") as f:
    for line in f:
        line = line.rstrip()
        ltbl = line.rsplit(",")
        dicRow = {"Task":ltbl[0], "Priority":ltbl[1]}
        lstTable.append(dicRow)        
        
#objFileName.close()  
     
        
# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        showToDo()
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        addToDo()
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        removeToDo()
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        saveTasks()
        continue
    elif (strChoice == '5'):
        break #and Exit the program



