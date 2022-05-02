'''
L’algorithme du tri par sélection utilise la recherche du minimum dans une liste. C’est comme un tirage de loto où l’on prend dans 
l’urne la valeur la plus petite à chaque tirage. L’urne contient de moins en moins de boules, et on prends à chaque fois la plus petite.
Ce que je demande est simplement d’écrire une fonction de recherche du plus petit élément d’une liste, avec l’index de départ pour la 
recherche. La fonction renvoie l’index du plus petit élément.
Il faut ensuite appeler cette fonction dans l’algorithme de tri par sélection.
L’idée est simplement de vous faire écrire une fonction et de l’utiliser au sein d’un autre algorithme -> réutilisation de code.
'''

from numpy import Infinity


def smallestValueGetter(liste):
    candidate = Infinity
    for value in liste:
        if value < candidate:
            candidate = value
    return liste.index(candidate)

# tri par selection

def recherche_minimum(liste, debut):
    for i in range(len(liste)):
        for j in range(debut, len(liste)):
            if liste[j-1] > liste[j]:
                liste[j-1], liste[j] = liste[j], liste[j-1]
                print(liste)
    return liste[0]

listOfValues = [8,5,6,2]
smallestValueIndex = smallestValueGetter(listOfValues)
print("La valeur la plus petite de la liste est:",recherche_minimum(listOfValues, smallestValueIndex))