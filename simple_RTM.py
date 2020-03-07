import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi

app = Flask(__name__)

slack_events_adapter = SlackEventAdapter(os.environ["SLACK_SIGNING_SECRET"], "/slack/events", app)
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

@slack_events_adapter.on("message")
def say_hello(payload):
    
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    if 'Hello' in text:
        slack_web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user_id}>!"
        )

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)