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
    req = requests.get(u, headers=headers)
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


def count_words(subreddit, word_list):
    """Counts keywords in the titles of hot articles of given subreddit."""
    count = []
    t = recurse(subreddit)
    tw = []
    k = 0
    c = 0
    pr = 0
    for i in t:
        tw.append(i.split())
    for i in word_list:
        for j in tw:
            if i in j:
                c = c + 1
                pr = 1
        count.append(c)
        c = 0
        k = k + 1
    for i in range(len(count)):
        if pr == 1 and t is not None:
            print("{}: {}".format(word_list[i], count[i]))
