# Update Webhook with Nylas Python v3 SDK

1. Install dependencies

```
pip install python-dotenv
pip install nylas==6.0.0b4
```

2. Create .env file with configuration parameter from Nylas

```bash
NYLAS_API_KEY = XXXXX
CALLBACK_URL = XXXXX
```

3. Update the 'webhook_id' variable in the **update_webhook.py** file and include the webhook id to be update

```bash
webhook_id = "XXXXXXXX"
```

4. Update the request body with the relevant parameters

```bash
request_body = {
    "callback_url": CALLBACK_URL (defined in .env file),
    "description": description of the update request,
    "notification_email_address": your notification email address,
    "trigger_types": list of trigger_types of the update request
}

```

*Available trigger types for v3 can be found here:* https://developer.nylas.com/docs/developer-guide/v3-webhooks/#trigger-types-available-in-v3-beta


## Usage

Run the python script

```bash
python update_webhook.py
```
