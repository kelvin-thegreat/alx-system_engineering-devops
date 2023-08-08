#!/usr/bin/python3
"""Reddit Top Ten Hottest Posts"""

import requests

def get_top_ten_posts(subreddit_name):
    """
    Fetches and prints the titles of the 10 hottest posts on a given subreddit.

    Args:
        subreddit_name (str): The name of the subreddit to retrieve posts from.
    """
    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit_name)
    headers = {
        "User-Agent": "Reddit API Client v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    
    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        print("Subreddit not found.")
        return
    
    posts_data = response.json().get("data")
    
    for post in posts_data.get("children"):
        post_title = post.get("data").get("title")
        print(post_title)

""" Example usage """
if __name__ == "__main__":
    subreddit_to_check = "programming"
    get_top_ten_posts(subreddit_to_check)

