import pickle
from wr import wr
import json
class notebook:

    def __init__(self, name:str):
        self.name = name
        self.words = {}
        self.getWords()
        self.loadSettings()

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
    
    def loadSettings(self):
        with open(self.name + ".json", "r") as settings:
            self.settings = json.load(settings)

    def setFrequency(self, lst:dict): # frequency of each level: {1:1, 2:3, 3:7} level 1 everyday, level 2 every three days, level 3 every 7 days
        with open(self.name + ".json", "w") as save:
            self.settings["frequency"] = lst
            json.dump(self.settings, save, indent = 4)

    def setMeaning(self, word:wr, meaning:str):
        word.setMeaning(meaning)

    def setArticle(self, word:wr, article:str):
        word.setArticle(self, article)

    def updateWords(self): #overwrites the pickle file with self.words dictionary
        with open(self.name + ".pkl", "wb") as save:
            for item in self.words:
                pickle.dump(self.words[item], save)

    def quiz():
        
            
    

        
        
                    
        

english = notebook("english")

    
