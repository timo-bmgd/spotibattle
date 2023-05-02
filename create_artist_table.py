import json

with open('artist_list.json', "r") as fp:
    data = json.load(fp)

data["Eminem"] = 2

with open("artist_list.json", "w") as jsonFile:
    json.dump(data, jsonFile)
