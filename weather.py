from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
WEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
AIR_QUALITY_BASE_URL = 'https://api.openweathermap.org/data/2.5/air_pollution?'

def get_current_weather(city):
    weather_url = WEATHER_BASE_URL + "appid=" + os.getenv("API_KEY") + f"&q={city}&units=imperial"
    weather_data = requests.get(weather_url).json()

    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']

    air_quality_url = AIR_QUALITY_BASE_URL + f"lat={lat}&lon={lon}&appid=" + os.getenv("API_KEY")
    air_quality_data = requests.get(air_quality_url).json()

    total_data = {**weather_data, **air_quality_data}

    return total_data

if __name__ == "__main__":
    print('\n*** Get Current Weather***\n')
    city = input("\nEnter city name: ")
    total_data = get_current_weather(city)

    print("\nWeather Data:")
    pprint(total_data)