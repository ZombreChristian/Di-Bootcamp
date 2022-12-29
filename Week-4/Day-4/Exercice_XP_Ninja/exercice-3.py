def box_printer():
    user = input("Donnez une chaine :")
    a = user.split()
    print("***************************")
    
    for i in a: 
        print("*",i,"                  *")
    print("***************************")    
    return  
        
print(box_printer())        