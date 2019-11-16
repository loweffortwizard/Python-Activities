'''
During the in-class presentation you were also shown the example
that used nested-if statements to display an appropriate message as
to whether the user the likes the colour blue and if they prefer
reading or going to the cinema. On Moodle you will find the starting
block of code, you need to complete the program.
The outcomes for the program are:
•	Favourite colour is blue and prefers reading.
•	Favourite colour is blue and prefers the cinema
•	Favourite colour is not blue and prefers reading
•	Favourite colour is not blue and prefers cinema
•	There should be a fall-back message for the occasions when incorrect answers are given.

'''

import time
def wait():
    time.sleep(1)

def main():
    faveColour = input("Please enter your favourite colour: ").lower()
    wait()
    readingOrCinema = input("Do you prefer reading or the cinema: ").lower()
    wait()

    if (faveColour == "blue") or (faveColour == "Blue") :
        if (readingOrCinema == "reading") or (readingOrCinema == "Reading"):
            print("Your favourite colour is blue and you prefer to read")
            wait()
        elif (readingOrCinema == "cinema") or (readingOrCinema == "Cinema"):
            print("Your favourite colour is blue and you prefer the cinema")
            wait()
        else:
            print("You did not type in reading or cinema.\nProgram is case-sensitive.")
            wait()
            main()
main()
print("End")
