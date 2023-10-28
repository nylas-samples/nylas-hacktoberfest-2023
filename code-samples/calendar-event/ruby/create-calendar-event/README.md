# Creating Calendar Event Using Ruby v3 SDK

This code sample will demonstrates, How to create a calendar event using Ruby v3 SDK.


## Setup

### System dependencies
- Ruby v3.x

### Install dependencies

```bash
$ gem install nylas
$ gem install dotenv
```

### Gather environmental variables

You'll need the following values:

```text
API_KEY=
GRANT_ID=
```

Add the above values to a new `.env` file:

```bash
$ touch .env # Then add your env variables
```

You'll also need the Calendar ID, which is obtained by listing the created calendars,
or by creating a new calendar.

## Usage

Run the script using the `ruby` command:

```bash
$ ruby create_event.rb
```