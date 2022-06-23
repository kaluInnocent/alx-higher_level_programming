#!/usr/bin/python3
"""A script that takes 2 arguments in order
to list 10 commits (from the most recent to oldest)
of the repository 'rails' by the user 'rails'
"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r = requests.get(url).json()
    if len(r) > 10:
        c = 10
    else:
        c = len(r)
    try:
        for i in range(c):
            sh = r[i].get("sha")
            com = r[i].get("commit").get("author").get("name")
            print(f"{sh}: {com}")
    except IndexError:
        pass
