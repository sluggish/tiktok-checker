import os
import requests

from colorama import Fore
from rotate import *

banner = f"""
████████ ██ ██   ██ ████████  ██████  ██   ██      ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
   ██    ██ ██  ██     ██    ██    ██ ██  ██      ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
   ██    ██ █████      ██    ██    ██ █████       ██      ███████ █████   ██      █████   █████   ██████  
   ██    ██ ██  ██     ██    ██    ██ ██  ██      ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
   ██    ██ ██   ██    ██     ██████  ██   ██      ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
"""
print(banner)

proxy = Random_Proxy()

def checker():
    with open("usernames.txt") as file:
        users = file.readlines()
    for user in users:
        jhit = proxy.Proxy_Request(url="https://tiktok.com/@" + user, request_type="get")
        if jhit.status_code == 200:
            print("[UNAVAILABLE] tiktok.com/@{0}".format(user))
        if jhit.status_code == 404:
            print("[AVAILABLE] tiktok.com/@{0}".format(user))

checker()