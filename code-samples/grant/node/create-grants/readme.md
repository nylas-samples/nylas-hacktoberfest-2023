# Creating Grants using Nylas Node.js SDK

This sample will show you to easily create grants with the Nylas Node.js SDK.

## Setup

### 1. In the root folder, create a `.env` file with your nylas configuration as follow:

```
API_KEY="YOUR_API_KEY"
CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"
```

### 2. Install dependencies

```bash
npm install
```

## Usage

Run the following command and go to `http://localhost:3000/oauth`

```bash
npm start
```

## Output

**ON BROWSER**

```js
{
  accessToken: 'token',
  grantId: 'id',
  email: 'some@gmail.com',
  expiresIn: 3600,
  idToken: 'token',
  tokenType: 'Bearer',
  scope: 'scope1 scope2'
}
```

**TERMINAL OUTPUT**

`GRANT ID: <GRANT_ID>`
