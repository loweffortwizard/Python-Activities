'''
	this program will be a text adventure game.
		it will bring up a question to the user(after some dialog).
		program will change results based on users choice.
		user can win and loss.
		user will be asked a few questions in total.
	implementation 3 - adding iteration into program, for looping
'''

import time
#used to add time into program, for waiting.

#global vars
bullet = 3

'''
    iteration for player, dependent on if var complete is == 1 to replay,
    else player has died, var complete == 0, game replay
'''

#var playeralive has value of True
playeralive = True

#while var playeralive is True
while playeralive:
    #var complete has value of function call - game
    complete = game()
    if complete == 1:
        #if var complete == 1, do this
        playeralive = input("Would you like to play again? [y/n]: ")
        space()
        space()
        space()
        if playeralive in ["y", "Y", "Yes", "YES", "yes"]:
            playeralive

        else:
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
            break
			
#functions
def space():
    print("")

def time():
    time.sleep(2)

def game():

        #printing game title screen
        print("===========================")
        print("=== Welcome to Rapture! ===")
        print("===========================")
        time()
        space()

        print("===========================")
        print("==== No Gods, No Kings ====")
        print("===========================")
        time()
        space()

        print("===========================")
        print("======= Only Trains =======")
        print("===========================")
        time()
        space()

        #printing background on game
        print("The year is 1960, while flying over the Atlantic ocean, Jake blacks out and awakens to discover that he is the sole survivor of a plane crash.")
        time()
        space()
        print("Amidst the wreckage of his plane Jack spots and swims to a lighthouse and boards a Bathysphere that takes Jake deep within the ocean and into Rapture.")
        time()
        space()
        print("Originally conceived as a utopia where a man would be entitled to all that he made without the interference of parasites by idealistic billionaire mogul Andrew Ryan. ")
        time()
        space()
        print("Rapture has since decayed and festered from the infectious effects of civil war and anarchy.")
        time()
        space()
        print("Brought about by the very ideals it citizens and its leader embrace. Aided by a sympathetic smuggler and a rogue geneticist.") 
        time()
        space()
        print("Jack salvages gene altering chemicals transforming himself into a superhuman.")
        time()
        space()
        print("Jake now must use his newfound powers and abilities as well as an arsenal of weapons to fend off the vicious hordes of psychotic mutants.")
        time()
        space()
        print("As well as security robots and armored supersoldiers that resulted from Raptures unrest while given the choice to either rescue or lethally harvest the genetic material from Rapture's only citizens with a chance: the 10 year old Little Sisters. ")
        time()
        space()
        print("As Jack wanders through the condemning atmosphere of rapture, he treads towards a secret that could shatter all that he has known forever.")
        time()
        space()

        #asking begin game question
        userinput1 = str(input("Would you kindly begin? [y/n]: "))
        time()
        space()

        #begin - y
        if userinput1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
            print("Thanks, now walk down that corridor to your left Jake.")
            time()
            space()

        #begin - n
        else:
            print("Oh dear Jake, looks like you were not as valuable as I first thought.")
            time()
            space()
            print("*The room Jake stands in begins to sink as glass shatters and the water rises.")
            time()
            space()
            print("Jake does not survive the fall and slowly drowns, with nothing but his clothing and a lone picture of his mother...")
            time()
            space()
            complete = 0
            return complete

        #stage 1 of game
        print("Jake does as the voice says and walks down the corridor.")
        time()
        space()

        print("Jake walks for 2 minites before he comes across a strange creature.")
        time()
        space()

        print("The creature appears to be female, white, tall, with some kind of weapon in her hand.")
        time()
        space()

        print("Jake looks to his left and sees a gun with 3 bullets.")
        time()
        space()

        print("The voice says to Jake to pick up the gun.")
        time()
        space()

        #asking gun pick question of the game
        userinput2 = str(input("Would you kindly pick up the gun? [y/n]: "))
        time()
        space()

        #gun - y
        if userinput2 in ["y", "Y", "Yes", "YES", "yes"]:
            print("Jake has picked up the weapon.")
            time()
            gun = 1
            space()

        #gun - n
        else:
            print("Jake does not pick up the weapon")
            time()
            gun = 0
            space()

        #stage 2 - battle
        print("The creature looks right at Jake, looking like its preparing to attack.")
        time()
        space()

        print("Jake stands his ground but the creature begins to run towards him.")
        time()
        space()

        #if player picked up gun
        if(gun == 1):
                print("The voice says to shoot the creature.")
                time()
                space()
                #asking if player will shoot
                userinput3 = str(input("Would you kindly shoot the creature? [y/n]"))
                time()
                space()
                if userinput3 in ["y", "Y", "Yes", "YES", "yes"]:
                        #if player puts yes, shoot and take one away from GB bullet
                        print("Jake uses one of his bullets and kills the creature.")
                        time()
                        space()
                        bullet = 2
                        complete = 1
                        return complete
                else:
                        #else player dies
                        print("Jake did not shoot the creature, sadly the creature does not stop and swipes at Jake, taking his head off clean.")
                        time()
                        space()
                        print("Jakes story has ended before it begun, nice going...")
                        time()
                        space()
                        complete = 0
                        return complete

        else:
        #else player does not have gun, player gets options but will die for both
                print("Jake did not pick up the gun and so has no defence against the creature.")
                time()
                space()
                print("The voice tells Jake to run back and hope for the best.")
                time()
                space()
                #asking if player will run
                userinput4 = str(input("Would you kindly run away from the creature? [y/n]"))
                time()
                space()
                if userinput4 in ["y", "Y", "Yes", "YES", "yes"]:
                        #if player says yes, player dies nicely
                        print("Jake runs back but falls down a crack in the floor, falling down a dies from the fall.")
                        time()
                        space()
                        print("What a cluts")
                        time()
                        space()
                        complete = 0
                        return complete
                else:
                        #else player dies horribily
                        print("Jake is impailed by the creatures weapon, and left stuck to the floor as he is eaten alive by the creature.")
                        time()
                        space()
                        print("Looks like Jake is usful for something after all.")
                        time()
                        space()
                        complete = 0
                        return complete

'''
	while loop moved to top
'''
									
'''
    end of program
'''
