# Exercice 1
#N01
def printCounterInRange():
    N = 5
    counter = 0
    for counter in range(counter, N, 1):
        print(counter)
    
# N02 Ecrivez un code qui affiche les nombres 1, 3, 5, 7 et 9 de deux manières différentes
def showNumbersUnderDifferentWays():
    return

# N04 : pyramid output
def pyramidOutput():
    pyramidsCount = int(input("enter the max number of pyramids"))
    for count in range(0, pyramidsCount, 1):
        print("^")

# N05 : Ecrivez un code qui affiche 5 fois N sous la forme "5xN = le_resultat". 
# N étant une valeur saisie par l'utilisateur, le_resultat, le résultat du calcul. 
# Ce dernier sera fait à l'aide d'une succession d'addition.
def kakezanNbyInput():
    Nvalues = []
    N = int(input("Enter a number"))
    for count in range(0, N, 1):
            kakezan = 5*N
            Nvalues.append(kakezan)


# n06 : Créez par compréhension la liste des puissance de 2, de 0 à 8
def powers(powersCount):
   i = 2
   for n in range(powersCount + 1):
       i <<= 1


def launcher():
    print("----------------- LAUNCHER CODES :\n - 1 : print counter with range\n - 2 : Multiply input by 5 and show 5 times\n - 3 : powers\n - 4 : powers of 2 depending on N Input loop ----------------- ")
    keyGiven = int(input("Enter the corresponding number of the function you want to start"))
    if keyGiven == 1:
        printCounterInRange()
    elif keyGiven == 2:
        powersCount = int(input("enter a number"))
        powers()
    elif keyGiven == 3:
        powers()
    elif keyGiven == 4:
        powers()
    elif keyGiven == 5:
        powers()
    elif keyGiven == 6:
        powers()
     
if True:
    launcher()