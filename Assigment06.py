#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  Sept 16, 2017
# ChangeLog: (Who, When, What)
#   RRoot, 09/16/2017, Created Script
#  Laura Wick, 02/18/2019, started with Sample Code and modified to encaps. 
#                           -> add globabl variable declarations to top
#                           -> add functions, moved processing work to functions
#                           -> change to class, add def to function names, add self. to global variables

#-------------------------------------------------#


# =============================================================================
# class todo(object):  #this class contains methods to maintain a to do list#
#     Id = None
#     Name = None
# 
#     def ToString(self):
#         return str(self.Id) + "," + str(self.Name)
# =============================================================================

class todo(object):
    #class for a to-do list
    
    Id = None
    Name = None
    
    def ToString(self):
        return str(self.Id) + "," + str(self.Name)
    
    
    #-- Data --#
    # declare variables and constants
    
    # objFile = An object that represents a file
    objFileName = "C:\_PythonClass\Assignment06_LauraWick\Todo.txt"
    
    # strData = A row of text data from the file
    strData = ""
    
    # dicRow = A row of data separated into elements of a dictionary {Task,Priority}
    dicRow = {}
    
    # lstTable = A dictionary that acts as a 'table' of rows
    lstTable = []
    
    # strMenu = A menu of user options
    strMenu = ("""
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)
    
    # strChoice = Capture the user option selection
    strChoice = '' #str(input("Which option would you like to perform? [1 to 4] - "))
    
    
    #-- Input/Output --#
    # User can see a Menu (Step 2)
    # User can see data (Step 3)
    # User can insert or delete data(Step 4 and 5)
    # User can save to file (Step 6)
    
    #-- Processing --#
    # Step 1
    # When the program starts, load the any data you have
    # in a text file called ToDo.txt into a python Dictionary.
    def loadToDoList(self):
        objFile = open(self.objFileName, "r")
        for line in objFile:
            strData = line.split(",") # readline() reads a line of the data into 2 elements
            dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
            self.lstTable.append(dicRow)
        objFile.close()    
    
    # Step 2
    # Display a menu of choices to the user
    def displayMenu(self):
        print(self.strMenu)
        
    # Step 3
    # Display all todo items to user
    def displayItems(self):
        print("******* The current items ToDo are: *******")
        for row in self.lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
    
    
    # Step 4
    # Add a new item to the list/Table
    def addNewItem(self):
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        dicRow = {"Task":strTask,"Priority":strPriority}
        self.lstTable.append(dicRow)
    
        self.displayItems()  #4a Show the current items in the table
    
    # Step 5
    # Remove a new item to the list/Table
    def removeItem(self):
        #5a-Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False #Creating a boolean Flag
        intRowNumber = 0
        while(intRowNumber < len(self.lstTable)):
            if(strKeyToRemove == str(list(dict(self.lstTable[intRowNumber]).values())[0])): #the values function creates a list!
                del self.lstTable[intRowNumber]
                blnItemRemoved = True
            #end if
            intRowNumber += 1
        #end for loop
        
        #5b-Update user on the status
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
    
        self.displayItems()
    
    # Step 6
    # Save tasks to the ToDo.txt file
    def saveTasks(self):
        
        self.displayItems()
    
        #5b Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(self.objFileName, "w")
            for dicRow in self.lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")    
    
    # Step 7
    # Exit program
    #-------------------------------1

#run the main part here...
    
td = todo()  #instantiate the todo() list class, below, add td. to the functions, they are now methods


# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
td.loadToDoList()


# Step 2
# Display a menu of choices to the user
while(True):
    
    td.displayMenu()
   
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3
    # Show the current items in the table
    if (strChoice.strip() == '1'):
        td.displayItems()

    # Step 4
    # Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        td.addNewItem()
        continue #to show the menu

    # Step 5
    # Remove a new item to the list/Table
    elif(strChoice == '3'):
        td.removeItem()
        continue #to show the menu

    # Step 6
    # Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        td.saveTasks()
        continue #to show the menu
        
    elif (strChoice == '5'):
        break #and Exit the program


#objectToDo = todo()
