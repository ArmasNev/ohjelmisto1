
import requests
import json

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
Chuck = response
print(f"Random Norris joke: {Chuck['value']}")
