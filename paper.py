import pickle
from wr import wr
import json
a = wr("a")
b = wr("b")
c = wr("c")

# dic = {}
# print(a.word)
# a.setMeaning("meaning")
# dic[a.word] = a
# dic[b.word] = b
# dic[c.word] = c
# print(dic)
with open("german.pkl", "wb") as save:
    # for item in dic:
    #     print(item)
    #     pickle.dump(dic[item], save)
    pickle.dump(dic, save)

new = {}
with open("german.pkl", "rb") as read:
    new = pickle.load(read)

print(new)
print(new['a'].meaning)

# print(new['a'].meaning)

