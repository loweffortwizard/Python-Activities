'''
	prog will compare two numbers.
'''

#importing lib and creating functions
import time
def wait():
    time.sleep(1)

#getting user input
number1 = int(input("Enter number: "))
wait()
number2 = int(input("Enter number: "))
wait()

#if number1 var is smaller, do this.
if (number1 < number2):
    print("Number 2 is greater than number 1")
    wait()

#if number1 is = to number2, do this.
if (number1 == number2):
    print("The numbers a equal")
    wait()

#if number1 or number2 is not equal, do this. 
if (number1 != number2):
    print("The numbers are not equal")
    wait()
	
if (number1 >= 50):
    print("The number:", number1, "is larger than or equal to 50.")
    wait()
else:
    print("The number:", number1, "is smaller than 50.")
    wait()

if (number2 >= 50):
    print("The number:", number2, "is larger than or equal to 50.")
    wait()
else:
    print("The number:", number2, "is smaller than 50.")
    wait()
	
print("End")
wait()

#end of prog
'''
•	Extend activity 2 by making the program display one of the following statements – depending upon the number that the user has entered.
o	The number is greater than 50
o	The number is exactly 50
o	The number is lesson than 50
'''
#getting input
number = int(input("Enter a number: "))
wait()
#if number > 50, do this
if (number > 50):
	print("The number", number, "is greater than 50")
	wait()
#else if number == 50, do this
elif(number == 50):
	print("The number", number, "is equal to 50")
	wait()
#else number is smaller than 50, do this
else:
	print("The number", number, "is less than 50")
	wait()
print("End")
wait()
#end of prog