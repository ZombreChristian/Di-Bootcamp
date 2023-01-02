class Song():
    def __init__(self,lyrics):
        self.liste = lyrics
        
    def sing_me_a_song(self):
        for x in self.liste:
            print(x)    
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])        
#print(stairway())

stairway.sing_me_a_song()