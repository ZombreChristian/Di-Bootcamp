def make_shirt(size,text):
    print(f"The size of the shirt is :{size} and the text is :{text}".format(size,text))

make_shirt(25,"Hello my brother")

print("******************************")
    
def make_shirt(size = 100,text="J'aime python"):
    print(f"The size of the shirt is :{size} and the text is :{text}".format(size,text))
make_shirt()
print("******************************")
make_shirt(250)
make_shirt(150)
print("******************************")
make_shirt(1245,"I'm a maintain")
print("******************************")
a = make_shirt()



    