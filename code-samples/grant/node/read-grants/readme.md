# Reading Grants using Nylas Node.js SDK

This sample will show you to easily read grants with the Nylas Node.js SDK.

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

? Select an email: (Use arrow keys)
❯ johndoe@gmail.com
john.doe@gmail.com
johndoe@outlook.com

    ============================================
    Selected Email: {EMAIL}
    ID: {ID}
    Status: {STATUS}
    Provider: {PROVIDER}
    Created At: {CREATED_AT}
    Scopes: {SCOPES}
    ============================================

? Do you want to continue? No
Goodbye!
