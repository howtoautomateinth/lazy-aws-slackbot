# Lazy AWS BOT

Lazy bot for manipulate AWS instance

*some tutorials on google.com would be different with this tutorial since it different client*

## Prerequisite

- Set up python environment
    - python -m venv slack-env
    - pip install -r requirements.txt
- Sign up [ngrok](https://ngrok.com/) to setup local machine as server
    - because we need local server that subscriptions to slack event
- Create a slack bot on [website](https://api.slack.com/apps) to get token
- Install an `@lazyawsbot` to workspace
- Setup slack bot token
    - depend on your OS then set a token inside script file and execute

## Hello World Slack Bot

Let's start with [simple.py](https://github.com/howtoautomateinth/lazy-aws-slackbot/blob/master/simple.py) which is a hello world message

### Steps

- Add permission for bot to join channel `channels:join` and `chat:write`
- Invite chat bot to `general` channel via mention `@lazyawsbot`
- run `python .\simple.py`

*Expected* you should have `Hello World!` message in channel

## Real Time Messaging (RTM)

is a WebSocket-based API that allows you to receive events from Slack in real time and send messages as users

### Steps

- On VSCode to run with `Simple RTM` debugger mode
- Use ngrok to make a web server tunnel on `ngrok http 3000`
- Grab `ngrok_url + /slack/events` and register on *Event Subscriptions* page in api slack
    - subscribe bot events with `message.channels`
- Add `@lazyawsbot` into #General
- Type `Hello World` and wait for response

## References Document

- [Python slack BOT Tutorial](https://github.com/slackapi/python-slackclient/tree/master/tutorial)
- [API Methods](https://api.slack.com/methods)
- [API Events Methods](https://api.slack.com/events)
- [Python Slack Client](https://github.com/slackapi/python-slackclient)
- [Python Slack Events API](https://github.com/slackapi/python-slack-events-api)
