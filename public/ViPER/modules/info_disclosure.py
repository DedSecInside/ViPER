import requests


class info():
    def __init__(self):
        pass

    def get_robots_txt(self, target):
        req = requests.get(target+"/robots.txt")
        r = req.text
        print(r,"#")

    def get_dot_git(self, target):
        req = requests.get(target+"/.git/")
        r = req.status_code
        if r == 200:
            subprocess.call("wget -r"+target, shell=True)
        else:
            print("NO .git folder found#")

    def get_dot_svn(self, target):
        req = requests.get(target+"/.svn/entries")
        r = req.status_code
        if r == 200:
            print(r,"#")
        else:
            print("NO .SVN folder found#")

    def get_dot_htaccess(self, target):
        req = requests.get(target+"/.htaccess")
        r = req.text
        statcode = req.status_code
        if statcode == 403:
            print("403 Forbidden#")
        else:
            print(r,"#")
