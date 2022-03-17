import json
with open("english.json", "r") as save:
    settings = json.load(save)

print(type(settings))
print(settings)
