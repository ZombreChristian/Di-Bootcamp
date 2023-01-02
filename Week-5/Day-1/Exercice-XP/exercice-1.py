class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def ancienCat(self):
        a=[]
        liste = { self.name : self.age }
        for x ,y in liste.items():
             print(x,y)
             
         
P1 = Cat("Milou",2)
P2 = Cat("Bobi",3)
P3 = Cat("Patience",4)

P1.ancienCat()
P2.ancienCat()
P3.ancienCat()


 
