import requests


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
                print(i[0].ljust(50), i[1].rjust(50))
