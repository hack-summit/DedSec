import requests
from flask import request


class xss_Protection():

    def xss_protect(self):

        global username1
        global print2
        global bool_flag2
        username1 = request.args.get('url')

        req3 = requests.get(username1)
        a_2=req3.headers
        print(a_2)
        bool_flag2=False
        print2="there is kind of possible of implementing xss, as it will not block the page when it finds the inline scripts."

        if("X-XSS-Protection" in a_2):

            if("0" in a_2["X-XSS-Protection"]):

                bool_flag2=False
                print2="here, they disabling the xss-filters, i.e. setting xss protection to 0."

            else:
                bool_flag2=True
                print2="if the browser founds an inline scripts, it blocks. So, some reflected xss can be prevented."

        elif("Content-Security-Policy" in a_2):

            if("script-src" in a_2["Content-Security-Policy"]):

                if("'unsafe-inline'" in a_2["Content-Security-Policy"]):
                    bool_flag2=False
                    print2="this page accepts inline scripts, instead of blocking it."

                elif("'none'" in a_2["Content-Security-Policy"]):
                    bool_flag2=True
                    print2="this page blocks prevents xss by blocking the inline scripts."

                else:
                    bool_flag2=False
                    print2="they are not filtering xss and won't block the web page."

            else:
                bool_flag2=False
                print2="they are not filtering xss and won't block the web page."

        return print2,bool_flag2

