# WeatherCLI

WeatherCLI is a simple command-line interface application that provides current weather information for any city around the world.

## Features

- Fetch real-time weather data
- Display temperature, humidity, and weather description
- Easy-to-use command-line interface

## Installation

1. Clone this repository:
2. Navigate to the project directory:
3. Install the required packages:

## Usage

Run the script with a city name as an argument:

## API Key

This project uses the OpenWeatherMap API. You need to sign up for a free API key at [https://openweathermap.org/](https://openweathermap.org/) and add it to the `config.py` file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

requests==2.26.0

# Add your OpenWeatherMap API key here
API_KEY = "your_api_key_here"
import sys
import requests
from config import API_KEY

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
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
