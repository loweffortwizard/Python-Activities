'''
	the following functions are commonly used among many of my programs.
	having them stored externally and simply importing the functions (and calling) 
	when needed was more effitient than having to write the same code in each new program. 
'''
#importing libs.
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