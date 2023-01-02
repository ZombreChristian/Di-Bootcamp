class Farm():
    def __init__(self,name):
        
        self.nom = name
        print(f"{self.nom}'s farm".format(self.nom))
    
        
    def add_animal(self,animal_name,nombre=""):
        self.nom = animal_name
        self.nb = nombre 
            
        liste =[]
        dictio = [{self.nom : self.nb }]
        dictio += dictio
        
        for i,j in dictio.items():
            liste.append(i)
            

            print(liste)
        
        
        
            
            """ for i,j in x.items():
                print(i,j) """
             
            #if w==0:
               # w = dictio.count(x)
            #print(x)
        
        
        
        
        #liste =[]
        
        #
        #a=liste.count(self.nom)
        
        #liste.append(self.nom)
        #liste.append(a)
        #liste.append(self.nb)
        
        #a= liste.count(self.nom)
        
        #liste.append(a)
        
        #liste ={ self.nom : a } 
         
        
        
        #(liste)
        
macdonald = Farm("McDonald")        
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
#macdonald.add_animal('sheep')