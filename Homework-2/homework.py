import requests, json, CONST
import pandas as pd
import plotly.express as px
from pprint import pprint
from MyIp import get_my_ip, get_location


def get_real_time_weather(lat: float, lon: float):
    url = (
        f"https://api.tomorrow.io/v4/weather/realtime?"
        f"location={lat},{lon}"
        f"&apikey={CONST.API_KEY}"
        "&units=metric"
    )

    headers = {"accept": "application/json", "accept-encoding": "deflate, gzip, br"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: HTTP {response.status_code}, response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON parsing failed: {e}")
        return None


def get_weather_forecast(lat: float, lon: float):
    url = (
        f"https://api.tomorrow.io/v4/weather/forecast?"
        f"location={lat},{lon}"
        f"&apikey={CONST.API_KEY}"
        "&units=metric"
    )

    headers = {"accept": "application/json", "accept-encoding": "deflate, gzip, br"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: HTTP {response.status_code}, response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON parsing failed: {e}")
        return None


def main():
    print("--- Weather API Demo ---")
    ip = get_my_ip()
    if not ip:
        print("Failed to get public IP address")
        return

    location = get_location(ip)
    if not location:
        print("Failed to get location data")
        return

    lat, lon, city, country = location

    weather = get_real_time_weather(lat, lon)
    if weather:
        pprint(weather)
        values = weather["data"]["values"]
        df = pd.DataFrame([values])
        df.to_csv("weather.csv", index=False)

    forecast = get_weather_forecast(lat, lon)
    if not forecast:
        print("Failed to get forecast data")
        return

    hourly_data = forecast["timelines"]["hourly"][:24]

    df_hourly = pd.DataFrame([
        {
            "time": item["time"],
            "temperature": item["values"]["temperature"]
        }
        for item in hourly_data
    ])

    fig = px.line(
        df_hourly,
        x="time",
        y="temperature",
        title=f"Předpověď teploty na 24 hodin ({city}, {country})",
        markers=True
    )

    fig.show()


if __name__ == "__main__":
    main()