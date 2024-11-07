import sys
import requests
from config import API_KEY

def get_weather(city):
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no",
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"],
            "description": data["current"]["condition"]["text"]
        }
    else:
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather_cli.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    weather_data = get_weather(city)

    if weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Description: {weather_data['description'].capitalize()}")
    else:
        print(f"Unable to fetch weather data for {city}")

if __name__ == "__main__":
    main()