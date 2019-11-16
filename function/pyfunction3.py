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
    this prog will calc the square root
'''
print("Welcome")
#print above.
wait()
#calling def

userInput1 = math.sqrt(float(input("Enter number: ")))
#getting user input, making it a float, converting it to its root, saving in var userInput1
wait()
#calling def

print(userInput1)
wait()

print("End")
wait()

'''
    this prog will calc the square
'''
print("Welcome")
#print above.
wait()
#calling def

userInput2 = int(input("Enter number: "))
#getting user input, making it a float, converting it to its root, saving in var userInput1
wait()
#calling def

total = userInput2 ^ userInput2
wait()
#calling def

print(userInput2, " x ", userInput2, "is ", total)
wait()
#calling def

print("End")
