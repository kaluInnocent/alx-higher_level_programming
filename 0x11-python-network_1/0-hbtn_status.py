#!/usr/bin/python3
"""A python script that fetches a url"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as response:
        pg = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(pg)))
    print("\t- content: {}".format(pg))
    print("\t- utf8 content: {}".format(pg.decode("utf-8")))
