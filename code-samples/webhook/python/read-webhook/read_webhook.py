import os
from dotenv import load_dotenv
from nylas import Client


load_dotenv()
API_KEY = os.getenv("NYLAS_API_KEY")

client = Client(api_key=API_KEY)

# Specify the webhook ID to be retrieved
webhook_id = "your_webhook_id"

# Retrieve the webhook by its ID
try:
    webhook = client.webhooks.find(webhook_id)
    print("Webhook ID:", webhook.id)
    print("Webhook URL:", webhook.callback_url)
    print("Webhook Triggers:", webhook.trigger_types)
    print("Webhook Notification email:", webhook.notification_email_address)
    # Print other webhook properties as needed
except Exception as e:
    print(f"Failed to retrieve webhook. Error: {e}")
