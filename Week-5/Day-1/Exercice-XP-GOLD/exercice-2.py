import random
class MyList():
    def __init__(self,liste):
        self.liste = liste
    
    def inverse(self):
        return self.liste[::-1]
    
    def trie(self):
        return sorted(self.liste)
    
    def number(self):
        numbers = list(range(len(self.liste)))
        return(numbers)  
    
li =["ali","affi","safi","danie","a","2"]  

renv = MyList(li)
print(renv.number()) 
print(renv.trie())   
    