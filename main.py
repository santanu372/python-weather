import requests
import argparse

# Replace with your own OpenWeatherMap API key
api_key = ""
base_url = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
  """
  Fetches weather data for a given city.

  Args:
      city (str): Name of the city.

  Returns:
      dict: Weather data or None if city not found.
  """
  params = {"q": city, "appid": api_key}
  response = requests.get(base_url, params=params)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code} - City not found")
    return None

def display_weather(weather_data):
  """
  Displays weather information in a readable format.

  Args:
      weather_data (dict): Weather data returned from API call.
  """
  if weather_data:
    city = weather_data["name"]
    temp = weather_data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
    feels_like = weather_data["main"]["feels_like"] - 273.15
    description = weather_data["weather"][0]["description"]
    print(f"Weather in {city}:")
    print(f"\tTemperature: {temp:.2f} °C")
    print(f"\tFeels Like: {feels_like:.2f} °C")
    print(f"\tDescription: {description}")
  else:
    print("Sorry, couldn't find weather data for that city.")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Get weather information for a city")
  parser.add_argument("city", type=str, help="Name of the city")
  args = parser.parse_args()

  weather_data = get_weather(args.city)
  display_weather(weather_data)
