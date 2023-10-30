""" 
Nylas v3 Python SDK to create a webhook
"""

import os
from dotenv import load_dotenv
from nylas import Client
from nylas.models.webhooks import WebhookTriggers


load_dotenv()

API_KEY = os.getenv("NYLAS_API_KEY")
CALLBACK_URL = os.getenv("CALLBACK_URL")

# Specify the ID of the webhook destination to update
webhook_id = "your_webhook_id"

client = Client(api_key=API_KEY)

# The request body to update the webhook destination
request_body = {
    "callback_url": CALLBACK_URL,
    "description": "updating my webhook",
    "notification_email_address": "onwuagbakenenna@gmail.com",
    "trigger_types": [WebhookTriggers.EVENT_UPDATED],
}

try:
    webhook_response = client.webhooks.update(
        webhook_id=webhook_id, request_body=request_body
    )

    # Content of the updated webhook destination
    print("Webhook ID:", webhook_response.id)
    print("Webhook URL:", webhook_response.callback_url)
    print("Webhook Triggers:", webhook_response.trigger_types)
    print("Webhook Notification email:", webhook_response.notification_email_address)
except Exception as e:
    print(e)
