puissance_de_2=[]

for index in range(8):
    puissance_de_2.append(2**index)
    print(puissance_de_2)

sequence="10101010"
for index in range(8):
    s=sequence[index]
    se=int(s)
    covert=se*puissance_de_2