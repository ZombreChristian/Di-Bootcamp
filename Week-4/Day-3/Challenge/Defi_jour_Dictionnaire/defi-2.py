items_purchase = {
  "Apple": 4,
  "Honey": 3,
  "Fan": 14,
  "Bananas": 4,
  "Pan": 100,
  "Spoon": 2
}

wallet = 100 
liste = []

for item, price in items_purchase.items():
  if wallet >= price :
    liste.append(item)
    
print(liste) 

a = sorted(liste)

print("**********************************************")
items_purchase = {
  "Phone": 999,
  "Speakers": 300,
  "Laptop": 5000,
  "PC": 1200
}
wallet =1 

liste = []

for item, price in items_purchase.items():
  if wallet >= price :
    liste.append(item)
    
print(liste) 

  
