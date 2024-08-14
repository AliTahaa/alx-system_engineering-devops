#!/usr/bin/python3
""" Module """

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    num_subs = data.get("subscribers")

    return num_subs
