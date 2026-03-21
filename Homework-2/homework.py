import requests, json, CONST
import pandas as pd
from pprint import pprint
from MyIp import get_my_ip, get_location


def get_real_time_weather(lat: float, lon: float):
    """Get real-time weather data for given latitude and longitude."""
    url = (
        f"https://api.tomorrow.io/v4/weather/realtime?"
        f"location={lat},{lon}"
        f"&apikey={CONST.API_Key}"
        "&units=metric"
    )

    headers = {"accept": "application/json", "accept-encoding": "deflate, gzip, br"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
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
    lat, lon = location
    weather = get_real_time_weather(lat, lon)
    if not weather:
        print("Failed to get weather data")
        return

    pprint(weather)

    values = weather["data"]["values"]
    df = pd.DataFrame([values])
    df.to_csv("weather.csv", index=False)

if __name__ == "__main__":
    main()