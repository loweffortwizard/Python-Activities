'''
from file - PyFunctions.py

def squareNumber(num):
    answer = num * num
    return answer

def multiply(num1, num2):
    answer = num1 * num2
    return answer

'''

#importing expernal functions. 
import PyFunctions

#getting first number form user. 
num1 = int(input("Please enter the number you wish to multiply: "))

#getting second number form user. 
num2 = int(input("Please enter the value you wish to multily by: "))

#getting result from inputs with use of external functions. 
answer = PyFunctions.multiply(num1, num2)

#printing result of sum. 
print (str(num1) + " x " + str(num2) + " = " + str(answer) )