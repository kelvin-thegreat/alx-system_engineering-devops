#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles of the first 10 hot post """
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)

""" Example usage """
subreddit_name = "programming"
print(f"Top 10 hot posts on r/{subreddit_name}:")
top_ten(subreddit_name)

