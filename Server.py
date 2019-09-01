from flask import request, Response, Flask, render_template, logging
import requests
from requests import cookies

from click_jacking import click_jacking
from ip_add import ip
from xss_protection import xss_Protection

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route('/home_night')
def night_1():
    return render_template('home_night.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/about_night')
def about_night():
    return render_template('about_night.html')

@app.route('/severity')
def severity():
    return render_template('severity.html')

@app.route('/severity_night')
def severity_night():
    return render_template('severity_night.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact_night')
def contact_night():
    return render_template('contact_night.html')


@app.route('/scan')
def scan():

    click=click_jacking()
    b=click.click_jackingfun()

    geo=ip()
    c=geo.geo_Ip()


    xss=xss_Protection()
    d=xss.xss_protect()

    return render_template("scan.html",username=b[0],print1=b[1],bool_flag=b[2], ip = c[0], country = c[1], latitude = c[2], longitude = c[3], server = c[4],print2=d[0],bool_flag2=d[1])


if __name__ == "__main__":
    app.run(host='192.168.43.179',port=8010,debug=True)



