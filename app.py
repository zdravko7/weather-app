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
    return f'The current temperature is {str(responseJSON['current']['temperature_2m'])} °C'




#import weather_controller

#weather_conditions = weather_controller.print_current_temperature()

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    temperature = print_current_temperature()
    return render_template('home.html', temperature=temperature)

@app.route('/contact', methods=['GET'])
def contact():
    return "Contact page"
    
if __name__ == "__main__":
    app.run()