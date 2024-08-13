#!/usr/bin/python3
"""function requests from Reddit API to return the
number of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function queries the Reddit API and then returns the number of
    subscribers for a particular subreddit"""
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'User-Agent': 'Mozilla/5.0'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
