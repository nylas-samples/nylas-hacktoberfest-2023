## Python Calendar Event Delete Nylas v3
This is the sample code for deleting the calendar events using Nylas Python SDK v3.

## Setup

### System Dependencies
- Python v3.x

### Gather environment variables

You'll need the following values:

```text
API_KEY = ""
GRANT_ID = ""
```

Add the above values to a new `.env` file:

```bash
$ touch .env # Then add your env variables
```

### Install dependencies

```bash
$ pip install -r requirements.txt
```

## Usage

Run the script using the `python` command:

```bash
$ python delete_event.py
```

You'll see your listed calendars, then input the index value of the calendar you want to choose. Once done, it'll fetch the calendar events of that specific calendar. You can input the index value of whatever event you want to delete. If the event is not read_only, it shall be deleted and you'll see the following text:-

```text
Event deleted successfully!
```

## Learn more

Visit our [Nylas API v3 documentation](https://developer.nylas.com/docs/v3-beta/) to learn more.
