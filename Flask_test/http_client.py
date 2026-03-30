import requests
from requests.auth import HTTPBasicAuth

SERVER_URL = "http://localhost:8000"

def call_test():
    try:
        response = requests.get(f"{SERVER_URL}/test", timeout=5)
        if response.status_code == 200:
            print("Response from server:", response.json())
        else:
            print(f"Error: HTTP{response.status_code}, response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"General error: {e}")

def call_test_auth():
    try:
        myauthentication = HTTPBasicAuth("RD", "123")
        response = requests.get(f"{SERVER_URL}/test_auth", auth=myauthentication, timeout= 5)
        if response.status_code == 200:
            print("Response from server:", response.json())
        else:
            print(f"Error: HTTP{response.status_code}, response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"General error: {e}")


def main():
    print("Calling /test endpoint")
    call_test()
    print("Calling /auth endpoint")
    call_test_auth()


if __name__ =="__main__":
    main()