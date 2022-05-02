lines = []                                         #1 
head = None                                        #-
with open('emissions_co2-tonne.csv', 'r') as csv : #2
    head = csv.readline()                          #3
    head = head.rstrip('\n')                       #4
    line = head                                    #5
    head = head.split(';')                         #6
    while line :                                   #7
        line = csv.readline().rstrip('\n')         #8
        if line :                                  #9
            columns = line.split(';')              #10
            lines.append(columns)                  #11



'''
Cherchez dans la liste lines s'il existe un pays qui a une population de 547030.0 habitants. 
Attention, les valeurs dans la liste lines sont toutes des chaines de caractere.
'''

# il n'est pas question de pays

'''
Stockez dans la variable *index_pays* l'index de l'element de la liste *head* qui a pour valeur 'Country'
'''

keyword = input("Entrez un mot à rechercher")

for word in head:
    if any(word in head == keyword):
        print ('word in head founded')

