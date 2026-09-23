# Shodan Sale Notifier

A small Python script that checks Shodan's Mastodon page for announcements about the yearly $5 sale and sends notifications via ntfy.

## Setup

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install the required dependencies.
4. Configure the ntfy topic in config.py (I recommend a string of random characters, since the topics aren't password protected).
5. Run the program.

## ntfy

Create or choose an ntfy topic and subscribe to it on your phone or other device.

The script sends a notification to that topic when it detects a matching Shodan Mastodon post.