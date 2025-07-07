import requests

with open("mylist.txt", "r") as file:
    urls = [line.strip() for line in file if line.strip()]

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        print(f"{url} - Status: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
