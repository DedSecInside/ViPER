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
    parser.add_argument('-i', '--recon', help='Injection Attacks', action="store_true")
    parser.add_argument('-u', '--url', type=str, help='URL', required=True)
    parser.add_argument('-A1', '--injection', help='Injection Attacks', action="store_true")
    parser.add_argument('-A3', '--xss', help='XSS', action="store_true")
    parser.add_argument('-a', '--All', help='All possible Attacks', action="store_true")

    args = parser.parse_args()
    target = args.url
    if args.recon or args.All:

        print("--------------------------------------------------------------")
        print("[+]      Getting the Headers")
        print("--------------------------------------------------------------")
        h = header()
        h.get_headers(target)
        print("--------------------------------------------------------------")
        print("[+]      Extracting Cookies ")
        print("--------------------------------------------------------------")
        c = Cookie()
        c.execute_all_func(target)
        print("--------------------------------------------------------------")
        print("[+]     Information Disclosure", 'yellow')
        print("--------------------------------------------------------------")
        i = info()
        i.execute_all_func(target)
        print("--------------------------------------------------------------")
        print("[+]      Testing HTTP Methods")
        print("--------------------------------------------------------------")
        hc = httpCommands()
        hc.execute_all_func(target)
    if args.injection or args.All:
        print("--------------------------------------------------------------")
        print("[+]      Checking for SQL Injection")
        print("--------------------------------------------------------------")
        sql = sqli()
        sql.execute_all_func(target)
    if args.xss or args.All:
        print("---------------------------------------------------------------")
        print("[+]      Checking for XSS Injection")
        print("--------------------------------------------------------------")
        x = xss()
        x.execute_all_func(target)
if __name__ == '__main__':
        main()
