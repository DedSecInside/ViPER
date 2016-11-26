import requests
import os
from termcolor.termcolor import colored, cprint


class xss():
    def __init__(self):
        pass

    def execute_all_func(self, target):
        try:
            self.xsscheck(target)
        except:
            cprint("Error Checking for X-Frame-Options", "red")
        try:
            self.createPOC(target)
        except:
            cprint("Error Creating POC", "red")

    def xsscheck(self, target):
        try:
            req = requests.get(target)
            head = req.headers["X-Frame-Options"]
            print("X-frame-options found!")
            print("Clickjacking not Possible",)
        except:
            cprint("Alert!", "red")
            cprint("Vulnerable to Clickjacking", "red")
            self.createPOC(target)

    def createPOC(self, target):
        html = """
            <html>
            <body>
            <p>Website is vulnerable to clickjacking!</p>
     <iframe src="'''+target+'''" height='600px' width='800px'></iframe>
            </body>
            </html>
        """
        f = open("poc.html", "w")
        f.write(html)
        f.close()
