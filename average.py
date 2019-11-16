'''
	Ask the user to enter 5 numbers. Keep a running total and print the total and average of the numbers. 
'''
#importing libs
import time
import sys

#wait def.
def wait():
    time.sleep(1)

#closing prog y/n.
def CloseProg(txt):
    txt.lower()
    if(txt!='y'):
		wait()
        sys.exit()
    else:
		wait()
        print("")

#getting desision for closing prog.
def UsersDecision():
    userChoice = str(input("If you wish to use again, press \"Y\": "))
    return userChoice

def main():
	
	#get first number. 
	num1 = int(input("Enter number: "))
	print(num1)
	wait()
	
	#get second number,
	num2 = int(input("Enter number: "))
	print(num2)
	wait()
	
	#get thrid number. 
	num3 = int(input("Enter number: "))
	print(num3)
	wait()
	
	#get fourth number.
	num4 = int(input("Enter number: "))
	print(num4)
	wait()
	
	#get fifth number. 
	num5 = int(input("Enter number: "))
	print(num5)
	wait()
	
	#working out sum of all numbers.
	sum = num1 + num2 + num3 + num4 + num5
	
	#working out average
	average = sum / 5
	
	#printing average
	print("The total is: ", average)
	wait()
	
	#user choice to end or restart prog
	CloseProg(UsersDecision())
	wait()

main()