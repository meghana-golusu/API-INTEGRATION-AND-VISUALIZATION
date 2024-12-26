import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Replace with your OpenWeatherMap API key
API_KEY = "c47d01e5e2475b8566351d210f56b249"
CITY = "London"
UNITS = "metric"  # Use "imperial" for Fahrenheit
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# Fetch weather data from OpenWeatherMap API
def fetch_weather_data(city, api_key, units="metric"):
    params = {"q": city, "appid": api_key, "units": units}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Parse and structure data
def parse_weather_data(data):
    if "list" not in data:
        print("Error: 'list' key not found in the API response.")
        return None

    weather_list = data["list"]
    records = []
    for entry in weather_list:
        records.append({
            "datetime": datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S"),
            "temperature": entry["main"]["temp"],
            "humidity": entry["main"]["humidity"],
            "wind_speed": entry["wind"]["speed"],
            "description": entry["weather"][0]["description"]
        })
    return pd.DataFrame(records)

# Fetch weather data
weather_data = fetch_weather_data(CITY, API_KEY, UNITS)

if weather_data:
    df = parse_weather_data(weather_data)
    
    if df is not None:
        # Display a preview of the data
        print(df.head())

        # Visualization: Temperature over time
        plt.figure(figsize=(10, 5))
        sns.lineplot(x="datetime", y="temperature", data=df, marker="o")
        plt.title(f"Temperature Trend in {CITY}", fontsize=14)
        plt.xlabel("Date and Time")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()

        # Visualization: Humidity over time
        plt.figure(figsize=(10, 5))
        sns.lineplot(x="datetime", y="humidity", data=df, marker="o", color="orange")
        plt.title(f"Humidity Trend in {CITY}", fontsize=14)
        plt.xlabel("Date and Time")
        plt.ylabel("Humidity (%)")
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()

        # Visualization: Wind Speed over time
        plt.figure(figsize=(10, 5))
        sns.lineplot(x="datetime", y="wind_speed", data=df, marker="o", color="green")
        plt.title(f"Wind Speed Trend in {CITY}", fontsize=14)
        plt.xlabel("Date and Time")
        plt.ylabel("Wind Speed (m/s)")
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()
    else:
        print("Failed to parse the weather data.")
else:
    print("Failed to fetch weather data.")
