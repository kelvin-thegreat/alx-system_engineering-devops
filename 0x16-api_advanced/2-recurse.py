#!/usr/bin/python3
"""Recursive function to fetch hot posts from Reddit"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches and returns a list of titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve posts from.
        hot_list (list): A list to accumulate the titles of hot posts.
        after (str): Identifier for the next page of results.

    Returns:
        list: A list containing the titles of all hot posts, or None if the subreddit is invalid.
    """
    base_url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "Reddit API Client v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 100,
        "after": after
    }
    
    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        return None

    results = response.json().get("data")

    if results is None:
        return hot_list
    
    after = results.get("after")
    
    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list

