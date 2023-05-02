import json

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_artists(data):
    artists = []
    for artist_data in data:
        artist = {
            'name': artist_data['name'],
            'popularity': artist_data['popularity'],
            'followers': artist_data['followers']['total']
        }
        artists.append(artist)
    return artists

def save_data_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    data = load_data_from_json('artist_data.json')
    artists = extract_artists(data)
    save_data_to_json(artists, 'artists_cleaned.json')

print()