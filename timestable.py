import time
import sys

def Time():
    time.sleep(0.5)

def Exit(txt):
    if(Decision.choose!='y'):
        sys.exit()
    else:
        Main()

def Decision():
    Decision.choose = str(input("Do you want to exit? "))
    return Decision.choose

def Main():
    usernumber = int(input("Enter Number: "))
    Time()
    
    print ("you entered ", usernumber)
    
    for value in range(0, 11):
        Time()
        print(usernumber,'x',value,'=',usernumber * value)

    Exit(Decision())

Main()
