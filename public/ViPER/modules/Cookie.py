#import base64
import requests
#from urllib.parse import urlparse


class Cookie():
    """
        Class for extracting Cookies
    """
    def __init__(self):
        pass

    def get_cookie(self, target):
        req = requests.get(target)
        c = req.cookies
        i = c.items()
        for name, value in i:
            print(name, value)

"""    def decode_cookie(self, target):
        req = requests.get(target)
        c = req.cookies
        i = c.items()
        for name, value in i:
            rep = ""
            b64 = ""
            rep = value.replace("%3D", "=")
            b64 = base64.b64decode(rep)
            print(b64)
"""
