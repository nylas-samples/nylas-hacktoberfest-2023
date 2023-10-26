# Delete Grants using Nylas Node.js SDK

This sample will show you to easily delete grants with the Nylas Node.js SDK.

## Setup

### 1. In the root folder, create a `.env` file with your nylas configuration as follow:

```
API_KEY="YOUR_API_KEY"
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

? Select an email to delete:: (Use arrow keys)
❯ johndoe@gmail.com
john.doe@gmail.com
johndoe@outlook.com

Grants deleted successfully!

DETAILS:

===============================

Request ID: ${requestId}

GRANTS ID: ${answer.grants.id}

Email: ${answer.grants.email}

===============================

? Do you want to delete another grants? No
Goodbye!
