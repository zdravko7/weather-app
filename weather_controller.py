import requests

url = r"https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 42.69,
    "longitude": 23.32,
    "current": "temperature_2m,wind_speed_10m",


}

response = requests.get(url, params=params)

responseJSON = response.json()

def print_current_temperature():
    return f'The current temperature is {str(responseJSON['current']['temperature_2m'])}'