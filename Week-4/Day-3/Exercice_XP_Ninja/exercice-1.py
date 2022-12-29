chaine ="Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

for x in chaine:
   a= chaine.replace(",","")
   
liste = a.split()
print("liste =",liste)
print("The manufacturers/companies are in the list is:",len(liste))

print("Liste =",sorted(liste,reverse=True))
listes = []
for x in liste:
    if "o" in x:
        listes.append(x)
print("The manufacturers’ names have the letter ‘o’ in them is :",len(listes))

lis = []
for y in liste:
    if "i" in y:
        lis.append(y)
print("The manufacturers’ names have the letter ‘i’ in them is :",len(lis))  

new_liste = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"] 
s = set(new_liste)
S = ', '.join(s)
print("chaine =",(S))   
for x in S:
   a= S.replace(",","")
   
ls = a.split()
print("The manufacturers/companies are in the list is:",len(ls))

for i in S:
    A = S[::-1]
print("A =",A)
for j in A:
   a= A.replace(",","")   
les = a.split()
print(sorted(les))