import socket

import geoip2 as geoip2
import requests
from flask import request
import geoip2.database

class ip:

    def geo_Ip(self):

        global username
        username = request.args.get('url')
        req1 = requests.get(username)
        a_1=req1.headers
        server=a_1['Server']

        list1 = username.split("//")

        list2 = list1[1].split("/")

        list3 = list2[0].split(".")

        str1 = []
        for i in range(len(list3)):
            if "www" != list3[i]:
                str1.append(list3[i])
        s = "."

        host_name=s.join(str1)
        print(host_name)
        a=socket.gethostbyname(host_name)

        reader = geoip2.database.Reader('/GeoLite2-City.mmdb') #Download this file to find the Location.

        response = reader.city(a)
        country=response.country.iso_code
        latitude=response.location.latitude
        longitude=response.location.longitude



        return a,country,latitude,longitude,server
