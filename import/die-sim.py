#importing libs
import time
import sys
import random

#wait def
def wait():
	time.sleep(1)

def CloseProg(txt):
    txt.lower()
    if(txt!='y'):
        sys.exit()

def UsersDecision():
    userChoice = str(input("If you wish to use again, press \"Y\": "))
    return userChoice
def main()
	die1 = random.randint(1, 6)
	die2 = random.randint(1, 6)
	
	if die1 == die2:
		print("You threw a double", die1)
	else:
		print("Not a double: \nDie 1 = ", die1, "\nDie 2 = ", die2)
	
	CloseProg(UsersDecision())
	wait()	
	
main()