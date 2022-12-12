class Dog:
    def __init__(self,name,height):
        self.nom = name
        self.taille = height
    def bark(self):
        print("goes woof",self.nom) 

    def jump(self):
        x = self.taille*2
        print(self.nom,"jumps",x,"cm high ")
#davids_dog = Dog("Rex",50)
print(Dog.bark("Rex"))
     
