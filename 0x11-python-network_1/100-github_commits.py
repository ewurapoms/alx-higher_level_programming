#!/usr/bin/python3
"""script lists 10 most recent commits
data from a GitHub repository
"""
import sys
import requests


if __name__ == "__main__":

    auth = sys.argv[1]
    repo = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(auth, repo)

    data = requests.get(url)
    commits = data.json()

    try:
        for index in range(10):
            print("{}: {}".format(
                commits[index].get("sha"),
                commits[index].get("commit").get("author").get("name")))
    except IndexError:
        pass
