# node-create-calender

This code sample will show you how to easily create a new calendar with the Nylas Node.js SDK.

## Setup

### System dependences
- Node.js v16x

## Create environment variables

You will need the following values: 

```
API KEY=""
GRANT_ID=""
```

Add the above value to a new ```.env``` file: 
```
$ touch  .env 
```

### Install dependencies
```
$ npm i nylas@beta dotenv
```

## Usage
Run the script using the ```node``` command: 
```
$ node index.js
```

When the calendar is successfully created, you will get the following output in your terminal: 

``` 
Your new calendar was successfully created ♡ Nylas
```

## Learn More
Click [here](https://developer.nylas.com/docs/api/v3-beta/ecc/#post-/v3/grants/-grant_id-/calendars) to learn more about creating a calendar using Nylas.