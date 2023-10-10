# Updating Calendar Event with Node SDK

## Setup

1) In the root folder, create a .env file with the following fields to ensure correct nylas configuration. Get these from your Nylas dashboard.

```bash
  CLIENT_ID=""
  CLIENT_SECRET=""
  ACCESS_TOKEN=""
```

2) Install dependencies using npm:

```bash
  npm install
```

3) Enter the following field values according to your requirements in ``index.js``:
   - event.title = '<Updated Event Title>';
   - event.location = '<Updated Location>';
   - event.description = '<Updated Description>';

4) If you want to update more/ different fields, add your own field with its value like ``event.<property> = '<Updated Event Property>'``. Log these updated fields in your terminal using ``console.log()``. 

## Usage

Run the script using the npm:

```bash
  npm start
```

## Output
If your .env file's fields are valid, the event should be updated successfully and you should be able to see the following output:

```bash
  Event updated successfully
  Updated Title: <Updated title>
  Updated Location: <Updated location>
  Updated Description: <Updated description>
```

In case any error occurs, it will be visible as the following output:

```bash
  Error: <error>
```
