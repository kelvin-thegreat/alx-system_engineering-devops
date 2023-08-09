#!/usr/bin/python3
"""
function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """Prints # of subscribers in a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    api_request = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subscriber = api_request.get("data", {}).get("subscribers", 0)
    return subscriber
