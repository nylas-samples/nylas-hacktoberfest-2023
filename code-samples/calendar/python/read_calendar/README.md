# 🗓️ Read Calendar

Read calendar events using the Nylas Python SDK and Poetry.

## 📜 Introduction

The `read_calendar` project is a Python script that leverages the Nylas Python SDK to read calendar events from a Nylas calendar. It's designed to provide a straightforward way to fetch and display calendar events within a specified time range.

## ✨ Features

- Read calendar events within a specific time range.
- Handle Nylas API errors and edge cases.
- Integrates with Poetry for dependency management.

## ⚙️ Requirements

Before using this project, make sure you have the following prerequisites:

- Python 3.10 or higher
- Make
- Nylas API credentials (Client ID and Client Secret)
- A Nylas calendar ID

## 🔧 Using Make

You can use the `make` command for common development tasks. Here are some useful targets:

- `make venv`: Create a virtual environment.
- `make install`: Generate a `.env` file and install required dependencies.
- `make run`: Run the app using Poetry.
- `make clean`: Remove build, test, coverage, and Python artifacts.

## 🚀 Installation

1. Fork/Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/read_calendar.git
    cd read_calendar
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

1. Run the script to read calendar events:

    ```bash
    make run
    ```

Read the on-screen information and copy a calendar ID to read events within the specified time range.

    ```bash
    *** Running the app locally... ***

    poetry run read_calendar
    Connected Calendars:

    Calendar ID: b7utep4mz2bnblp9un7nf4huz, Name: Emailed events
    Calendar ID: dvr7bn8t2vitjwicq4a0wlmyz, Name: yo.code.inbox@gmail.com
    Calendar ID: c3297qn92ylo1zpia4f5xwpxc, Name: Birthdays
    Calendar ID: f2p46w7r9scde9omji1ofakiq, Name: Holidays in Lebanon

    Getting events for Calendar 'Holidays in Lebanon':

    Event: The Prophet's Birthday, Date: 2023-09-27
    Event: Daylight Saving Time ends, Date: 2023-10-29
    Event: All Saints' Day, Date: 2023-11-01
    Event: Independence Day, Date: 2023-11-22
    Event: Christmas Day, Date: 2023-12-25
    Event: New Year, Date: 2024-01-01
    Event: Orthodox Christmas, Date: 2024-01-06
    Event: St Maron's Day, Date: 2024-02-09
    Event: Commemoration of the Assasination of PM Rafic Hariri, Date: 2024-02-14
    Event: Teachers' Day, Date: 2024-03-09
    Event: Ramadan Start, Date: 2024-03-11
    Event: Mother's Day, Date: 2024-03-21
    Event: Feast of the Annunciation, Date: 2024-03-25
    Event: Good Friday, Date: 2024-03-29
    Event: Daylight Saving Time starts, Date: 2024-03-31
    Event: Easter Monday, Date: 2024-04-01
    Event: Eid al-Fitr, Date: 2024-04-10
    Event: Eid ul Fitr Holiday, Date: 2024-04-11
    Event: Labor Day, Date: 2024-05-01
    Event: Orthodox Good Friday, Date: 2024-05-03
    Event: Orthodox Easter Day, Date: 2024-05-05
    Event: Martyr's Day, Date: 2024-05-05
    Event: Orthodox Easter Monday, Date: 2024-05-06
    Event: Ascension Day, Date: 2024-05-09
    Event: Liberation and Resistance Holiday, Date: 2024-05-12
    Event: Liberation and Resistance Day, Date: 2024-05-25
    Event: Eid al-Adha, Date: 2024-06-17
    Event: Eid al-Adha Holiday, Date: 2024-06-18
    Event: Muharram, Date: 2024-07-08
    Event: Ashoura, Date: 2024-07-17
    Event: Assumption of Mary, Date: 2024-08-15
    Event: Nativity of Mary, Date: 2024-09-08
    Event: The Prophet's Birthday, Date: 2024-09-16
    Event: Daylight Saving Time ends, Date: 2024-10-27
    Event: All Saints' Day, Date: 2024-11-01
    Event: Independence Day, Date: 2024-11-22
    Event: Christmas Day, Date: 2024-12-25
    Event: New Year, Date: 2025-01-01
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
