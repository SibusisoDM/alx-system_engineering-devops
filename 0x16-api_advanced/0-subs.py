#!/usr/bin/python3
# queries the Reddit API and returns the number of subscribers

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 302:
            return 0
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0

