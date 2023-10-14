""" 
Nylas v3 Python SDK to create a webhook
"""

import os
import dotenv
import json
import nylas
from nylas import Client
from nylas.models.webhooks import WebhookTriggers


dotenv.load_dotenv()

API_KEY= os.environ.get("API_KEY")
print(API_KEY)


# instantiating a client object
client = Client(
    api_key=API_KEY
)


request_body = nylas.models.webhooks.CreateWebhookRequest(
    trigger_types = [WebhookTriggers.EVENT_CREATED],
    description = "sdk demo 1",
    callback_url = "https://eodg8rgla17nx41.m.pipedream.net",
    notification_emai_address = "sharsha315@gmail.com"
    )

try:
    response = client.webhooks.create(
        request_body=request_body
    )
except Exception as e:
    print(e)

