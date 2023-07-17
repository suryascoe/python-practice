import requests
from twilio.rest import Client

MY_LATITUDE = 29.443817
MY_LONGITUDE = 75.670265
api_key = "Your API Key"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "ACd0086696efce5ec5ae71e1e67602a517"
auth_token = "You Auth Token"


weather_params = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:12]

will_rain = False

for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+15736854664',
        body='Its going to rain bring you ☂️',
        to='To Send Number'
    )

    print(message.status)
