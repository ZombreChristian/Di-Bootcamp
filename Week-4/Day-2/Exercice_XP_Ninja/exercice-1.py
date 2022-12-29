from math import sqrt
C = 50
H = 30
user = input("Entrer une chaine de nombre separé par des virgules :")
valeur =user.replace(","," ")
liste_user = valeur.split()

numbers = [int(i) for i in liste_user]

#print(numbers)
val = []
for D in numbers:
   q = int(sqrt((2*C*D)/H))
   print(q) 
   
          

            