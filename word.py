import datetime
import pickle
class word:
    meaning = None
    article = None
    streak = None
    totalTraining = 0 # number of time the word was called
    lastCalled = None

    def __init__(self, word:str):
        self.word = word

    def setMeaning(self, meaning:str):
        self.meaning = meaning

    def setArticle(self, article:str):
        self.article = article
    
    def addTotalTraining(self):
        self.totalTraining += 1
    
    def updateLastCalled(self):
        self.lastCalled = datetime.datetime.now()


