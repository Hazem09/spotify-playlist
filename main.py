import os
from dotenv import load_dotenv, find_dotenv
import requests
import json
from billboard import getSongs


dotenv_path = find_dotenv()
if load_dotenv(dotenv_path):
    TOKEN = os.getenv("TOKEN")
    USER_ID = os.getenv("USER_ID") 
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
else:
    # raise error if .env file is not found
    raise FileNotFoundError(".env file not found")


def create_playlist(name):
    endpoint = f"https://api.spotify.com/v1/users/{USER_ID}/playlists"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "name": name,
        "public": False # change to True if you want the playlist to be public
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    return response.json()["id"]

def search_track(name):
    endpoint = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    params = {
        "q": name,
        "type": "track",
        "limit": 1
    }
    response = requests.get(endpoint, headers=headers, params=params)
    return response.json()["tracks"]["items"][0]["uri"]

def add_tracks_to_playlist(playlist_id, track_uris):
    endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "uris": track_uris
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    return response.ok

if __name__ == "__main__":
    birthday = input("Enter your birthday (YYYY-MM-DD): ")
    songs = getSongs(birthday) # retrieve list of songs
    playlist_name = input('Enter the playlist name: ') # example playlist name
    playlist_id = create_playlist(playlist_name)
    track_uris = [search_track(song) for song in songs]
    add_tracks_to_playlist(playlist_id, track_uris)
    print(f"Playlist '{playlist_name}' created with {len(songs)} songs.")