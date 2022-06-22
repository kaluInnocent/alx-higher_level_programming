#!/usr/bin/python3
"""A script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": q})
    try:
        response = response.json()
        if response == {} or len(response) == 0:
            print("No result")
        else:
            print(
                    f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
