""" 
import random
user = int(input("Entrer un nombre compris entre (1 et 9) :"))
nb_aleatoire = random.randrange(1,10)

if user == nb_aleatoire:
    print("Gagnant")
else :
    print("Meilleure chance la prochaine fois")
      
#print("La valeur du nombre aleatoire était:",nb_aleatoire)       """

import random

#print("La valeur du nombre aleatoire était:",nb_aleatoire)   
score_gagne = 0
score_perdu = 0

while True:
    nb_aleatoire = str(random.randrange(1,10))
    user = (input("Entrer un nombre compris entre (1 et 9) ou taper q pour quitter :"))
    if user != "q":    
        
        if user == nb_aleatoire:
            print("Gagnant")
            score_gagne = score_gagne +1
        else :
            print("Meilleure chance la prochaine fois")
            score_perdu = score_perdu +1
        print("La valeur du nombre aleatoire était:",nb_aleatoire)        
        
            
    else:
        break
print("Total de Score gagné",score_gagne)
print("Total de Score perdu",score_perdu)
                