import pickle
from word import word as wr

class notebook:

    def __init__(self, name:str):
        self.name = name
    
    def addWord(self, word):
        with open(self.name, 'ab') as words:
            pickle.dump(word, words)

    