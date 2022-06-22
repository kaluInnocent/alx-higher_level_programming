#!/usr/bin/python3
"""A Python script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
from urllib.error import HTTPError


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            response = response.read().decode("utf-8")
            print(response)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
