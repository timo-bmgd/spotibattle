import json
import os
import base64


from dotenv import load_dotenv
from requests import post, get

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_access_token():
    # Formulate a POST request:
    # 1. Convert our API client data into base64 (RIGHT FORMAT!)
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    # 2. Add those in the headers
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # 3. Define the url for the POST request
    url = 'https://accounts.spotify.com/api/token'

    # 4. Add the data for the post request
    data = {"grant_type": "client_credentials"}

    # 5. POST those using the POST method. This will then save the answer from the server!
    result = post(url, headers=headers, data=data)

    # 6. Extract the json data
    # (JSON is a lightweight format for storing and transporting data)
    # (JavaScript Object Notation)
    json_result = json.loads(result.content)
    access_token = json_result["access_token"]

    # 7. Return token ! :)
    return access_token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=3"

    query_url = url + "?" + query
    result = get(query_url, headers=headers)

    # THE json-result CONTAINS A LIST OF ALL MATCHES. (LIST OF LISTS)
    json_result = json.loads(result.content)["artists"]["items"]
    #followers = json_result['items']
    return json_result[0];


def get_top_artists(token):
    url = "https://api.spotify.com/v1/browse/categories/toplists/playlists"
    headers = get_auth_header(token)
    limit = 50  # Spotify API allows a maximum limit of 50 per request

    top_artists = []

    for offset in range(0, 50, limit):
        params = {
            "country": "US",
            "limit": limit,
            "offset": offset,
        }
        result = get(url, headers=headers, params=params)
        json_result = json.loads(result.content)

        for item in json_result['playlists']['items']:
            playlist_id = item['id']
            artists_from_playlist = get_artists_from_playlist(token, playlist_id)
            top_artists.extend(artists_from_playlist)

    return top_artists[:50]  # Return only the top 50 Artists


def get_artists_from_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    limit = 50

    params = {
        "limit": limit,
    }
    result = get(url, headers=headers, params=params)
    json_result = json.loads(result.content)

    artists_playlist = []
    for item in json_result['items']:
        for artist in item['track']['artists']:
            artists_playlist.append(artist['name'])

    return artists_playlist


def save_top_artists_to_json_file(top_artists):
    with open("top_100_artists.json", "w") as file:
        json.dump(top_artists, file)

##def save_top_artistsplaylist_to_json_file(artists):
  ##  with open("top_100_artistsPlaylist.json", "w") as file:
       ## json.dump(artists, file)

def save_selected_artists_to_json_file(artists):
    with open("selected_Artists.json", "w") as file:
        json.dump(artists, file)

def create_unclean_json_file():
    access_token = get_access_token()
    get_top_artists(access_token)
    top_artists = get_top_artists(access_token)

    artists_data = []
    for i in range(10):
        artistx = top_artists[i]
        artists_data.append(search_artist(get_access_token(), artistx))

    # Saving artist data to a JSON file
    with open("artist_data.json", "w") as outfile:
        json.dump(artists_data, outfile, indent=4)

    artists_data_playlist = []
    artists_from_playlist = get_artists_from_playlist(access_token, "5sVP9rWCHwxCvAuIS1xLAM")

    for i in range(5):
        artisty = artists_from_playlist[i]
        print(artists_from_playlist[i])

        artists_data_playlist.append(search_artist(get_access_token(), artisty))
        print(search_artist(get_access_token(), artisty))

    # Saving artist data to a JSON file
    with open("top_100_artistsPlaylist.json", "w") as outfile:
        json.dump(artists_data_playlist, outfile, indent=4)





