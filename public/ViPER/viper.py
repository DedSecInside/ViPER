from modules.head import header
from modules.Cookie import Cookie
from modules.get_Arguments import arguments
from modules.info_disclosure import info
from modules.httpcommands import httpCommands
from modules.sqli import sqli
from termcolor.termcolor import colored, cprint
from modules.xss import xss
import sys
import argparse


class webRecon():
    def __init__(self):
        pass


def main():
    parser = argparse.ArgumentParser(description="Web Recon Script")
    parser.add_argument('-u', '--url', type=str, help='URL', required=True)
    parser.add_argument('-A1', '--injection', help='Injection Attacks', action="store_true")
    parser.add_argument('-A3', '--xss', help='XSS', action="store_true")
    parser.add_argument('-a', '--All', help='All possible Attacks', action="store_true")
    args = parser.parse_args()
    target = args.url
    cprint('`````````````````````````````````````````````````````', 'red')
    cprint('`````````                                     ```````', 'red')
    cprint('`````````                                  ```````', 'red')
    cprint('`````````                                     ```````', 'red')
    cprint('```````````````````````````````````````````````````````', 'red')
    cprint("--------------------------------------------------------------", 'green')
    cprint("[+]      Getting the Headers", 'yellow')
    cprint("--------------------------------------------------------------", 'green')
    h = header()
    h.get_headers(target)
    cprint("--------------------------------------------------------------", 'green')
    cprint("[+]      Extracting Cookies ", 'yellow')
    cprint("--------------------------------------------------------------", 'green')
    c = Cookie()
    c.execute_all_func(target)
    cprint("--------------------------------------------------------------", 'green')
    cprint("[+]     Information Disclosure", 'yellow')
    cprint("--------------------------------------------------------------", 'green')
    i = info()
    i.execute_all_func(target)
    cprint("--------------------------------------------------------------", 'green')
    cprint("[+]      Testing HTTP Methods", 'yellow')
    cprint("--------------------------------------------------------------", 'green')
    hc = httpCommands()
    hc.execute_all_func(target)
    if args.injection or args.All:
        cprint("--------------------------------------------------------------", 'green')
        cprint("[+]      Checking for SQL Injection", 'yellow')
        cprint("--------------------------------------------------------------", 'green')
        sql = sqli()
        sql.execute_all_func(target)
    if args.xss or args.All:
        cprint("---------------------------------------------------------------", 'green')
        cprint("[+]      Checking for XSS Injection", 'yellow')
        cprint("--------------------------------------------------------------", 'green')
        x = xss()
        x.execute_all_func(target)
if __name__ == '__main__':
        main()
