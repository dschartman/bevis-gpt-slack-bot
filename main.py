from slack_bolt.adapter.socket_mode import SocketModeHandler
from bot.app import app
from bot.config import SLACK_APP_TOKEN

# Start your app
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
