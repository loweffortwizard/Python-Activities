#importing libs
import time
import sys

#defining function for waiting 1 second
def wait():
	time.sleep(1)
	#wait 1 second //// 1 = how long to wait

'''
defining square function - will be used to get input of square 
and calculate area of numbers given, then print that result to the user
'''
def square():
	getinput1 = int(input("Enter width: "))
	#getting user input, converting the input to an integer, then saving that input into a variable called getinput1.
	wait()
	#calling defined function wait() to wait 1 second
	print(getinput1)
	#printing users input
	wait()
	#waiting 1 second 
	
	getinput2 = int(input("Enter length: "))
	#getting user input, converting the input to an integer, then saving that input into a variable called getinput1.
	wait()
	#waiting 1 second 
	print(getinput2)
	#printing user input
	wait()
	#waiting 1 second
	
	area = getinput1 * getinput2
	#var area has value of vars getinput1 times the value of getinput2
	
	print("The area is: ", area)
	#printing area variable
	wait()
	#waiting 1 second 
	
	print("End of prog.")
	#print above.

square()
#calling function square() ---- this is needed else the program will not run the program to calculate the square of two numbers.	