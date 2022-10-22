from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime
from flask import jsonify
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/time")
def time():
    return jsonify(time=datetime.now())


@app.route("/weather")
def weather_latlong():
    req = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(request.args.get("lat"), request.args.get("long"), "ea50e63a3bea67adaf50fbecbe5b3c1e")).json()
    return jsonify(temp=req["main"]["temp"]-273.15, weather=req["weather"][0]['main'], description=req["weather"][0]['description'])


@app.route("/weather/<city>")
def weather(city):
    req = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, "ea50e63a3bea67adaf50fbecbe5b3c1e")).json()
    return jsonify(temp=req["main"]["temp"]-273.15, weather=req["weather"][0]['main'], description=req["weather"][0]['description'])


if __name__ == "__main__":
    app.run(debug=True)
