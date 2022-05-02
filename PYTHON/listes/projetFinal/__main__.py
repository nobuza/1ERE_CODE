'''
V0.1:
'''

####################################################################
############ LIBRARY INSTALLER ####################################
import os
os.system("pip install pyfiglet")
####################################################################
'''
Pyfliget is used to translate text in ascii art, for the menu of the deminer.
Looks are a matter.
'''

import time
import pyfiglet
from random import randint

'''
PLAN DE DEV:
1. Système d'import de deck, menu
2. Menu jeu:
    - vérifie la selection d'un deck, sinon demande de faire auparavant
    - random pull card
    - cmp answer by numbers proposed
'''


openedDeck = []

def deckNameQuestion():
        userInput = (input("Please enter the deck's file name with the extension, which must be a .txt\n>"))
        return userInput

########################################
#### DECKS MENU V1.0###################
######################################
def decksMenu():
    loopedCounterDueToError = 1 # contains the number of times the user has crashed the system by a mistyping of the deck's name and extension for example.
    importedDeck = []
    while True:
        deckName = input("Please enter the deck's file name with the extension, which must be a .txt\n>")
        try:
            with open(deckName, 'r') as deck : 
                head = deck.readline()
                head = head.rstrip('\n')
                value = head                                  
                head = head.split(';')                         
                while value :                                   
                    value = deck.readline().rstrip('\n')         
                    if value :                                  
                        columns = value.split(';')              
                        importedDeck.append(columns)                  
        except:
            if loopedCounterDueToError == 3:
                print("The deck could not be opened. Please refer to the rule given, or to the user assistance manual pt.2 index 1.\nThird time the program crashes. Quitting...")
                exit()
            else:
                print("The deck could not be opened. Please refer to the rule given, or to the user assistance manual pt.2 index 1.")
                loopedCounterDueToError = loopedCounterDueToError + 1

#plateau = [plateauGenerator()]*5
#print(plateau)

# to increment for each new difficulty level coded in
developerMode = False

def developperModeQuestion():
    isSet = False
    while isSet != True:
        try:
            userInput = (input("Voulez vous démarrer en mode développeur? 'y' pour oui, 'n' pour non\n>"))
            if userInput == "y":
                valueOfDevmod = True
                isSet = True
            elif userInput == "n":
                valueOfDevmod = False
                isSet = True
        except:
            print("Cannot proceed entered key. Please respect the rule.")
    #print("*******\nDBG_LOCATION: developerModeQuestion()\nValue of Developper Mode that is returned: ", valueOfDevmod, "\n********")
    return(valueOfDevmod)



#+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+########################################+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#
                                                ######### GAME ENGINE V0.4###########
#+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+########################################+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#

def menu():
    print('░░░░██░░████████░░██░░░░░░░░░░░░░░░░░░░░░░░░ ')
    print('░░██▒▒██▒▒▒▒▒▒▒▒██▒▒██░░░░░░░░░░░░░░░░░░░░░░ ')
    print('░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░ ')
    print('░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░ ')
    print('██▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░ ')
    print('██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░░░░░░░░░░░░░ ')
    print('██▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████░░ ')
    print('██▒▒██▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██ ')
    print('██▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████░░ ')
    print('██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░ ') 
    print('██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ')

    ascii_banner = pyfiglet.figlet_format("Mettaton's Quizz!")
    print(ascii_banner)
    print("Bienvenue. Aucun niveau de difficulté n'est disponible pour cette version. Ajout dans ne prochaine update!")

    global developerMode
    developerMode = developperModeQuestion()
    if developerMode:
        print("********\nDBG_LOCATION: menu()\nValue of Developper Mode: ", developerMode, "\n**********")
    print("----------------------")

def askForCoordinates():
    print("Enter land coordinates separated by a comma.\nThe format is: 'HORIZONTAL_LINE_NUMBER, INDEX_OF_THE_NUMBER_IN_THE_LINE'.\nExample: 0, 4")
    try:
        coordinatesGivenByUser = input(">")
        parsedUserCoordinates = [int(s) for s in coordinatesGivenByUser.split(',')]
        return parsedUserCoordinates
    except:
        print("The answer was misstyped, the system cannot read these.")
        askForCoordinates()

def gameWithNormalGamemode():
    print("Developper Mode set to:", developerMode)
    numberOfTiles = 25
    print("Selected.")
    print("Creating map...")
    time.sleep(0.5)
    print("Map generated. GAME BEGINS!")
    for i in range(0, numberOfTiles):
        parsedUserCoordinates = askForCoordinates()
        if developerMode:
            print("******************START DEV OUTPUT***************\n- parsedUserCoordinates= ",parsedUserCoordinates,"\n- plateau= ",plateau, "\n********************END DEV OUTPUT****************")
        # first index is for the horizontal line selected, second for the number selected in this line.
        if plateau[parsedUserCoordinates[0]][parsedUserCoordinates[1]] == "0":
            print("No bombs encountered.")
        else:
            ascii_kaboom = pyfiglet.figlet_format("KABOOM!")
            print(ascii_kaboom)
            break

def restart():
    replayOrQuitKey = replayOrQuit()
    if replayOrQuitKey == "r":
        menu()
    elif replayOrQuitKey == "q":
        exit()

def replayOrQuit():
    isSet = False
    while isSet != True:
        try:
            userInput = (input("-+-+-+-+-+-+-+-+-+-+-+-+-MENU-+-+-+-+-+-+-+-+-+-+-+-+-\n - [r] : re-play\n - [q] : quit program\n-+-+-+-+-+-+-+-+-+-+-+-+-MENU-+-+-+-+-+-+-+-+-+-+-+-+-\n>"))
            if userInput == "r":
                return userInput
            elif userInput == "q":
                return userInput
        except:
            print("Cannot proceed entered key. Please respect the rule.")
    if developerMode:
        print("*******\nDBG_LOCATION: replayOrQuit()\nValue of userInput that is returned: ", userInput, "\n********")


'''
# UNCOMMENT WHEN DEVELOPPING IS DONE
while(1 == 1):
    restart()
'''


########################################
########### STARTER ###################
menu()
######################################
print("------------------------------------------------------")
print("Nothing to see here!")
print('░░░░██░░████████░░██░░░░░░░░░░░░░░░░░░░░░░░░ ')
print('░░██▒▒██▒▒▒▒▒▒▒▒██▒▒██░░░░░░░░░░░░░░░░░░░░░░ ')
print('░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░ ')
print('░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░ ')
print('██▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░ ')
print('██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░░░░░░░░░░░░░ ')
print('██▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████░░ ')
print('██▒▒██▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██ ')
print('██▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████░░ ')
print('██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░ ') 
print('██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ')
print("Reached end of program.\nExiting...")
print("------------------------------------------------------")
