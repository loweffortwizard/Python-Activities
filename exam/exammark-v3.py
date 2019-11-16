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



    

