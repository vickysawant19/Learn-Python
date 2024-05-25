import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather(city="goa"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data
    
    # if weather_data["cod"] != "404":

    #     print(f"\nCurrent Weather for {weather_data["name"]}")
    #     print(f"\nTemp. is {weather_data["main"]["temp"]}")
    #     print(f"\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.")
    # else:
    #     print(f"No data for {city}")

    # print(weather_data)
    # pprint(weather_data)goa


if __name__ == "__main__":
    print("\n *** Get Current Weather Conditions ***\n")

    city = input("\n Please enter a city name: ")

    weather_data = get_current_weather(city)

    pprint(weather_data)



