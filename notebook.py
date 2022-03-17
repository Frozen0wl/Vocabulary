import pickle
from wr import wr

class notebook:

    def __init__(self, name:str):
        self.name = name
        self.words = {}
        self.getWords()
        

    def addWord(self, word:str):
        with open(self.name + ".pkl", 'ab') as save:
            pickle.dump(wr(word), save)
        
    def getWords(self):
        with open(self.name + ".pkl", 'rb') as read:
            while True:
                try:
                    obj = pickle.load(read)
                    self.words[obj.word] = obj
                except Exception as e:
                    if str(e) == "Ran out of input": break
                    else: print(e); break
    
                    
        

english = notebook("english")

    
