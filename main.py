from notifications import send_notification
from mastodon import get_matching_posts
from datetime import datetime as dt

# Get new posts which fit the keywords
matching_posts, extra_stats = get_matching_posts()
if extra_stats["new"] < 1:
    print("No new posts were found.")
else:
    print(f"Done. {extra_stats["new"]} new posts were searched, {extra_stats["matching"]} containing keyword matches.")

for post in matching_posts:
    send_notification(f"Shodan is on sale!\nLink: {post['url']}")
    print("Notification sent")
