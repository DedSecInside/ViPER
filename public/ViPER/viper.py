from modules.head import header
from modules.Cookie import Cookie
from modules.get_Arguments import arguments
from modules.info_disclosure import info
from modules.httpcommands import httpCommands
import sys
import argparse


class webRecon():
    def __init__(self):
        pass


def main():
    try:
        s = arguments()
        target = s.get_arguments()
        print("--------------------------------------------------------------")
        print("[+]      Getting the Headers#")
        print("--------------------------------------------------------------")
        h = header()
        h.get_headers(target)
    except:
        print("ERROR getting Headers.")
    try:
        print("--------------------------------------------------------------")
        print("[+]      Extracting Cookies #")
        print("--------------------------------------------------------------")
        c = Cookie()
        print("Cookies")
        c.get_cookie(target)
        print("base64 decoded value#")
        c.decode_cookie(target)
    except:
        print("NO Cookies")
    print("--------------------------------------------------------------")
    print("[+]     Information Disclosure#")
    print("--------------------------------------------------------------")
    i = info()

    i.get_robots_txt(target)
    i.get_dot_git(target)
    i.get_dot_svn(target)
    i.get_dot_htaccess(target)

    try:
        print("--------------------------------------------------------------")
        print("[+]      Testing HTTP Methods#")
        print("--------------------------------------------------------------")
        hc = httpCommands()
        try:
            hc.get_method(target)
        except:
            print("Error in get_method")
        try:
            hc.post_method(target)
        except:
            print("Error in post method")
        try:
            hc.head_method(target)
        except:
            print("Error in head method")
        try:
            hc.put_method(target)
        except:
            print("Error in post method")
        try:
            hc.delete_method(target)
        except:
            print("Error in delete method")
    except:
        print("Error in testing methods")
if __name__ == '__main__':
        main()
