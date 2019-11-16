'''
prog will calculate area of a triangle,
based on user input

https://stackoverflow.com/questions/14607890/area-of-a-triangle-python-27
https://www.programiz.com/python-programming/examples/area-triangle
'''

#importing libs
import time
import sys
import math

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
    inputside1 = int(input("Enter side 1: "))
    #get input from user, save as int in var inputside1
    wait()
    #wait 1 second
    print(inputside1)
    #print above
    wait()
    #wait 1 second
    
    inputside2 = int(input("Enter side 2: "))
    #get input from user, save as int in var inputside2
    wait()
    #wait 1 second
    print(inputside2)
    #print above
    wait()
    #wait 1 second

    inputside3 = int(input("Enter side 3: "))
    #get input from user, save as int in var inputside2
    wait()
    #wait 1 second
    print(inputside3)
    #print above
    wait()
    #wait 1 second
    
    half = (inputside1 + inputside2 + inputside3) / 2
    #var half = all inputs together then half by 2

    area = (half*(half - inputside1)*(half - inputside2)*(half - inputside3))**0.5
    #var area is equal to the power of half - inputs times each other, times 0.5
    print(area)
    #print area
    wait()
    #wait 1 second
    endprog(userdecision())
    #prompt user decision
	
#end of prog