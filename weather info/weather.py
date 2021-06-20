import requests
from pprint import pprint


API_KEYS = "d50dbec291ffec82723d9399d44a1a80"

City_Name = input("enter the city name ")

url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_KEYS+"&q="+ City_Name

r = requests.get(url).json()

pprint(r)