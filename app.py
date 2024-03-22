import requests
import weather_controller

from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def home():
    temperature = weather_controller.print_current_temperature()
    return render_template('home.html', temperature=temperature)


@app.route('/contact', methods=['GET'])
def contact():
    return "Contact page"
    
if __name__ == "__main__":
    app.run()