'''
V0.1:
- Developper mode
- Plateau generator
- Game engine, asks for coos and does the comparison to the list
- Doesn't do anything if there is a bomb yet, or warns if there is one nearby.
Just pure compare and a message "No bombs encountered." if there wasn't, to make the difference.
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
Soit une grille de jeu sous forme de liste de liste
exemple: [[0, 0, 0, 0, *], [0, *, 0, 0, 0], [0, 0, 0, 0, 0], [0, *, 0, *, 0], [0, 0, *, 0, 0]]
- les zeros ne font rien
- les * mettent fin aux jeu

Ecrire l'algorithme, en francais ou en Python 
qui regarde si des coordonnées utilisateur saisies sous forme de chaine de caractére avec le séparateur "," tombent sur une mine ou sur une null. 
exemple: 2,4

Comment utiliser la saisie utilisateur ? (Notion vu en TP) Comment savoir si c'est une bombe ou une case safe ?
'''

'''
PLAN DE DEV:
1. Dev un randomizer de plateau
2. Dev le système de jeu
'''

########################################
#### RANDOMIZER V1.0###################
######################################
'''
PLAN DU RANDOMIZER:
1. lists container plateau = []
1. single function generating random lists and append to plateau = []:
    a. list container temp = []
    b. creating by a loop, one by one characters, with a random : it uses randomint() and if the result is 0, it's zero, else if it's one, it's a *
'''

def plateauGenerator():
    generatedList = []
    for i in range(0, 5):
        randomNumber = randint(0,1)
        if randomNumber == 1:
            generatedList.append("*")
        else:
            generatedList.append("0")
    return generatedList

#plateau = [plateauGenerator()]*5
#print(plateau)

########################################
#### GAME ENGINE V1.1##################
######################################
'''
PLAN DU RANDOMIZER:
 - loop 1=1 till the user selects "quit" in the gameover menu
 - menu() that takes in the developper mode activation, the difficulty, calls external defs to get those values
 - S
'''
# to increment for each new difficulty level coded in
difficultyLevels = 1
plateau = []
numberOfTiles = 0
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

def menu():
    print("        ,--.!,")
    print("     __/   -*-")
    print("   ,d08b.  '|`")
    print("   0088MM   ")
    print("   `9MMP' ")

    ascii_banner = pyfiglet.figlet_format("DEMINE-MOI")
    print(ascii_banner)
    print("Bienvenue. Selectionnez votre niveau de difficulté:")
    print("----------------------")
    if difficultyLevels == 1:
        print("1: Normal")
    selectedDifficulty = input(">")

    global developerMode
    developerMode = developperModeQuestion()
    if developerMode:
        print("********\nDBG_LOCATION: menu()\nValue of Developper Mode: ", developerMode, "\n**********")
    print("----------------------")

    if selectedDifficulty == "1":
        print("Starting new game in normal mode...")
        time.sleep(1)
        gameWithNormalGamemode()

def askForCoordinates():
    print("Enter land coordinates separated by a comma.\nThe format is: 'HORIZONTAL_LINE_NUMBER, INDEX_OF_THE_NUMBER_IN_THE_LINE'.\nExample: 0, 4")
    try:
        coordinatesGivenByUser = input(">")
        parsedUserCoordinates = [int(s) for s in coordinatesGivenByUser.split(',')]
        return parsedUserCoordinates
    except:
        print("The coordinates were mistyped, the system cannot read these.")
        askForCoordinates()

def gameWithNormalGamemode():
    print("Developper Mode set to:", developerMode)
    numberOfTiles = 25
    print("Selected.")
    print("Creating map...")
    time.sleep(0.5)
    plateau = [plateauGenerator()]*5
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

menu()

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

while(1 == 1):
    restart()