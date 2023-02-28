#!/usr/bin/python3
"""Sub count"""


import requests
import json


def top_ten(subreddit):
    """Gets the number of subscribers."""
    headers = {'User-Agent': 'Chrome/110.0.5481.105',
               'allow_redirects': 'False'}
    u = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10&t=all"
    req = requests.get(u, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        print(None)
        return
    for t in req.json()['data']['children']:
        print(t['data']['title'])
