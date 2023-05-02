import json

with open('artist_list.json') as fp:
    data = json.load(fp)
    print(data[2])
