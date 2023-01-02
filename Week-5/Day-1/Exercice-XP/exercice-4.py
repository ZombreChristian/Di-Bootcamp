class Zoo():
    def __init__(self,zoo_name,animals=[]):
        self.zoo_name = zoo_name
        self.animals = animals
        
    def  add_animal(self,new_animal):
        self.nom = new_animal
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            
            
    def get_animals(self):
        for x in self.animals:
            print(x) 
            
    def sell_animal(self, animal_sold) :
          if animal_sold in self.animals:
              self.animals.remove(animal_sold)
              
              
    def sort_animals(self):
        self.animals.sort()
        for i in enumerate(self.animals):
            print(i) 
        
        
                 
                           
test = Zoo("faso")
test.add_animal("giraffe") 
test.add_animal("chat")
test.add_animal("chaton")
test.add_animal("agout")
test.add_animal("lion")
test.add_animal("lionceau")
test.sort_animals()

#test.sell_animal("lion") 
#test.get_animals()                
        