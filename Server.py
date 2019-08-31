from flask import request, Response, Flask, render_template, logging
import requests
from requests import cookies

from click_jacking import click_jacking

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('hackathon.html')

@app.route('/home_night')
def night_1():
    return render_template('hackathonnight_1.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/about_night')
def about_night():
    return render_template('about_night.html')


@app.route('/scan')
def scan():

    c=click_jacking()
    return c.click_jackingfun()


if __name__ == "__main__":
    app.run(host='192.168.43.179',port=8010,debug=True)



