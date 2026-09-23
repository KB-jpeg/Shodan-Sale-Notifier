import requests
from config import *

def send_notification(data="Shodan is on sale"):
    requests.post(
        f"https://ntfy.sh/{ntfy_topic}",
        data=data.encode('utf-8'),
        headers={
            "Title": "Shodan Sale",       # Optional: Adds a bold title
            "Priority": "high",            # Optional: max, high, default, low, min
            "Tags": "fire,computer"  # Optional: Adds emojis/icons
        }
    )

