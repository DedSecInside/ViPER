import requests
from termcolor.termcolor import colored, cprint


class httpCommands():
    def __init__(self):
        pass

    def execute_all_func(self, target):
        try:
            self.get_method(target)
        except:
            cprint("Error", "red")
        try:
            self.post_method(target)
        except:
            cprint("Error", "red")
        try:
            self.head_method(target)
        except:
            cprint("Error", "red")
        try:
            self.put_method(target)
        except:
            cprint("Error", "red")
        try:
            self.delete_method(target)
        except:
            cprint("Error", "red")

    def get_method(self, target):
        cprint("Testing GET Method", 'yellow')
        print("")
        req = requests.get(target)
        r = req.status_code
        if r == 200:
            print(r, "OK")
        else:
            print("Response:", r)

    def post_method(self, target):
        cprint("Testing POST Method",'yellow')
        print("")
        req = requests.post(target)
        r = req.status_code
        if r == 200:
            print(r, "OK")
        else:
            print("Response", r)

    def head_method(self, target):
        cprint("Testing Head Method",'yellow')
        print("")
        req = requests.head(target)
        r = req.status_code
        if r == 200:
            print(r, "OK")
        else:
            print("Response", OK)

    def put_method(self, target):
        cprint("Testing Put Method",'yellow')
        print("")
        req = requests.put(target)
        r = req.status_code
        if r == 200:
            print(r, "OK")
        else:
            print("Response", r)

    def delete_method(self, target):
        cprint("Testing Delete Method",'yellow')
        print("")
        req = requests.delete(target)
        r = req.status_code
        if r == 200:
            print(r, "OK")
        else:
            print("Response", r)
