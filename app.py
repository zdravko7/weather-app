# app.py

import weather_controller

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