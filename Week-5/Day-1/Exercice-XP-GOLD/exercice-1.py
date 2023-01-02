from math import pi
class Circle():
    def __init__(self,rayon = 1):
        self.rayon = rayon
        
    def perimetre(self):
        return 2* self.rayon * pi
    
    def surface(self):
        return pi * self.rayon * self.rayon
    def definition(self):
        return ("Un cercle est une courbe plane fermée constituée de point situés à égale distance d'un point nommé centre")
       
calcul = Circle()

print(calcul.definition() )    