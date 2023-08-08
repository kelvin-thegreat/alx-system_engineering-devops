#!/usr/bin/python3
"""
Contains the number_of_subscribers function

"""
import requests

def number_of_subscribers(subreddit):
    if not isinstance(subreddit, str):
        return 0

    url = f'http://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'CustomUserAgent'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    except (requests.RequestException, ValueError):
        return 0

"""# Test the function """
subreddit_name = 'python'
subscribers = number_of_subscribers(subreddit_name)
if subscribers > 0:
    print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")
else:
    print(f"The subreddit '{subreddit_name}' is invalid or inaccessible.")

