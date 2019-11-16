#importing libs
import time
import sys

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
	currentTime = time.time()
	currentTimeFormat = time.ctime(currentTime)

	oneHourInSec = 1*60*60
	timeInOneHour = currentTime + oneHourInSec
	timeInOneHourFormat = time.ctime(timeInOneHour)
	
	print('time.time() '), currentTime)
	print('time.ctime() '), currentTimeFormat)
	print('time.ctime(timeInOneHour) '), timeInOneHourFormat)

	CloseProg(UsersDecision())
	wait()
	
main()