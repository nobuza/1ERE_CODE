lines = []                                         #1 
head = None                                        #-
index_population = 5
with open('countries.csv', 'r') as csv : 
    head = csv.readline()                          #3
    head = head.rstrip('\n')                       #4
    line = head                                    #5
    head = head.split(';')                         #6
    while line :                                   #7
        line = csv.readline().rstrip('\n')         #8
        if line :                                  #9
            columns = line.split(';')              #10
            lines.append(columns)                  #11
        
#print(lines[0][index_population])
'''
def searchForPopulation(searching:float): 
    for i in range (0, len(lines)):
        if lines[i][index_population]==searching:
           return(lines[i][3])

def searchPythonic(searching):
    any(e[5] == searching for e in lines):
        return e
'''
    
element = 66987244

elementInList = False
for list in lines:
    if element in list:
       elementInList = True

print(elementInList)

'''
print(searchForPopulation(66987244))
print(searchPythonic(66987244))
'''