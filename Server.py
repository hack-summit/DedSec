from flask import request, Response, Flask, render_template, logging
import requests
from requests import cookies

from click_jacking import click_jacking
from ip_add import ip

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

    click=click_jacking()
    b=click.click_jackingfun()

    geo=ip()
    c=geo.geo_Ip()

    return render_template("scan.html",username=b[0],print1=b[1],bool_flag=b[2],ip=c[0],country=c[1],latitude=c[2],longitude=c[3],server=c[4])


if __name__ == "__main__":
    app.run(host='192.168.43.179',port=8010,debug=True)



