# SendEventRSVPResponse

This sample will show you to easily send RSVP Response with the Nylas Python SDK.

You can follow along step-by-step in our blog post ["How to Send RSVP Response with the Nylas Python SDK"](https://www.nylas.com/blog/category/developers/).

## Setup

### System dependencies

- Python v3.x

### Gather environment variables

You'll need the following values:

```text
API_KEY = ""
GRANT_ID = ""
CALENDAR_ID = ""
EVENT_ID = ""
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
$ python3 SendEventRSVPResponse.py
```

When your message is successfully sent, you'll get the following output in your terminal:

```text
RSVP Response succeed, request id: 11111111
Event: Nylas RSVP Response Test id: 11111111
Participant: email@test.com status: yes
Participant: email@test2.com status: maybe
```

## Learn more

Visit our [Nylas Python SDK documentation](https://developer.nylas.com/docs/v3-beta/) to learn more.
