'''
prog will calculate area of a square,
based on user input
'''

#importing libs
import time
import sys

#wait def
def wait():
	time.sleep(1)

#closing prog
def endprog(txt):
    txt.lower()
    if(txt!='y'):
        sys.exit()

#closing prog option
def userdecision():
    userchoice = str(input("If you wish to use again, press \"Y\": "))
    return userchoice

#while true, run prog
while(True):
	inputside1 = int(input("Enter length: "))
	#get input from user, save as int in var inputside1
	wait()
	#wait 1 second
	print(inputside1)
	#print above
	
	inputside2 = int(input("Enter width: "))
	#get input from user, save as int in var inputside2
        wait()
	#wait 1 second
	print(inputside2)
	#print above
	
	area = inputside1 * inputside2
	#var area has value of inputside1 X inputside2
	
	print(area)
	#print area
	wait()
	#wait 1 second
	endprog(userdecision())
	#prompt user decision
	
#end of prog
