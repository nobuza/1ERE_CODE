from numpy import Infinity
import pyfiglet

developerMode = False
list = [5, 4, 2, 1, 0, 6]

############################################
####SMALLEST VALUE PICKER USING MIN()#####
########################################
def smallestValueInListIndexIdentifierWithMin(vallist:list):
    return vallist.index(max(vallist))
'''
smallestValueInListIndex = smallestValueInListIndexIdentifierWithMin(list)
print('The index corresponding to the smallest value is: ', smallestValueInListIndex)
'''
############################################
####SMALLEST VALUE PICKER USING LOOP#######
#########################################
def smallestValueInListIndexIdentifierWithLoop(vallist:list):
    smallestValueCandidate = -Infinity
    for i in vallist:
        if i > smallestValueCandidate:
            smallestValueCandidate = i
    return list.index(smallestValueCandidate)


#+++++++++++++++++++++++++++++++++MENU MENU MENU MENU+++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++MENU MENU MENU MENU+++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++MENU MENU MENU MENU+++++++++++++++++++++++++++++++++#
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

def functionToExecuteSelecter(): # used in menu, asks the user what function he wants to execute
    isSet = False
    while isSet != True:
        try:
            userInput = (input(">"))
            if userInput == "1":
                return "1"
            elif userInput == "2":
                return "2"
        except:
            print("Cannot proceed entered key. Please respect the rule.")

def menu():
    ascii_banner = pyfiglet.figlet_format("SMALLEST VALUE IN LIST FUNCTIONS")
    print(ascii_banner)
    global developerMode
    developerMode = developperModeQuestion()
    if developerMode:
        print("********\nDBG_LOCATION: menu()\nValue of Developper Mode: ", developerMode, "\n**********")
    print("----------------------")
    print("Bienvenue. Selectionnez la fonction à executer:")
    print("----------------------")
    print("1: SMALLEST VALUE PICKER USING MIN()")
    print("2: SMALLEST VALUE PICKER USING LOOP")
    selectedFunction = functionToExecuteSelecter()
    if selectedFunction == "1":
        result = smallestValueInListIndexIdentifierWithMin(list)
        print("L'index de la plus grande valeur (avec max() en méthode) est: ", result)
    elif selectedFunction == "2":
        result = smallestValueInListIndexIdentifierWithLoop(list)
        print("L'index de la plus grande valeur en utilisant une boucle, est: ", result)


#++++++++++++++++++++++++++++++++++MENU END MENU END++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++MENU END MENU END++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++MENU END MENU END++++++++++++++++++++++++++++++++++#

menu()