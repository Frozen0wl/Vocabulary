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
            self.words = pickle.load(read)
    
    def loadSettings(self):
        with open(self.name + ".json", "r") as settings:
            self.settings = json.load(settings)

    def setFrequency(self, lst:dict): # frequency of each level: {1:1, 2:3, 3:7} level 1 everyday, level 2 every three days, level 3 every 7 days
        with open(self.name + ".json", "w") as save:
            self.settings["frequency"] = lst
            json.dump(self.settings, save, indent = 4)

    def setMeaning(self, word:str, meaning:str):
        self.words[word].setMeaning(meaning)

    def setArticle(self, word:wr, article:str):
        word.setArticle(self, article)

    def getMeaning(self, word:str):
        return self.words[word].meaning

    def updateWords(self): #overwrites the pickle file with self.words dictionary
        with open(self.name + ".pkl", "wb") as save:
            pickle.dump(self.words, save)

    def quiz():
        pass
        
            
    

        
        
                    
        

german = notebook("german")
# german.setMeaning('a', "new meaning")
print(german.getMeaning('a'))
# german.updateWords()