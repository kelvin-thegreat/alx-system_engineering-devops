#!/usr/bin/python3
""" Count_words function/Module"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries Reddit API, prints sorted keyword count.

    Args:
        subreddit (str): The name of the subreddit to retrieve articles from.
        word_list (list): A list of keywords to count.
        after (str): Identifier for the next page of results.
        word_count (dict): Dictionary to store keyword counts.

    Returns:
        None
    """
    if word_count is None:
        word_count = {}
    
    base_url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "Reddit API Client v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 100,
        "after": after
    }
    
    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    results = response.json().get("data")
    after = results.get("after")
    
    for post in results.get("children"):
        title = post.get("data").get("title").lower()
        for word in word_list:
            if f" {word.lower()} " in f" {title} ":
                word_count[word] = word_count.get(word, 0) + 1

    if after is not None:
        return count_words(subreddit, word_list, after, word_count)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")

"""# Example usage"""
if __name__ == "__main__":
    subreddit_to_check = "programming"
    keywords_to_count = ["python", "java", "javascript"]
    count_words(subreddit_to_check, keywords_to_count)

