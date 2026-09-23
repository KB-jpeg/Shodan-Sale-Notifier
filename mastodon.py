import requests
from datetime import datetime as dt, timezone
from config import *

def get_matching_posts():
    posts_matching = []
    try:
        with open("latest.txt", "r") as f:
            date_latest = dt.fromisoformat(f.read())
    except (ValueError, FileNotFoundError):
        date_latest = dt(1900, 1, 1, tzinfo=timezone.utc)

    def write_date(date):
        with open("latest.txt", "w") as f:
            f.write(date)
        date = dt.fromisoformat(date)

    r = requests.get(
        f"https://mastodon.shodan.io/api/v1/accounts/{account_id}/statuses",
        params={"limit": 20},
        timeout=10
    )

    r.raise_for_status()
    posts_raw = r.json()
    posts_new = []

    # Reverse raw posts to have oldest first
    posts_raw_rev = list(reversed(posts_raw))

    for post in posts_raw_rev:
        if dt.fromisoformat(post['created_at'])>date_latest:
            posts_new.append(post)

    for post in posts_new:
        for keyword in keywords:
            if keyword in post['content'].lower():
                posts_matching.append(post)
                break
        if posts_new:
            write_date(post['created_at'])

    return posts_matching, posts_new
