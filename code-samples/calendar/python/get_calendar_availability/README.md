# 🗓️ Get Calendar Availability 

Get calendar availability using the Nylas Python SDK and Poetry.

## 📜 Introduction

The `get_calendar_availability` project is a Python script that leverages the Nylas Python SDK to get calendar availability within a time range from a Nylas calendar. It's designed to provide a straightforward way to get calendar availability within a time range.

## ✨ Features

- Get calendar availability within a time range.
- Handle Nylas API errors and edge cases.
- Integrates with Poetry for dependency management.

## ⚙️ Requirements

Before using this project, make sure you have the following prerequisites:

- Python 3.10 or higher
- Make
- Nylas API credentials (`'API_KEY'` and `'GRANT_ID'`)

## 🔧 Using Make

You can use the `make` command for common development tasks. Here are some useful targets:

- `make venv`: Create a virtual environment.
- `make install`: Generate a `.env` file and install required dependencies.
- `make run`: Run the app using Poetry.
- `make clean`: Remove build, test, coverage, and Python artifacts.

## 🚀 Installation

1. Fork/Clone this repository to your local machine:

    ```bash
    git clone https://github.com/nylas-samples/nylas-hacktoberfest-2023.git
    cd nylas-hacktoberfest-2023/code-samples/calendar/python/get_calendar_availability
    ```

1. Set up a virtual environment and activate it:

    ```bash
    make venv
    ```

1. Install project dependencies using Poetry:

    ```bash
    make install
    ```

1. Configure your Nylas API credentials in the `.env` file by setting your `'API_KEY'` and `'GRANT_ID'` with your actual credentials.

## 🏁 Getting Started

After completing the installation steps, you're ready to get started:

1. Run the script to get calendar availability:

    ```bash
    make run
    ```

Read the on-screen information (at the moment, there is a big in the endpoint).

    ```bash
    *** Running the app locally... ***


    poetry run get_calendar_availability
    Error while fetching calendar availability: Unrecognized request URL (POST: /v3/grants/<your_grant_id>/calendar/availability). Please see https://developer.nylas.com/docs/api/v3-beta/ or we can help at https://support.nylas.com/.
    None
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
