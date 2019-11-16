import time
# importing use of time.

import math
#importing math to use math.sqrt

### creating function to wait for 1 second. ###
def wait():
    time.sleep(1)
    # waiting for 1 second
    #end of def

'''
    this prog will calc the square
'''
print("Welcome")
#print above.
wait()
#calling def

userInput1 = int(input("Enter exponent number: "))
#getting user input, making it a float, converting it to its root, saving in var userInput1
wait()
#calling def

userInput2 = int(input("Enter time number: "))
#getting user input, making it a float, converting it to its root, saving in var userInput2
wait()
#calling def

total = userInput1 ** userInput2
wait()
#calling def

print(userInput1, " x ", userInput2, "is ", total)
wait()
#calling def

print("End")