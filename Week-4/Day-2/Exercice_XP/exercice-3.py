Liste = ["Banana","Apples","Oranges","Blueberries"]
Liste.remove("Banana")

Liste.remove("Blueberries")

Liste.append("Kiwi")

Liste.insert(0,"Apples")
    
x=0
for i in Liste:
    if i == 'Apples':
        x=x+1
print("Le nombre total des pommes :",x)
Liste.clear()

print(Liste)
