Liste={}
#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
prix=0      
#nb=int(len(family))  

for age,key in Liste.items():
    nom = input(key)
    ages = input(age)
    Liste.append(nom,age)
    
    #age=int(input("Donnez l’âge de la personne qui veut un billet: "))
"""
    if age<3:
        
        prix=prix+0
        
    elif 3<age<=12:
        
        prix=prix+10
        
    elif age>12:
        
        prix=prix+15 
        
print(f"le coût total de tous les billets des {nb} membres de la famille est {prix} :".format(nb,prix))           
 """

print(Liste)   
   