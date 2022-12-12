Liste =[]
som = 10
while 1:
    pizza = input("Entrer pizza ou taper (q) pour quitter: ")
    if pizza != "q" :
        Liste.append(pizza)
        print("Vous avez ajouter",pizza, "à la liste de vos pizzas")
        som = (som + 2.5)
    else:
        break
        
        
print("La liste de vos pizzas :",Liste,"et le prix total est :",som)