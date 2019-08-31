import requests
from flask import request, render_template


class click_jacking():

    def click_jackingfun(self):
        global username
        username = request.args.get('url')
        global print1
        global bool_flag
        r = requests.get(username)
        bool_flag = False
        a = r.headers

        print1 = "this domain doesn't contains x-frame options."
        if ("X-Frame-Options" in r.headers):
            if (("DENY" in a["X-Frame-Options"]) or ("SAMEORIGIN" in a["X-Frame-Options"])):
                bool_flag = True
                print1 = "it is not vulnerable to clickjacking as it contains x-frame options."
            else:
                print1 = "it is vulnerable click-jacking."
        elif ("Content-Security-Policy" in r.headers):
            bool_flag = True
            print1 = "this domain doesn't contains frame ancestors in csp policy also it contains x-frame options, so it is not vulnerable to click-jacking."
            if ("frame-ancestors" in a["Content-Security-Policy"]):
                insecure_ancestors = ('*',
                                      'http', 'https',
                                      'http://', 'https://',
                                      'http://*', 'https://*')
                if (insecure_ancestors in a["Content-Security-Policy"]):
                    bool_flag = False
                    print1 = "this domain contains csp policy's insecure wilcards, it is vulnerable to click-jacking."
                else:
                    print1 = "it is not vunerable to click-jacking."
            else:
                bool_flag = False
                print1 = "it is vulnerable to clickjacking"
        print(r.headers)
        print(request.headers)
        # js_data=request.form['']
        print()

        return render_template("scan.html", username=username, print1=print1, bool_flag=bool_flag)
