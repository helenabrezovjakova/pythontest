import requests

endpoint = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}"
payload = {"q": "London, UK", "units": "metric", "appid": "YOUR_APP_ID"}

response = request.get(endpoint, params=payload)
data = response.json()

print data 'main'
print response.url
print reponse.status_code
print response.headers["content-type"]
print response.text
