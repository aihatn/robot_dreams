import requests
import CONST

def get_my_ip():
    try:
        response = requests.get(CONST.URL_IP, timeout = 5)
        if response.status_code == 200:
            return response.text.strip()
        else:
            print(f"Error: HTTP {response.status_code}")
            return None
    except requests.exceptions.RequestException as msg:
        print(f"Request failed: {msg}")
        return None

def get_location(ip: str):
    try:
        url_location = f"http://ip-api.com/json/{ip}"
        response = requests.get(url_location, timeout=5)
        if response.status_code == 200:
            json_data = response.json()
            print(f"Location data for IP {ip}: {json_data}")
            data = json_data["lat"], json_data["lon"]
            return data
        else:
            print(f"Error: HTTP {response.status_code}")
            return None
    except requests.exceptions.RequestException as msg:
        print(f"Request failed: {msg}")
        return None
    except Exception as msg:
        print(f"General error: {msg}")
        return None

def get_my_location():
    ip = get_my_ip()
    if ip:
        print(f"My public IP: {ip}")
        location = get_location(ip)
        if location:
            print(f"My location (lat, lon): {location}")
        else:
            print("Failed to get location")
    else:
        print("Failed to get public IP")


def main():
    pass

if __name__ == "__main__":
    main()