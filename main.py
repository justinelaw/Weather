import requests
from pprint import pprint

API_key = 'b184bd7754cb642c4cf10a3f1dec8ed0' 

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_key + "&q=" + city

weather_data  = requests.get(base_url).json()

pprint(weather_data)

