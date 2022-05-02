planification = tab_intervalles = [[0,7,'C1'],[2,5,'C2'],[6,8,'C3'],[1,2,'C4'],[5,6,'C5'],[0,2,'C6'],[4,7,'C7'],[0,1,'C8'],[3,6,'C9'],[1,3,'C10'],[4,5,'C11'],[6,8,'C12'],[0,2,'C13'],[5,7,'C14'],[1,4,'C15']]

def main(listeDeCreneaux):
    for i in range(len(listeDeCreneaux)-1):
        minVal = listeDeCreneaux[i]
        minIndex = i
        for place in range(i, len(listeDeCreneaux)):
            if minVal > listeDeCreneaux[place]:
                minVal = listeDeCreneaux[place]
                minIndex = place
            if minIndex != i:
                listeDeCreneaux[i], listeDeCreneaux[minIndex] = listeDeCreneaux[minIndex], listeDeCreneaux[i]


