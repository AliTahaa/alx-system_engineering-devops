#!/usr/bin/python3
"""Module to query the Reddit API and return the top 10 hot posts"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and returns the top 10 hot posts of a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    try:
        response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print('None')
        return

    try:
        data = response.json().get("data", {}).get("children", [])
    except ValueError:
        print('None')
        return

    if not data:
        print('None')
        return

    for child in data:
        print(child.get("data", {}).get("title"))
