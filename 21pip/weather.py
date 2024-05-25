import requests
from dotenv import load_dotenv
import os
load_dotenv()
from pprint import pprint


def get_current_weather():
    print(f"\n** Get current weather conditions ***\n")
    
    city = input(f"Please enter city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)

    weather_data = requests.get(request_url).json()
    # print(weather_data)cclear
    
    if weather_data["cod"] != "404":

        print(f"\nCurrent Weather for {weather_data["name"]}")
        print(f"\nTemp. is {weather_data["main"]["temp"]}")
        print(f"\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.")
    else:
        print(f"No data for {city}")

    # print(weather_data)
    # pprint(weather_data)goa



if __name__ == "__main__":

    get_current_weather()