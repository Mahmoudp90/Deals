from webbrowser import get
import requests
import json

# Get the token 
def get_token():
    url = "http://127.0.0.1:8000/api-token-auth/"
    response = requests.post(url, headers={"Content-Type": "application/json"}, data={"username": "mahmoudp90", "password": "mahmoudp90"})
    data = response.json()
    return data

token = get_token()
print(token)

