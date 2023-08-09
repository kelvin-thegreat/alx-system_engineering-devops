#!/usr/bin/python3
"""  recursive function that queries the Reddit API """
import requests


def count_words(subreddit, listed_words, list_found=[], after=None):
    """Prints counts of words found.

    Args:
        subreddit (str): subreddit to search.
        listed_words (list): words to search for in post titles.
        list_found (obj): value pairs of words.
        after (str): The next page of the API results.
    """
    agent = {'User-agent': 'test45'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=agent)
    if after is None:
        listed_words = [word.lower() for word in listed_words]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in listed_words:
                    list_found.append(word)
        if aft is not None:
            count_words(subreddit, listed_words, list_found, aft)
        else:
            result = {}
            for word in list_found:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
