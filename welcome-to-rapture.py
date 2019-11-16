'''
	this program will be a text adventure game.
		it will bring up a question to the user(after some dialog).
		program will change results based on users choice.
		user can win and loss.
		user will be asked a few questions in total.
	implementation 3 - adding iteration into program, for looping
'''

#import lib
import time #used to add time into program, for waiting.

#global var
global bullet #used to determine amount of bullets left

#defining function
def space():#declaring function to print a new line
    print("") #print out a blank line

def game(): #declaring function to run game
    score = 0 # var score has value of 0
    
    #printing game title screen
    print("===========================")
    print("=== Welcome to Rapture! ===")
    print("===========================")
    time.sleep(2) #pausing for 2 seconds
    space() # run function

    print("===========================")
    print("==== No Gods, No Kings ====")
    print("===========================")
    time.sleep(2) #pausing for 2 seconds
    space() #run function

    print("===========================")
    print("======= Only Trains =======")
    print("===========================")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    
    #printing background on game
    print("The year is 1960, while flying over the Atlantic ocean, Jake blacks out and awakens to discover that he is the sole survivor of a plane crash.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    print("Amidst the wreckage of his plane Jack spots and swims to a lighthouse and boards a Bathysphere that takes Jake deep within the ocean and into Rapture.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    print("Originally conceived as a utopia where a man would be entitled to all that he made without the interference of parasites by idealistic billionaire mogul Andrew Ryan. ")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    print("Rapture has since decayed and festered from the infectious effects of civil war and anarchy.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    print("Brought about by the very ideals it citizens and its leader embrace. Aided by a sympathetic smuggler and a rogue geneticist.") 
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    print("Jack salvages gene altering chemicals transforming himself into a superhuman.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    print("Jake now must use his newfound powers and abilities as well as an arsenal of weapons to fend off the vicious hordes of psychotic mutants.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    print("As well as security robots and armored supersoldiers that resulted from Raptures unrest while given the choice to either rescue or lethally harvest the genetic material from Rapture's only citizens with a chance: the 10 year old Little Sisters. ")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    print("As Jack wanders through the condemning atmosphere of rapture, he treads towards a secret that could shatter all that he has known forever.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
    
    #asking begin game question
    userinput1 = str(input("Would you kindly begin? [y/n]: ")) #var userinput1 has value of input
    time.sleep(2) #pausing for 2 seconds
    space() #run function

    #begin - y
    if userinput1 in ['y', 'Y', 'Yes', 'YES', 'yes']: #if input was equal to criteria - do this
        print("Thanks, now walk down that corridor to your left Jake.") # print this
        time.sleep(2) #pausing for 2 seconds
        space() #run function
        score = score + 1 # var score has value of self + 1

    #begin - n
    else: # else input did not meet criteria - do this
        print("Oh dear Jake, looks like you were not as valuable as I first thought.")
        time.sleep(2) #pausing for 2 seconds
        space() #run function
        print("*The room Jake stands in begins to sink as glass shatters and the water rises.")
        time.sleep(2) #pausing for 2 seconds
        space() #run function
        print("Jake does not survive the fall and slowly drowns, with nothing but his clothing and a lone picture of his mother...")
        time.sleep(2) #pausing for 2 seconds
        space() #run function
        score = score - 1 #score has value of self - 1
        complete = 0 #var complete is equal to 0
        return complete, score # return var complete and score
        
    #stage 1 of game
    print("Jake does as the voice says and walks down the corridor.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function

    print("Jake walks for 2 minites before he comes across a strange creature.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function

    print("The creature appears to be female, white, tall, with some kind of weapon in her hand.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function
            
    print("Jake looks to his left and sees a gun with 3 bullets.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function

    print("The voice says to Jake to pick up the gun.")
    time.sleep(2) #pausing for 2 seconds
    space() #run function

    #asking gun pick question of the game
    userinput2 = str(input("Would you kindly pick up the gun? [y/n]: ")) #userinput2 has value of input
    time.sleep(2) #pausing for 2 seconds
    space() #run function

    #gun - y
    if userinput2 in ["y", "Y", "Yes", "YES", "yes"]: # if input does not match criteria - do this
        print("Jake has picked up the weapon.")
        time.sleep(2) #pausing for 2 seconds
        gun = 1 #var gun equal to 1
        space() #run function
        score = score + 1 #score equal self + 1

    #gun - n
    else:
        print("Jake does not pick up the weapon")
        time.sleep(2)
        gun = 0
        space()
        score = score - 1

    #stage 2 - battle
    print("The creature looks right at Jake, looking like its preparing to attack.")
    time.sleep(2)
    space()

    print("Jake stands his ground but the creature begins to run towards him.")
    time.sleep(2)
    space()

    #if player picked up gun
    if(gun == 1):
        print("The voice says to shoot the creature.")
        time.sleep(2)
        space()
        #asking if player will shoot
        userinput3 = str(input("Would you kindly shoot the creature? [y/n]: "))
        time.sleep(2)
        space()
        if userinput3 in ["y", "Y", "Yes", "YES", "yes"]:
            #if player puts yes, shoot and take one away from GB bullet
            print("Jake uses one of his bullets and kills the creature.")
            time.sleep(2)
            space()
            bullet = 2
            score = score + 1
            complete = 1
            return complete, score
        else:
            #else player dies
            print("Jake did not shoot the creature, sadly the creature does not stop and swipes at Jake, taking his head off clean.")
            time.sleep(2)
            space()
            print("Jakes story has ended before it begun, nice going...")
            time.sleep(2)
            space()
            score = score - 1
            complete = 0
            return complete, score

    else:
    #else player does not have gun, player gets options but will die for both
        print("Jake did not pick up the gun and so has no defence against the creature.")
        time.sleep(2)
        space()
        print("The voice tells Jake to run back and hope for the best.")
        time.sleep(2)
        space()
        #asking if player will run
        userinput4 = str(input("Would you kindly run away from the creature? [y/n]: "))
        time.sleep(2)
        space()
        if userinput4 in ["y", "Y", "Yes", "YES", "yes"]:
            #if player says yes, player dies nicely
            print("Jake runs back but falls down a crack in the floor, falling down a dies from the fall.")
            time.sleep(2)
            space()
            print("What a cluts")
            time.sleep(2)
            space()
            score = score - 1
            complete = 0
            return complete, score
        else:
            #else player dies horribily
            print("Jake is impailed by the creatures weapon, and left stuck to the floor as he is eaten alive by the creature.")
            time.sleep(2)
            space()
            print("Looks like Jake is usful for something after all.")
            time.sleep(2)
            space()
            score = score - 1
            complete = 0
            return complete, score

#var playeralive has value of True
playeralive = True

#while var playeralive is True
while playeralive:
    #var complete has value of function call - game
    complete, score = game()
    if complete == 1:
        #if var complete == 1, do this
        playeralive = input("Would you like to play again? [y/n]: ")
        space()
        space()
        space()
        if playeralive in ["y", "Y", "Yes", "YES", "yes"]:
            playeralive

        else:
            file = open("score.txt","a") #open score text file
            file.write(str(score))
            file.close()
            break

    else:
        #if complete == 0, do this
        playeralive = input("You have died! Would you like to play again? [y/n]: ")
        space()
        space()
        space()
        if playeralive in ["y", "Y", "Yes", "YES", "yes"]:
            playeralive

        else:
            file = open("score.txt","a") #open score text file
            file.write(str(score))
            file.close()
            break

'''
    end of program
'''
