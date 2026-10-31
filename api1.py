import main_functions
import requests # library to request data from API

api_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"

response = requests.get(api_url).json()

print(response)

dates = []
for i in response:
    dates.append(i["date"])
print(dates)

print(response[0].keys())

for picture in response:
    print(picture["data"], picture["title"], picture["hdurl"])