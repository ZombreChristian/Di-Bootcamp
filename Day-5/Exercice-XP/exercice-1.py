

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def ancienCat(Vals):
        
        for valeur in Vals.values():
            print()
            
P1 = Cat("Milou",2)
P2 = Cat("Bobi",3)
P3 = Cat("Patience",4)

noms = [P1.name,P2.name,P3.name]
ages = [P1.age,P2.age,P3.age]

liste = { noms:ages for noms , ages in zip(noms,ages)}
print(Cat.ancienCat(liste))


