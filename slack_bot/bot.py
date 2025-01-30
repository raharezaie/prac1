import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Load your bot token from environment variables
slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(channel="#general", text="Hello 
from my bot!")
    print(response)
except SlackApiError as e:
    print(f"Error: {e.response['error']}")

