puissance_de_2 = [] #Création d'une liste python
for index in range(8): #boucle bournée, ! aux ':' en fin ligne
    puissance_de_2.append(2**index)
    
print(puissance_de_2) #affiche le contenu de la variable puissance_de_2

print("Enter a 8bit range")
sequence = input()

convert = 0

for index in range(8):
    s = sequence[index]
    se = int(s)
    convert = se * puissance_de_2[7 - index] + convert

print(convert)
