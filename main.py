import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from config import *


app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)


@app.event("message")
def message_handler(body, say):
    text = body["event"].get("text")
    user_id = body["event"].get("user")
    bot_id = app.client.auth_test(token=SLACK_BOT_TOKEN)["user_id"]

    if user_id != bot_id and text:
        print(text)


# Start your app
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
