# Import your dependencies
import os
from nylas import Client
from dotenv import load_dotenv

# Load your env variables
load_dotenv()

# Set Nylas API_KEY
nylas = Client(
    api_key=os.environ.get("API_KEY")
)

# Set the webhook id to delete (You can use webhooks.list() method in order to see webhooks list)
webhook_to_destroy = os.environ.get("WEBHOOK_TO_DESTROY")

try:
    response = nylas.webhooks.destroy(webhook_to_destroy)
    print('Webhook destroyed succesfully!')
except Exception as e:
    print(f'An error occurred destroying webhook, exception {str(e)}')

# Check Webhook List
try:
    webhooks_list = nylas.webhooks.list()
    for webhook in webhooks_list:
        print(webhook)
except Exception as e:
    print(f'An error occurred, exception {str(e)}')
