chaine = input("Taper la chaine:")

chaine_vide = ""

for x in range(len(chaine)):
    
  if x == 0 or chaine[x] != chaine[x-1]:
      
    chaine_vide = chaine_vide + chaine[x]

print("Nouvelle chaine avec toutes les lettres consécutives en double supprimées:",chaine_vide)    
