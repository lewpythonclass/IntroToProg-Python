#Assignment07 Exception Handling
#Intro to Python
#Laura Wick
#02/25/2019


#Create a simple example of how you would use Python Exception Handling. 

#first take in the user input with a data type cast to integer
#use the basic ValueError exception, which catches non-integer input values
#if the exception is not encountered, move on to the number guessing code

try:  
    x = int(input("What integer number am I thinking of?  "))
except ValueError:
    print("ValueError:  that's not an integer number.")
else:
    print("Good, you successfully entered an integer.")  #passed the exception case
    if x==7:
        print("Yes, seven!")  #correct answer
    else:
        print("...but it's not the number I had in mind.")
