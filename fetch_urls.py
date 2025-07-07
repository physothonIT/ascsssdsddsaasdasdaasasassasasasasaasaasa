import requests
from requests.exceptions import RequestException

with open("mylist.txt", "r") as file:
    urls = [line.strip() for line in file if line.strip()]

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{url} - Status: {response.status_code}")
            print("Response Content:")
            print(response.text[:500])  # Limit to first 500 characters
            print("-" * 50)
        else:
            print(f"{url} - Status: {response.status_code} (Not 200)")
    except RequestException as e:
        print(f"Error fetching {url}: {e}")
