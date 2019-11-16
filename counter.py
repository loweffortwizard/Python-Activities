'''
	making a countdown clock. 
	from 10 to 0.
'''

#importing libs
import time
import sys

#main function
def main():

	#var counter = 0
	counter = 0
	
	#while var counter is less than 10, do this.
	while(counter < 10):
	
		#counter = itself - 1
		counter = counter + 1
		#print var
		print(counter)
		time.sleep(1)
	'''
		for(int counter = 0; counter > 10; counter++)
		print(counter)
		time.sleep(1)	
	'''
main()
#end of prog