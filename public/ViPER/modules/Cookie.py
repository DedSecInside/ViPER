import base64
import requests
from termcolor.termcolor import colored, cprint


class Cookie():
    """
        Class for extracting Cookies
    """
    def __init__(self):
        pass

    def execute_all_func(self, target):
        try:
            self.get_cookie(target)
        except:
            cprint("Errror Getting Cookies", "red")
        try:
            self.decode_cookie(target)
        except:
            cprint("Error Decoding Cookies (base64)", "red")

    def get_cookie(self, target):
        cprint("[*]Getting Cookie", "yellow")
        req = requests.get(target)
        c = req.cookies
        i = c.items()
        if i:
            for name, value in i:
                print(name, value)
        else:
            cprint("No cookies found", "red")

    def decode_cookie(self, target):
        cprint("")
        cprint("[*]Decoding Cookie", "yellow")
        req = requests.get(target)
        c = req.cookies
        i = c.items()
        for name, value in i:
                b64 = value.replace("%3D", "=")
                try:
                    b64 = base64.b64decode(b64).decode('ascii')
                except:
                    print("")
                print(name, b64)
