# 🗓️ Update Calendar Event 

Update a calendar event using the Nylas Python SDK and Poetry.

## 📜 Introduction

The `update_calendar_event` project is a Python script that leverages the Nylas Python SDK to read and update calendar events from a Nylas calendar. It's designed to provide a straightforward way to fetch, display, and update calendar events.

## ✨ Features

- Update a calendar event given an event id and a calendar id.
- Handle Nylas API errors and edge cases.
- Integrates with Poetry for dependency management.

## ⚙️ Requirements

Before using this project, make sure you have the following prerequisites:

- Python 3.10 or higher
- Make
- Nylas API credentials (`'API_KEY'` and `'GRANT_ID'`)
- A Nylas Calendar ID and an Event ID

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
    cd nylas-hacktoberfest-2023/code-samples/calendar-event/python/update_calendar_event
    ```

1. Set up a virtual environment and activate it:

    ```bash
    make venv
    ```

1. Install project dependencies using Poetry:

    ```bash
    make install
    ```

1. Configure your Nylas API credentials in the `.env` file by setting your `'API_KEY'` and `'GRANT_ID'`  with your actual credentials.

## 🏁 Getting Started

After completing the installation steps, you're ready to get started:

1. Run the script to update calendar:

    ```bash
    make run
    ```

Read the on-screen information and copy a calendar id and one of its events ids to update it using these ids.

    ```bash
    *** Running the app locally... ***


    poetry run update_calendar_event
    Connected Calendars:

    Calendar ID: mahmoudddharmouchhh@gmail.com, Name: mahmoudddharmouchhh@gmail.com, Description: None
    Calendar ID: en.lb#holiday@group.v.calendar.google.com, Name: Holidays in Lebanon, Description: Holidays and Observances in Lebanon
    Calendar ID: addressbook#contacts@group.v.calendar.google.com, Name: Birthdays, Description: Displays birthdays, anniversaries, and other event dates of people in Google Contacts.
    Calendar ID: n1rd0h727dk44lva57qnbbeis8@group.calendar.google.com, Name: test, Description: test description
    Calendar ID: co9ko6p4qbd5fvh7i55urnvf5s@group.calendar.google.com, Name: test, Description: test description
    Calendar ID: tfnid9uts44nb1bqku4bednt14@group.calendar.google.com, Name: test-update, Description: Updated test description

    Getting events before event update for Calendar 'test-update':

    Event id: c7c5ccevt3agepcccv1an05sec, Event title: Team Meeting, start time: 2023-10-01 00:00:00, end time: 2024-10-20 23:59:59

    Event Update: True


    Getting events after event update for Calendar 'test-update':

    Event id: c7c5ccevt3agepcccv1an05sec, Event title: Team Meeting Update, start time: 2023-10-01 00:00:00, end time: 2024-10-20 23:59:59
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
