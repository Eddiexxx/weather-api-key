import requests 
from dotenv import load_dotenv 
import os
from pprint import pprint

# Related to the vidio: Python Virtual Environment and pip for Beginners.mp4 
# YouTube Address : https://www.youtube.com/watch?v=eDe-z2Qy9x4 ( video of instructor)
# Activate the .venv

load_dotenv()

def get_current_weather():
    print('\n*** Get Current Weather Condotion ***\n')
    
    city = input('\nPlease enter a city name:\n')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    # print(request_url)
    
    weather_data = requests.get(request_url).json()
    
    print()
    # pprint(weather_data)
    
    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]}')
    print(f'\nFeels like : {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.\n')
    
if __name__ == '__main__':
    get_current_weather()