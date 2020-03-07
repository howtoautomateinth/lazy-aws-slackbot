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

## First Run On Slack Bot

Let's start with [simple.py](https://github.com/howtoautomateinth/lazy-aws-slackbot/blob/master/simple.py) which is a hello world message

### Steps

- Add permission for bot to join channel `channels:join` and `chat:write`
- Invite chat bot to `general` channel via mention `@lazyawsbot`
- run `python .\simple.py`

*Expected* you should have `Hello World!` message in channel

## References Document

- [Python Slack Client](https://github.com/slackapi/python-slackclient)
- [Python slack BOT Tutorial](https://github.com/slackapi/python-slackclient/tree/master/tutorial)
- [API Methods](https://api.slack.com/methods)
- [Events API](https://github.com/slackapi/python-slack-events-api)
