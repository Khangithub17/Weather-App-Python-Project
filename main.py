
import requests
import json

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=be3d02720d30478d91275221233107&q={city}"

r = requests.get(url)
print(r.text)
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])



