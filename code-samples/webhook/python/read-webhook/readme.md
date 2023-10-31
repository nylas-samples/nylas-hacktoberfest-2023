# Read Webhook with Nylas Python v3 SDK

1. Install dependencies

```
pip install python-dotenv
pip install nylas
```

2. Create .env file with configuration parameter from Nylas

```bash
NYLAS_API_KEY = XXXXX
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
