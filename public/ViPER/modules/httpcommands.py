import requests


class httpCommands():
    def __init__(self):
        pass

    def get_method(self, target):
        print("Testing GET Method#")
        req = requests.get(target)
        r = req.status_code
        if r == 200:
            print(r, "OK#")
        else:
            print("Response:", r)

    def post_method(self, target):
        print("Testing POST Method#")
        try:
            req = requests.post(target)
            r = req.status_code
            if r == 200:
                print(r, "OK#")
            else:
                print("Response", r,"#")
        except:
            print("I/O Error")
    def head_method(self, target):
        print("Testing Head Method#")
        req = requests.head(target)
        r = req.status_code
        if r == 200:
            print(r, "OK#")
        else:
            print("Response", OK)

    def put_method(self, target):
        print("Testing Put Method#")
        req = requests.put(target)
        r = req.status_code
        if r == 200:
            print(r,"OK#")
        else:
            print("Response", r)

    def delete_method(self, target):
        print("Testing Delete Method#")
        req = requests.delete(target)
        r = req.status_code
        if r == 200:
            print(r,"OK#")
        else:
            print("Response", r,"#")
