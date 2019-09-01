import requests
from flask import request


class cors_domain():

    def cors_checker(self):
        global username1
        global print3
        global bool_flag3
        username2 = request.args.get('url')

        req3 = requests.get(username2)
        a_3 = req3.headers
        print(a_3)
        bool_flag3=True
        print3="cors[cross domain] is not allowed."
        if("Access-Control-Allow-Origin" in a_3):
            if("null" in a_3["Access-Control-Allow-Origin"]):

                bool_flag3=False
                print3="the allow oringin header is null. So, there can be possible of granting documents i.e. any origin can create a hostile document with a 'null' Origin"

            elif("*" in a_3["Access-Control-Allow-Origin"]):

                bool_flag3=False
                print3="it allows cors[cross domain]"

            else:

                origin=a_3["Access-Control-Allow-Origin"]
                bool_flag3=True
                print(origin)
                print3=origin

        return print3,bool_flag3