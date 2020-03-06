import os
import time
import re
import slack
from slack import WebClient

client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])

response = client.chat_postMessage(
    channel='#general',
    text="Hello world!")
assert response["ok"]
assert response["message"]["text"] == "Hello world!"