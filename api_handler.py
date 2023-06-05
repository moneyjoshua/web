import requests
import json



def get_joke():
    resp = requests.get("https://api.chucknorris.io/jokes/random")
    if not resp:
        return False, ()
    json = resp.json()
    return json

