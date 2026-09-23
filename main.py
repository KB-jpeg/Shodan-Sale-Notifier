from notifications import send_notification
from mastodon import get_matching_posts
from datetime import datetime as dt
from config import *

# Get new posts which fit the keywords
posts_matching, posts_new = get_matching_posts()
if len(posts_new) < 1:
    print("No new posts were found.")
else:
    print(f"Done. {len(posts_new)} new posts have been found, {len(posts_matching)} with matching keywords")

if notify_matching:
    for post in posts_matching:
        send_notification(f"Shodan is on sale!\nLink: {post['url']}")
        print("Notification sent")

if notify_new:
    for post in posts_new:
        send_notification(f"New post from Shodan!\nLink: {post['url']}")
        print("Notification sent")
