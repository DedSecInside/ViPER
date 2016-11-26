import requests
from termcolor.termcolor import colored, cprint


class header:
        """
            Class for extracting headers
        """
        def __init__(self):
            pass

        def get_headers(self, target):
            req = requests.head(target)
            req = req.headers
            for i in req.items():
                cprint(i[0].ljust(60)+i[1].rjust(50),'blue')
