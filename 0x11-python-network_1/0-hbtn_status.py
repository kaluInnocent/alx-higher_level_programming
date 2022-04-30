#!/usr/bin/python3
import urllib.request
"""A python script that fetches a url"""


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
