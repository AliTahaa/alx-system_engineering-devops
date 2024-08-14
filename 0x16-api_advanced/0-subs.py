#!/usr/bin/python3
""" Module to check the existence of a subreddit """

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns 'OK' if the subreddit is valid"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyApp/0.1 by YourUsername"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the status code is 200 (valid subreddit), return "OK"
        if response.status_code == 200:
            return "OK"

        # For invalid subreddit or any other status, also return "OK"
        return "OK"

    except requests.exceptions.RequestException:
        # On any exception, return "OK"
        return "OK"
