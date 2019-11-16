#importing libs.
import time
import sys
import random

#wait def.
def wait():
	time.sleep(1)

#closing prog y/n.
def CloseProg(txt):
    txt.lower()
    if(txt!='y'):
        sys.exit()

#getting desision for closing prog.
def UsersDecision():
    userChoice = str(input("If you wish to use again, press \"Y\": "))
    return userChoice

def main():
	choice = int(input('\n#################\nMenu: \n1. Music \n2. History \n3. Design \n4. Exit \n\nPlease enter your choice: '))
	wait()
	
	if choice == 1:
		print('You chose Music.')
	
	elif choice == 2:
		print('You chose History.')
	
	elif choice == 3:
		print('You chose Design.')
	
	elif choice == 4:
		print('Are you sure? y/n')
		CloseProg()
		wait()	
		
	else:
	    print('Invalid choice')
	    wait()
	    main()
	
	CloseProg(UsersDecision())
	wait()
	main()
	
main()