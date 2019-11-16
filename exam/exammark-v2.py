import time
import sys

def wait():
    time.sleep(1)

#def to close prog
def CloseProg(txt):
    txt.lower()
    if(txt!='y'):
        sys.exit()

#prog to promp decision to end
def UsersDecision():
    userChoice = str(input("If you wish to use again, press \"Y\": "))
    return userChoice

'''
	detracked 2 indents in python IDLE.
'''
def main():
    while(True):
        #getting input
        examMark = int(input("Please enter your exam mark: "))
        wait()

        #working out grade
        if (examMark >=0) and (examMark <= 19):
             #U
            print("You have earned a grade U")
            CloseProg(UsersDecision())
            wait()
                        
                        #E
        elif(examMark >= 20) and (examMark <= 29):
            print("You have earned a grade E")
            CloseProg(UsersDecision())
            wait()
                            
                            #D
        elif(examMark >= 30) and (examMark <= 46):
            print("You have earned a grade D")
            CloseProg(UsersDecision())
            wait()
                            
                            #C
        elif(examMark >= 46) and (examMark <= 60):
            print("You have earned a grade C")
            CloseProg(UsersDecision())
            wait()
                        
                            #B
        elif(examMark >= 60) and (examMark <= 76):
            print("You have earned a grade B")
            CloseProg(UsersDecision())
            wait()
                        
                        #A
        elif(examMark >= 75) and (examMark <= 90):
            print("You have earned a grade A")
            CloseProg(UsersDecision())
            wait()
                        
                    #A*
        elif(examMark > 90):
            print("You have earned a grade A*")
            CloseProg(UsersDecision())
            wait()
                        
        else:
            print("Error, please try again.")
            CloseProg(UsersDecision())
            main()
main()
print("End.")
'''
import sys

def CloseProg(txt):
    txt.lower()
    if(txt!='y'):
        sys.exit()

def UsersDecision():
    userChoice = str(input("If you wish to use again, press \"Y\": "))
    return userChoice
        
while(True):
    examMark = int(input("Please enter your exam mark: "))

    if (examMark >=0) and (examMark <= 19):
        print("You have earned a grade U")
        CloseProg(UsersDecision())
    elif (examMark >=20) and (examMark <= 29):
        print("You have earned a grade E")
        CloseProg(UsersDecision())
    elif (examMark >=30) and (examMark <= 45):
        print("You have earned a grade D")
        CloseProg(UsersDecision())
    elif (examMark >=46) and (examMark <= 59):
        print("You have earned a grade C")
        CloseProg(UsersDecision())
    elif (examMark >=60) and (examMark <= 75):
        print("You have earned a grade B")
        CloseProg(UsersDecision())
    elif (examMark >=76) and (examMark <= 89):
        print("You have earned a grade A")
        CloseProg(UsersDecision())
    elif (examMark >=90) and (examMark <= 100):
        print("You have earned a grade A*")
        CloseProg(UsersDecision())
    else:
        print("You did not enter a valid exam mark.")
        CloseProg(UsersDecision())
'''
