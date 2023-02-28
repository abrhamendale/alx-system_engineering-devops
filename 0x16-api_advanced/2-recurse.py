#!/usr/bin/python3
"""Sub count"""


import requests
import json


def recurse(subreddit, hot_list=[]):
    """Retrieves all the hot articles."""
    headers = {'User-Agent': 'Chrome/110.0.5481.105'}
    u = "https://www.reddit.com/r/" + subreddit + "/hot.json?&t=all"
    hl = []
    try:
        req = requests.get(u, headers=headers, allow_redirects=False)
        t = req.json()['data']['children']
        print(t[0])
        hl = recurse2(t, hl)
        return (hl)
    except KeyError:
        return (None)


def recurse2(t, hl):
    """Retrieves all the hottest articles."""
    if len(t) == 0:
        return (hl)
    hl.append(t[0]['data']['title'])
    t.pop(0)
    recurse2(t, hl)
    return (hl)
