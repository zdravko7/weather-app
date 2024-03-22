# app.py

#import weather_controller

#weather_conditions = weather_controller.print_current_temperature()

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Home Page"

@app.route('/contact', methods=['GET'])
def contact():
    return "Contact page"
    
if __name__ == "__main__":
    app.run()