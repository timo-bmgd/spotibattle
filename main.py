import json
import os
import base64
import game

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
    # followers = jsonresult['items']
    return json_result[0];


print(search_artist(get_access_token(), "ACDC"))
