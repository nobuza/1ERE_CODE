def moyenneCalc(lst):
    return sum(lst) / len(lst)
  
lst = [2, 4, 6, 1, 9, 3]
moyenne = moyenneCalc(lst)
  
print("Moyenne de la liste =", round(moyenne, 2))