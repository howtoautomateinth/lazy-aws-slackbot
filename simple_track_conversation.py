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

# For simplicity we'll store our app data in-memory with the following data structure.
conversation_tracking = []

@slack_events_adapter.on("app_mention")
def lazy_aws_bot(payload):
    
    global conversation_tracking
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    if 'AWS' in text:
        
        # check user id first prevent duplicated
        user_list_id = [user_list_id.get('user_id') for user_list_id in conversation_tracking]
        if user_id not in user_list_id:
            conversation_tracking.append({'user_id': user_id,'channel_id': channel_id})
            
            slack_web_client.chat_postMessage(
                channel=channel_id,
                text=f"Hi <@{user_id}>! How can I help you today?"
            )
        else:
            slack_web_client.chat_postMessage(
                channel=channel_id,
                text=f"Yes Yes <@{user_id}>! I'm here .. How can I help you?"
            )
        

@slack_events_adapter.on("message")
def tracking_msg(payload):
    
    global conversation_tracking
    switcher = {
        'show instance':0,
        'delete instance':1,
        'create instance':2,
    }

    event = payload.get("event", {})

    user_id = event.get("user")
    text = event.get("text")

    # check user id first prevent duplicated
    user_list_id = [user_list_id.get('user_id') for user_list_id in conversation_tracking]
    if user_id in user_list_id:
        choice = switcher.get(text.lower(), 'nothing')
        if choice != 'nothing':
            # send request to AWS Gateway
            print('choice --> {0}'.format(choice))


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)