'''
	program will be used to get two numbers from user,
	then times them together. 
'''

import time
# importing use of time. 

### creating function to wait for 1 second. ###
def wait():
    time.sleep(1)
    # waiting for 1 second
    #end of def

print("Welcome")
#print above.

userInput1 = int(input("Enter number: "))
# get user input, save it as an int and save that value in var userInput1.
wait()#calling function. 

print ("You entered", userInput1)
# print userInput1 var
wait()#calling function. 

userInput2 = int(input("Enter another number: "))
# get user input, save it as an int and save that value in var userInput2.
wait()#calling function. 

print ("You entered", userInput2)
# print userInput2
wait()#calling function. 

total = userInput1 * userInput2
#var total equals userInput1 times userInput2
wait()#calling function. 

print("The value of ", userInput1, "X ", userInput2, " = ", total)
#print results from calculation.
wait()#calling function. 
        
print("end program")
### end of program ### 
