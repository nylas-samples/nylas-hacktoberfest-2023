# delete_webhook

This sample will show you to easily destroy a webhook with the Nylas Python SDK.

You can follow along step-by-step in our blog post ["How to Destroy a Webhook with the Nylas Python SDK"](https://www.nylas.com/blog/category/developers/).

## Setup

### System dependencies

- Python v3.x

### Gather environment variables

You'll need the following values:

```text
API_KEY = ""
WEBHOOK_TO_DESTROY = ""
```

Add the above values to a new `.env` file:

```bash
$ touch .env # Then add your env variables
```

### Install dependencies

```bash
$ pip3 install nylas
$ pip3 install python-dotenv
```

## Usage

Run the script using the `python3` command:

```bash
$ python3 delete_webhook.py
```

When the webhook was deleted, you'll get the following output in your terminal:

```text
Webhook destroyed succesfully!
```

## Learn more

Visit our [Nylas Python SDK documentation](https://developer.nylas.com/docs/v3-beta/) to learn more.
