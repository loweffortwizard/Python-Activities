'''

	This errors function will be used to determain if the user's input
	is an int type, or can be converted to an int.

	If yes, it will ask for another input, then another, then end.

	If the user enters a string or invalid data, the user will be asked to
	enter their input again, until the correct input has been entered. 

'''

#importing libs.
import time
import sys

#defining functions.

#function will close the program.
def closeprog(txt):
    txt.lower()
    if(txt!='y'):
        print("Exiting...")
        sys.exit()
    elif(txt=='y'):
        print("Restarting program.")
        main()
    else:
        print("Error closing program")

#function will ask for user input if wanting to end program.
def usersdecision():
    #getting user input, converting to string and saving result in var userchoice
    userchoice = str(input("If you wish to use again, press \"Y\": "))
    return userchoice
    
#function will wait 1 second.
def wait():
    #wait for 1 second
    time.sleep(1)

#function will print message when user enter an invalid input in main function.
def errormessage():
    #print below - \n mean make a new line.
    print("Error: Please enter a number, not a letter/word.\nYou cannot continure without entering a number.")

#function will check the data type of the input
def main():
    wait()
    #iterate first try
    while True:
        #try to get input
        try:
            #getting input and converting to an int - saving in var userinput1
            userinput1 = int(input(("Enter the first number: ")))
            wait()
            #if int - will go to next loop
            break 

        #user input gets rejected on any input except an int value
        except ValueError:
                #calling error and wait function.
                errormessage()
                wait()
                #loop back to ask for input
                continue 
            
    #iterate second try
    while True:
        try:
            #getting input and converting to an int - saving in var userinput2
            userinput2 = int(input(("Enter the second number: ")))
            #if int - will go to next loop
            wait()
            break 
            
        #user input gets rejected on any input except an int value
        except ValueError:
                #calling error and wait function.
                errormessage()
                wait()
                #loop back to ask for input
                continue 
            
    #iterate final try
    while True:
        try:
            #getting input and converting to an int - saving in var userinput3
            userinput3 = int(input(("Enter the third number: ")))
            wait()
            #if int - will go to next loop
            break 
            
        #user input gets rejected on any input except an int value
        except ValueError:
                #calling error and wait function.
                errormessage()
                wait()
                #loop back to ask for input
                continue 
    
    #var sum has value of all three inputs added together. 
    total = userinput1 + userinput2 + userinput3
    
    #print below
    print("The sum of ", userinput1, " + ", userinput2, " + ", userinput3, "is ", total)
    wait()
    
    #asking if user will close program
    closeprog(usersdecision())

#calling main function - run prog.
main()
