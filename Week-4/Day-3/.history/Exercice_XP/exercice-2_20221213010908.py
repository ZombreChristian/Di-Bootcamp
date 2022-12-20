Liste=[] 
prix=0      
nb=int(input("Combien de personne veulent un billet ? :"))  

for i in range(0,nb):
    
    age=int(input("Donnez l’âge de la personne qui veut un billet: "))

    if age<3:
        
        prix=prix+0
        
    elif 3<age<=12:
        
        prix=prix+10
        
    elif age>12:
        
        prix=prix+15 
print(f"le coût total de tous les billets des {nb} membres de la famille est {prix} :".format(nb,prix))           
    print("Verification de l'autorisation de la personne.......")

    
 
    Liste.append(age)
    if age in range(16,22) :
            
        print(" Oui la personne est autorisée à regarder le film")
            
    else:
            
        print("Non la personne n'est pas autorisée à regarder le film")
        Liste.remove(age)
            
            

           
print("La liste finale est :",Liste)    