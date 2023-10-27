import os
from dotenv import load_dotenv
from nylas import APIClient


load_dotenv()

CLIENT_ID = os.getenv("NYLAS_CLIENT_ID")
CLIENT_SECRET = os.getenv("NYLAS_CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("NYLAS_ACCESS_TOKEN")

client = APIClient(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN
)

# Specify the webhook ID to be retrieved
webhook_id = "your_webhook_id"

# Retrieve the webhook by its ID
try:
    webhook = client.webhooks.get(webhook_id)
    print("Webhook ID:", webhook.id)
    print("Webhook URL:", webhook.callback_url)
    print("Webhook Triggers:", webhook.trigger_types)
    # Print other webhook properties as needed
except Exception as e:
    print(f"Failed to retrieve webhook. Error: {e}")
