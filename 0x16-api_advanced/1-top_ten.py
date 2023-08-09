#!/usr/bin/python3
"""Reddit Top Ten Hottest Posts"""

import requests

def top_ten(subreddit_name):
    """
    Function that fetches and prints titles of top 10 hottest posts on a given subreddit.
    Args:
        subreddit_name (str): Subreddit to retrieve posts from.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit_name)
    headers = {
        "User-Agent": "Reddit API Client v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }

    res = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    
    posted_data = res.json().get("data")
    for post in posted_data.get("children"):
        posted_title = post.get("data").get("title")
        print(posted_title)

