# Read Webhook with Nylas Python v3 SDK

1. Install dependencies

```
pip install python-dotenv
pip install nylas
```

2. Create .env file with configuration parameters from Nylas

```bash
NYLAS_CLIENT_ID = XXXXX
NYLAS_CLIENT_SECRET = XXXXX
NYLAS_ACCESS_TOKEN = XXXXX
```

3. Update the 'webhook_id' variable in the **read_webhook.py** file and include the webhook id to be read

```bash
webhook_id = "XXXXXXXX"
```

## Usage

Run the python script

```bash
python read_webhook.py
```
