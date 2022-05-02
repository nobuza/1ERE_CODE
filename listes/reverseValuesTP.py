*Rappel* : pour échanger deux élèments en *Python*, on peut écrire a, b = b, a
Soit la liste **ma_liste = [2, 1, 4, 3]**

#Échangez les élèments d'index 0 et 1, ainsi que 2 et 3

ma_liste = [2, 1, 4, 3]
print(ma_liste)

ma_liste[0], ma_liste[1] = ma_liste[1], ma_liste[0]
ma_liste[2], ma_liste[3] = ma_liste[3], ma_liste[2]

print(ma_liste)

#Dans le code suivant, une liste est créée avec deux entiers générés aléatoirements.

#Si le 1er element est **supérieur** au second, inversez les. Vous utiliserez l'indexation de liste et non les valeurs directement. Dans le cas contraire, il n'y a rien a faire.

import random
l_2_a = [random.randint(0, 9) for rep in range(2)]

#inverser les valeurs de la liste si la 1ere est superieure a la seconde
if l_2_a[0] > l_2_a[1]:
    l_2_a[0], l_2_a[1] = l_2_a[1], l_2_a[0]
    print('inversion')
else:
    print('Rien a faire')

#Dans le code suivant, une liste est créée avec n entiers générés aléatoirements.
#*candidat*, un index, est choisi aléatoirement parmi les indexes de 1 à (taille de la liste - 1), et donc du 2nd au dernier élément de la liste.

#Si ce candidat est **supérieur a son prédécesseur**, inversez les. Vous utiliserez l'indexation de liste et non les valeurs directement. Dans le cas contraire, il n'y a rien a faire.

import random
n = 10
l_n_a = [random.randint(0, 9) for rep in range(n)]
candidat = random.randint(1, n-1)

#inverser les valeurs de la liste si la 1ere est superieure a la seconde
if l_n_a[candidat] > l_n_a[candidat - 1]:
    l_n_a[candidat], l_n_a[candidat - 1] = l_n_a[candidat - 1], l_n_a[candidat]
    print('inversion')
else:
    print('Rien a faire')

#Soit une liste quelconque, en utilisant une boucle non bornée, affichez tous les éléments de la liste :
#- en commençant part le premier,
#- en commencant part le dernier.

import random
n = 10
l_n_a = [random.randint(0, 9) for rep in range(n)]

#Affichage en commençant par le 1er élément
index = 0
while index < n :
    print(l_n_a[index])
    index = index + 1

print("-----------------------------")

#Affichage en commençant par le dernier élément
index = 9
while index >= 0 :
    print(l_n_a[index])
    index = index - 1
    

#Soit la liste la_liste, vous devez déplacer l'étoile de la dernière à la première place. Pour cela :
#- il faut parcourir la liste du dernier au premier index
#- à chaque étape, il faut échanger l'élément courant avec l'élément qui le précède.

import time
la_liste = ['-','-','-','-','*']
index = len(la_liste) - 1
while index != 0 :
    la_liste[index], la_liste[index - 1] = la_liste[index - 1], la_liste[index]
    #print('\r', la_liste, end='', flush=True)
    print(la_liste)
    index = index - 1
    time.sleep(1)
    

#Soit la liste **ma_liste = [1, 3, 4, 2]**.

#Décalez le **dernier élèment** tant qu'il est **supérieur** à l'élèment qui le précède, et que l'index est supérieur à 0. Ceci par échanges successifs.

ma_liste = [1, 3, 4, 2]

print(ma_liste)

index = 3
while index > 0 and ma_liste[index] < ma_liste[index - 1]:
        ma_liste[index], ma_liste[index - 1] = ma_liste[index - 1], ma_liste[index]
        #..., ... = ..., ...
        index = index - 1
        #print('inloop', ma_liste)
        
print(ma_liste)

#L'exercice précédent est la dernière étape de l'algorithme du *tri par insertion*, car elle décale le dernier élément.

#En fait, l'algorithme complet prend un élément de la liste est le décale tant que les éléments précédent sont supérieur. Les élément sont pris un par un **à partir du second élement** de la liste **jusqu'au dernier** grâce à une boucle bornée.

import random
n = 10
ma_liste = [random.randint(0,10) for i in range(n)]

print(ma_liste)

for index in range(1, n, 1):
    while index > 0 and ma_liste[index] < ma_liste[index - 1]:
        ma_liste[index], ma_liste[index - 1] = ma_liste[index - 1], ma_liste[index]
        index = index - 1

print(ma_liste)

