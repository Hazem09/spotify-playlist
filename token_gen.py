import os
from dotenv import load_dotenv, find_dotenv
import requests
import base64


dotenv_path = find_dotenv()
if load_dotenv(dotenv_path):
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
else:
    # raise error if .env file is not found
    raise FileNotFoundError(".env file not found")

redirect_uri = "http://localhost:8888/callback"
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

# Step 1: Generate authorization URL
params = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "scope": "playlist-modify-private" # add any other scopes your app requires
}
auth_url = authorization_base_url + "?" + "&".join(f"{k}={v}" for k, v in params.items())
print(f"Go to the following URL to authorize your app: {auth_url}")

# Step 2: Get authorization code from callback URL
callback_url = input("Paste the URL of the callback page here: ")
authorization_code = callback_url.split("code=")[1].split("&")[0]

# Step 3: Exchange authorization code for access token
auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
data = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri
}
headers = {
    "Authorization": f"Basic {auth_header}"
}
response = requests.post(token_url, data=data, headers=headers)
access_token = response.json()["access_token"]
print(f"Access token: {access_token}")
