#!/usr/bin/python3
"""Sub count"""


import requests
import json


def number_of_subscribers(subreddit):
    """Gets the number of subscribers.
    auth = requests.auth.HTTPBasicAuth('<CLIENT_ID>', '<SECRET_TOKEN>')
    data = {'grant_type': 'password',
            'username': '<USERNAME>',
            'password': '<PASSWORD>'}"""
    headers = {'User-Agent': 'Chrome/110.0.5481.105', 'allow_redirects': 'False'}
    """
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                                auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    """
    u = "https://www.reddit.com/r/" + subreddit + "/about.json?limit=100&t=all"
    try:
        req = requests.get(u, headers=headers, allow_redirects=False)
        return (req.json()['data']['subscribers'])
    except KeyError:
        return (0)
