'''
	program will work out the current time, and time of parking.
	it will also have a charge based on 2, 4 and 12 hours. 
'''
#importing libs.
import time
import sys

#importing external lib
import basicfunction

def main():
    basicfunction.wait()
    #getting current time. 
    ticket = time.time()
    ticketformat = time.ctime(ticket)

    #getting time form user.
    charge = int(input('\nInput hours parking required (2, 4 or 12): '))
    basicfunction.wait()

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
    basicfunction.wait()

    #print expiration. 
    print('Expires on: ', expiredateformat)
    basicfunction.wait()

    #######determining charge for ticket. 
    #if charge = 2, print cost and option to end.
    if (charge == 2):
            print('Charge: £3.50')
            basicfunction.CloseProg(basicfunction.UsersDecision())
            basicfunction.wait()
            
    #else if charge = 4, print cost and option to end.
    elif (charge == 4):
            print('Charge: £5')
            basicfunction.CloseProg(basicfunction.UsersDecision())
            basicfunction.wait()

    #else if charge = 12, print cost and option to end.
    elif (charge == 12):
            print('Charge: £10')
            basicfunction.CloseProg(basicfunction.UsersDecision())
            basicfunction.wait()

    #if none of the above, print errror and option to end.
    else:
            print('Error, please try again. ')
            basicfunction.CloseProg(basicfunction.UsersDecision())
            basicfunction.wait()
    main()
#calling defined function main() to start prog.
main()