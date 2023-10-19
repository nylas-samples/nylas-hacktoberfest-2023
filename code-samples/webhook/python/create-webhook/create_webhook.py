""" 
Nylas v3 Python SDK to create a webhook
"""

import os
import dotenv
from nylas import Client
from nylas.models.webhooks import WebhookTriggers


dotenv.load_dotenv()

API_KEY= os.environ.get("API_KEY")
CALLBACK_URL = os.environ.get("CALLBACK_URL")

# instantiating a client object
client = Client(
    api_key=API_KEY
)

request_body = {
    "trigger_types": [WebhookTriggers.EVENT_CREATED],
    "description": "sdk demo event created",
    "callback_url": CALLBACK_URL,
    "notification_email_address": "sharsha315@gmail.com"
}

# creating webhooks
try:
    response = client.webhooks.create(
        request_body=request_body
    )
except Exception as e:
    print (e)
