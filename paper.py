import pickle
from wr import wr
import json
a = wr("a")
b = wr("b")
c = wr("c")

dic = {}

dic[a.word] = a
dic[b.word] = b
dic[c.word] = c
print(dic)
with open("english.pkl", "wb") as save:
    for item in dic:
        print(item)
        pickle.dump(dic[item], save)


