class Dog:
    def __init__(self,name,height):
        self.nom = name
        self.taille = height
        
    def bark(self):
        print("{} goes woof".format(self.nom)) 

    def jump(self):
        x = self.taille*2
        print("{} jumps {} cm high ".format(self.nom, x )) 

        
davids_dog = Dog("Rex",50)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()

