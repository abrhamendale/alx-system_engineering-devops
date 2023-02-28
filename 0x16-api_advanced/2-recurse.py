#!/usr/bin/python3
"""Sub count"""


import requests
import json


def recurse(subreddit, hot_list=[]):
    """Retrieves all the hot articles."""
    headers = {'User-Agent': 'Chrome/110.0.5481.105',
               'allow_redirects': 'False'}
    u = "https://www.reddit.com/r/" + subreddit + "/hot.json?&t=all"
    hl = []
    req = requests.get(u, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        return (None)
    t = req.json()['data']['children']
    hl = recurse2(t, hl)
    return (hl)


def recurse2(t, hl):
    """Retrieves all the hottest articles."""
    if len(t) == 0:
        return (hl)
    hl.append(t[0]['data']['title'])
    t.pop(0)
    recurse2(t, hl)
    return (hl)
