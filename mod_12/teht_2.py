import requests
import json


city = input("Enter city: ")


request = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e3f33ee44a99b067499c7d6fe067159b&units=metric")
response = requests.get(request).json()
try:
    vastaus = requests.get(request)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(f"City {city} temperature right now is {json.dumps(json_vastaus ['main'] ['temp'])} degrees Celcius")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
