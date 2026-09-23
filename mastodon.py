import requests
from datetime import datetime as dt, timezone
from config import *

def get_matching_posts():
    matching_posts = []
    extra_stats = {}
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
    posts = []

    # Reverse raw posts to have oldest first
    posts_raw_rev = list(reversed(posts_raw))

    for post in posts_raw_rev:
        if dt.fromisoformat(post['created_at'])>date_latest:
            posts.append(post)

    extra_stats["new"] = len(posts)

    for post in posts:
        for keyword in sale_keywords:
            if keyword in post['content'].lower():
                matching_posts.append(post)
                break
        if posts:
            write_date(post['created_at'])

    extra_stats["matching"] = len(matching_posts)
    return matching_posts, extra_stats
