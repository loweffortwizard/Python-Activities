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
        sys.exit()
    else:
        main()

#getting desision for closing prog.
def UsersDecision():
    userChoice = str(input("If you wish to use again, press \"Y\": "))
    return userChoice

def main():
    wait()
    #getting current time. 
    ticket = time.time()
    ticketformat = time.ctime(ticket)

    #getting time form user.
    charge = int(input('\nInput hours parking required (2, 4 or 12): '))
    wait()

    #var userinput = charge times 1*60*60 (Getting hours)
    userinput = 1*60*60 * charge

    #converting userinput to current time and saving in var userinputformat
    userinputformat = time.ctime(userinput)

    #var expiredate = int converted userinput add int converted ticket. 
    expiredate = int(userinput) + int(ticket)

    #formatting expiredate to current time - saving in var expiredateformat
    expiredateformat = time.ctime(expiredate)
    
    #printing time now.
    print('Time now: ', ticketformat)
    wait()

    #print expiration. 
    print('Expires on: ', expiredateformat)
    wait()
    
    #######determining charge for ticket. 
    #if charge = 2, print cost and option to end.
    if (charge == 2):
        print('Charge: £3.50')
        CloseProg(UsersDecision())
        wait()

    #else if charge = 4, print cost and option to end.
    elif (charge == 4):
        print('Charge: £5')
        CloseProg(UsersDecision())
        wait()

    #else if charge = 12, print cost and option to end.
    elif (charge == 12):
        print('Charge: £10')
        CloseProg(UsersDecision())
        wait()

    #if none of the above, print errror and option to end.
    else:
        print('Error, please try again. ')
        CloseProg(UsersDecision())
        wait()

    ## Above could be turned to switches. ##

#calling defined function main() to start prog.
main()