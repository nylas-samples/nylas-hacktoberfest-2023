# node-read-calendar
This code sample will show you how to read a calendar with the Nylas Node.js SDK.

## Setup
### System dependencies
- Node.js v16x

## Create enviroment variables
You will need the following values: 

```
API_KEY = ""
GRANT_ID=""
CALENDAR_ID=""
```

Add the above values to a new ```.env``` file: 

``` 
$ touch .env 
```

### Install dependencies
``` 
npm i nylas@beta dotenv
```

## Usage
Run the script using the ```node`` command: 
```
$ node index.js
```

When the calendar is successfully read, you will recieve an output of the Calendar object with the matching id.

