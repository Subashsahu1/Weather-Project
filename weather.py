from urllib import response
from wsgiref.util import request_uri
import requests

API_KEY = "d3714d432bebc293b07fefdadc100a41"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input ("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print('weather:', weather)
    print('Temperature:', temperature, 'degree celsius')

else:
    print("An error occurred")