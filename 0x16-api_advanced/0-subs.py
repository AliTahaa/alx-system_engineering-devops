#!/usr/bin/python3
""" Module """

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    else:
        return 0
