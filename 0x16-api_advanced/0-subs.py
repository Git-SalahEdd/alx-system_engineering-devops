#!/usr/bin/python3
""" module of the function number_of_subscribers """

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit using
    the Reddit API.

    Args:
        subreddit (str): The name of the subreddit for which to
        retrieve subscriber count.

    Returns:
        int: The number of subscribers for the specified subreddit,
        or 0 if not found or an error occurs.
    """
    if subreddit is None:
        return 0
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) \
        Gecko/20100101 Firefox/73.0"}

    response = requests.get(url, headers=headers, allow_redirects=False).json()

    return response.get("data", {}).get("subscribers", 0)
