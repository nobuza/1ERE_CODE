import random
from unittest import result
from numpy import Infinity

enemyDeck = [1, 8, 2, 6, 7, 0, 9]
myDeck = [1, 4, 9, 4, 5, 0, 9, 11, 6]

#randomCard = random.choice(enemyDeck) # Pick random value from list
'''
def findSmallestSuperiorValue(enemyCard):
    candidate = Infinity # the candidate value storer for our smallest value
    for i in myDeck: 
        if i > enemyCard: # if the card is bigger than the enemy card
            if i < candidate: # if the card is smaller than the candidate value for result
                candidate = i
    return i

randomlyChosenValue = random.choice(enemyDeck)
result = findSmallestSuperiorValue(randomlyChosenValue)
print('La carte sortante du deck enemi est égale à', randomlyChosenValue, '\nLa carte la plus faible mais supérieure à cette carte enemie est: ', result)
'''


# on s'embrouille pour rien, ya plus simple en fait

def findSmallestSuperiorValue(enemyCard):
    result = n = min(i for i in myDeck if i > enemyCard)
    return result

randomlyChosenValue = random.choice(enemyDeck)
resultat = findSmallestSuperiorValue(randomlyChosenValue)
print('Enemy card:', randomlyChosenValue)
print('Result:', resultat)