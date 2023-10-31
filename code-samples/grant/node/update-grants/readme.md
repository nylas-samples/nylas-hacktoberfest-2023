# Update Grants using Nylas Node.js SDK

This sample will show you how to easily override the existing grant scopes with the Nylas Node.js SDK.

## Setup

### 1. In the root folder, create a `.env` file with your nylas configuration as follow:

```
API_KEY="NYLAS_API_KEY"
```

### 2. Install dependencies

```bash
npm install
```

## Usage

```bash
npm start
```

## Output

? Please select a Gmail account to update: (Use arrow keys)


❯ johndoe@gmail.com

john.doe@gmail.com

johndoe@outlook.com

? Scopes: (Press <space> to select, <a> to toggle all, <i> to invert selection, and <enter> to proceed)

❯◯ Gmail ReadOnly

◯ Gmail Send

◯ Gmail Modify

◯ Calendar

◯ Contacts

    ❯ Grant updated successfully!

    UPDATED GRANT DETAILS:
    ===============================
    Request ID: {requestId}
    GRANTS ID: {GRANT_ID}
    Email: {EMAIL}
    Scopes: {SCOPES}
    ===============================

? Do you want to update another grant? No

Goodbye!
