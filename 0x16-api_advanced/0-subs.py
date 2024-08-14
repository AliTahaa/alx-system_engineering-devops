#!/usr/bin/python3
""" Module to fetch the number of subscribers from a subreddit """

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns number of
    subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyApp/0.1 by YourUsername"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the status code indicates a successful request
        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                return data.get("subscribers", 0)

        # If the subreddit doesn't exist or is invalid, return 0
        return 0

    except requests.exceptions.RequestException:
        # Catch any request-related exceptions and return 0
        return 0
