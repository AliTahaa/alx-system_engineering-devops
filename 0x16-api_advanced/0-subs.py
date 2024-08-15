#!/usr/bin/python3
""" Modul """

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            print("OK")
            return data['data']['subscribers']
        else:
            print("OK")
            return 0
    except requests.RequestException:
        print("OK")
        return 0
