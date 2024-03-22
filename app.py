# app.py

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



#import weather_controller

#weather_conditions = weather_controller.print_current_temperature()

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return print_current_temperature()

@app.route('/contact', methods=['GET'])
def contact():
    return "Contact page"
    
if __name__ == "__main__":
    app.run()