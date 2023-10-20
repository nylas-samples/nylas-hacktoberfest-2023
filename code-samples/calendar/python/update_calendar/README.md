# 🗓️ Update Calendar 

Update a calendar using the Nylas Python SDK and Poetry.

## 📜 Introduction

The `update_calendar` project is a Python script that leverages the Nylas Python SDK to read and update calendar from a Nylas calendar. It's designed to provide a straightforward way to fetch, display, and update calendar using its id.

## ✨ Features

- Read and update calendar using its id.
- Handle Nylas API errors and edge cases.
- Integrates with Poetry for dependency management.

## ⚙️ Requirements

Before using this project, make sure you have the following prerequisites:

- Python 3.10 or higher
- Make
- Nylas API credentials (Client ID and Client Secret)
- A Nylas Calendar ID
- Writable Calendar Permissions (Ensure that you are attempting to update calendar from a calendar for which you have the necessary write permissions. If you don't have write permissions, you won't be able to update calendar.)

## 🔧 Using Make

You can use the `make` command for common development tasks. Here are some useful targets:

- `make venv`: Create a virtual environment.
- `make install`: Generate a `.env` file and install required dependencies.
- `make run`: Run the app using Poetry.
- `make clean`: Remove build, test, coverage, and Python artifacts.

## 🚀 Installation

1. Fork/Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/update_calendar.git
    cd update_calendar
    ```

1. Set up a virtual environment and activate it:

    ```bash
    make venv
    ```

1. Install project dependencies using Poetry:

    ```bash
    make install
    ```

1. Configure your Nylas API credentials in the `.env` file by setting your `'CLIENT_ID'`, `'CLIENT_SECRET'`, and `'ACCESS_TOKEN'`  with your actual credentials.

## 🏁 Getting Started

After completing the installation steps, you're ready to get started:

1. Run the script to update calendar:

    ```bash
    make run
    ```

Read the on-screen information and copy a calendar ID to update it using its ID.

    ```bash
    *** Running the app locally... ***


    poetry run update_calendar
    Connected Calendars:

    Calendar ID: b7utep4mz2bnblp9un7nf4huz, Name: Emailed events
    Calendar ID: dvr7bn8t2vitjwicq4a0wlmyz, Name: yo.code.inbox@gmail.com
    Calendar ID: c3297qn92ylo1zpia4f5xwpxc, Name: Birthdays
    Calendar ID: f2p46w7r9scde9omji1ofakiq, Name: Holidays in Lebanon
    Calendar updated successfully.
    ```

## 📚 Documentation

This project includes Google-style documentation within the code. You can find detailed information on how the script works, its functions, and error handling in the script itself.

## 🤝 Contributing

Contributions are welcome! If you would like to improve this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure tests pass.
4. Submit a pull request with a clear description of your changes.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
