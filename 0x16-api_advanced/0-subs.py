#!/usr/bin/python3
""" Module """

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns number of subscribers"""
    try:
        raw_sub_info = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={"User-Agent": "My-User-Agent-v1.0"},
            allow_redirects=False
        )
        raw_sub_info.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

    return raw_sub_info.json().get("data", {}).get("subscribers", 0)
