#!/usr/bin/python3
from urllib.request import Request, urlopen
"""A python script that fetches a url"""

if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        pg = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(pg)))
    print("\t- content: {}".format(pg))
    print("\t- utf8 content: {}".format(pg.decode("utf-8")))
