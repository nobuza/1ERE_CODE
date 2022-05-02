'''
------------PSEUDOCODE-------------
1. 2 variables, liste et n qui correspond au nombre d'éléments dans la liste
2. for index in range de ma liste, boucle sur toutes les valeurs de la liste, commençant à la deuxième valeur
3. si la valeur à l'index est plus petite que celle d'avant, on inverse les valeurs des deux éléments.
4. on retire 1 à n, considérant qu'on a traité un élément, on retire 1 au "compteur d'éléments dans la liste" n.
5. print(liste)
'''

import random
ma_liste = [5, 1, 2, 4]
n = len(ma_liste)

print(ma_liste)

for index in range(1, n, 1):
    while index > 0 and ma_liste[index] < ma_liste[index - 1]:
        ma_liste[index], ma_liste[index - 1] = ma_liste[index - 1], ma_liste[index]
        index = index - 1

print(ma_liste)
