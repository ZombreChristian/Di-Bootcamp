import random

def get_random_temp(season):
    season = int(season)
    if  3 <= season <= 6:
        print("Saison :Printemps")
    elif 6 <= season <= 9:
        print("Saison :Eté")
    elif 9 <= season <= 12:
        print("Saison :Automne")
    elif 1 <= season <= 3:
        print("Saison :Hiver")
    
   
    
    return float(random.randrange(-10, 41))
#print(get_random_temp())

def main():
   
   user = input(("Donner un numero de mois:"))
   temp= float(get_random_temp(user))
   
   if temp < 0:
       print("Brrr, c’est glacial! Portez des couches supplémentaires aujourd’hui ")
   elif 0 <= temp < 16:
       print("Assez froid! N’oublie pas ton manteau ")
   elif 16 <= temp < 23:
       print("Il fait moins chaud ")
          
   elif 24 <= temp < 32:
       print("Il fait de plus en plus chaud ") 
       
   else :
       print("Il fait très très chaud ")
    
   a = f"La température actuelle est de {temp} degrés Celsius.".format(float(temp))
   return a

print(main())