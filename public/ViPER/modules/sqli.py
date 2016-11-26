import os
import requests
from termcolor.termcolor import colored, cprint


class sqli():
    """
    Class for detecting SQL Injection
    """

    def __init__(self):
        pass

    def execute_all_func(self, target):
        try:
            self.urlbased(target)
        except:
            cprint("Errror In Checking url based SQLi", "red")
        try:
            self.cookiebased(target)
        except:
            cprint("Error In Checking Cookie based SQLi", "red")
        try:
            self.useragentbased(target)
        except:
            cprint("Error In Checking User-agent based SQLi", "red")
        try:
            self.refererbased(target)
        except:
            cprint("Error In Checking Referer-based SQLi", "red")

    def urlbased(self, target):
        cprint("[*] Checking for URL based SQLi", 'yellow')
        key = list()
        path = os.getcwd()
        error = ["MySQL server version", "have an error", "SQL syntax"]
        f = open(path+'/modules/sqlpayloads.txt', 'r')
        payload = f.readlines()
        f.close()
        for i in range(0, len(error)):
            req = requests.get(target+payload[i])
            res = req.text
            if error[i] in res:
                key.append(1)
            else:
                key.append(0)
        if 1 in key:
            cprint("Vulnerable to Url Based SQL Injection!", 'red')
        else:
            cprint("No Injection  Possible !", 'blue')

    def cookiebased(self, target):
        cprint("[*] Checking for Cookie based SQLi", 'yellow')
        path = os.getcwd()
        key = list()
        error = ["MySQL server version", "have an error", "SQL syntax"]
        f = open(path+'/modules/sqlpayloads.txt', 'r')
        payload = f.readlines()
        f.close()
        req = requests.get(target)
        c = req.cookies
        i = c.items()
        for j in range(0, len(error)):
            for ckey, value in i:
                payload[j] = payload[j].strip("\n")
                value = value+payload[j]
                temp = value
                req = requests.get(target, cookies={ckey: value})
                value = temp
                res = req.text
                if error[j] in res:
                    key.append(1)
                else:
                    key.append(0)
        if 1 in key:
            cprint("Vulnerable to Cookie Based SQL Injection!", 'red')
        else:
            cprint("No Injection  Possible !", 'blue')

    def useragentbased(self, target):
        cprint("[*] Checking for User-Agent based SQLi", 'yellow')
        path = os.getcwd()
        key = list()
        error = ["MySQL server version", "have an error", "SQL syntax"]
        f = open(path+'/modules/sqlpayloads.txt', 'r')
        payload = f.readlines()
        f.close()
        user_agent = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 39.0) Gecko/20100101 Firefox/39.0'}
        temp = user_agent['User-agent']
        for i in range(0, len(error)):
            payload[i] = payload[i].strip("\n")
            user_agent['User-agent'] = user_agent['User-agent'] + payload[i]
            req = requests.get(target, headers=user_agent)
            user_agent['User-agent'] = temp
            res = req.text
            if error[i] in res:
                key.append(1)
            else:
                key.append(0)
        if 1 in key:
            cprint("Vulnerable to User-Agent-based SQL Injection!", 'red')
        else:
            cprint("No Injection  Possible !", 'blue')

    def refererbased(self, target):
        cprint("[*] Checking for Cookie based SQLi", 'yellow')
        path = os.getcwd()
        key = list()
        error = ["MySQL server version", "have an error", "SQL syntax"]
        f = open(path+'/modules/sqlpayloads.txt', 'r')
        payload = f.readlines()
        f.close()
        referer = target
        temp = referer
        for i in range(0, len(error)):
            payload[i] = payload[i].strip("\n")
            referer = referer + payload[i]
            req = requests.get(target, headers={'Referer': referer})
            referer = temp
            res = req.text
            if error[i] in res:
                key.append(1)
            else:
                key.append(0)
        if 1 in key:
            cprint("Vulnerable to Referer Based SQL Injection!", 'red')
        else:
            cprint("No Injection  Possible !", 'blue')
