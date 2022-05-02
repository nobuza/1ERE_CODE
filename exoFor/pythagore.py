from math import sqrt

def pythagore():
    print("- a = Côté  adjacent \n- b = côté opposé \n - c = hypothénuse")
    formula = input("Quel côté voulez vous calculer ?")
    
    if formula == "c":
    	side_a = int(input("Renseignez la longeur du 1er côté"))
    	side_b = int(input("Renseignez la longeur du 2eme côté"))
    
    	side_c = sqrt(side_a * side_a + side_b * side_b)
    	
    	print("La longueur de l'hypothénuse est:")
    	print(side_c)
    
    elif formula == "a":
    	side_a = int(input("Renseignez la longeur du côté connu"))
    	side_c = int(input("Renseignez la longeur de l'hypothénuse"))
        side_b = sqrt((side_c * side_c) -(side_a * side_a))
        print("La longueur de l'autre côté est : ")
        print(side_b)
    
    elif formula == "b":
    	side_a = int(input("Renseignez la longeur du 1er côté"))
    	side_b = int(input("enseignez la longeur de l'hypothénuse"))
            
        side_c = sqrt(side_c * side_c - side_a * side_a)
        
        print("La longueur de l'autre côté est :")
        print(side_c)
    
    else:
    	print('Please select a side between a, b, c')