import json

def get_artist_follower_count(name):
    with open("artist_data.json", "r") as infile:
        artists_data = json.load(infile)

    for artist_data in artists_data:
        if name in artist_data:
            return artist_data[name]['followers']['total']

    return None

name = "Selena Gomez"
followers = get_artist_follower_count(name)
if followers is not None:
    print(f"{'name'} has {'followers'} followers.")
else:
    print(f"Artist '{name}' not found in the artist_data.json file.")
