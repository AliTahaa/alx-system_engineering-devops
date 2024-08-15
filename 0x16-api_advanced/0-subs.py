#!/usr/bin/python3
""" Module """


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns number of subscribers"""
    import requests

    raw_sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                                .format(subreddit),
                                headers={"User-Agent": "My-User-Agent"},
                                allow_redirects=False)
    if raw_sub_info.status_code >= 300:
        return 0

    return raw_sub_info.json().get("data").get("subscribers")
