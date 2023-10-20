# Creating Webhook using Nylas Python v3 SDK

## Setup

1. Install dependencies

```bash
pip install nylas --pre
pip install python-dotenv
```

2. Create .env file inside for Nylas configuration environmental variables

```bash
API_KEY="YOUR_API_KEY"
CALLBACK_URL="CALLBACK_URL"
```

3. Your callback url needs to be in the following format

```bash
"https://your-server.com/webhook"
```

## Usage

Run the python script

```bash
python create_webhook.py
```
