import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers on a given Reddit subreddit.

    Args:
        subreddit (str): Name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit doesn't exist.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "YourScriptName v1.0.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get("data")
        return data.get("subscribers", 0)
    except requests.exceptions.RequestException:
        return 0


def check_subreddit(subreddit):
    """
    Checks if a subreddit exists and prints "OK" if it does.

    Args:
        subreddit (str): Name of the subreddit to check.
    """
    if number_of_subscribers(subreddit) > 0:
        __builtins__.print("OK")


check_subreddit("existing_subreddit")
check_subreddit("nonexistent_subreddit")
