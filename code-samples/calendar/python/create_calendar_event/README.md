# 🗓️ Create Calendar Event 

Create a calendar event using the Nylas Python SDK and Poetry.

## 📜 Introduction

The `create_calendar_event` project is a Python script that leverages the Nylas Python SDK to read and create calendar events from a Nylas calendar. It's designed to provide a straightforward way to fetch, display, and create calendar events.

## ✨ Features

- Create a calendar event given a calendar id.
- Handle Nylas API errors and edge cases.
- Integrates with Poetry for dependency management.

## ⚙️ Requirements

Before using this project, make sure you have the following prerequisites:

- Python 3.10 or higher
- Make
- Nylas API credentials (Client ID and Client Secret)
- A Nylas Calendar ID
- Writable Calendar Permissions (Ensure that you are attempting to create a calendar event for which you have the necessary write permissions. If you don't have write permissions, you won't be able to create a calendar event.)

## 🔧 Using Make

You can use the `make` command for common development tasks. Here are some useful targets:

- `make venv`: Create a virtual environment.
- `make install`: Generate a `.env` file and install required dependencies.
- `make run`: Run the app using Poetry.
- `make clean`: Remove build, test, coverage, and Python artifacts.

## 🚀 Installation

1. Fork/Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/create_calendar_event.git
    cd create_calendar_event
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


    poetry run create_calendar_event
    Connected Calendars:

    Calendar ID: b7utep4mz2bnblp9un7nf4huz, Name: Emailed events
    Calendar ID: dvr7bn8t2vitjwicq4a0wlmyz, Name: yo.code.inbox@gmail.com
    Calendar ID: c3297qn92ylo1zpia4f5xwpxc, Name: Birthdays
    Calendar ID: f2p46w7r9scde9omji1ofakiq, Name: Holidays in Lebanon

    Event created: {'id': 'c037aujdhhcd0xtqu1vpdz4zx', 'cls': <class 'nylas.client.restful_models.Event'>, 'api': <nylas.client.client.APIClient object at 0x7f6fe21c5030>, 'title': 'Team Meeting', 'description': 'Discuss project progress', 'location': 'Virtual', 'when': {'end_time': 1697904000, 'object': 'timespan', 'start_time': 1697900400}, 'participants': [{'comment': None, 'email': 'oss1@wiseai.dev', 'name': None, 'phone_number': None, 'status': 'noreply'}, {'comment': None, 'email': 'oss2@wiseai.dev', 'name': None, 'phone_number': None, 'status': 'noreply'}], 'calendar_id': 'dvr7bn8t2vitjwicq4a0wlmyz', 'account_id': 'dx1wzoyuv7m1owc5rcfk8bhaj', 'conferencing': None, 'read_only': False, 'busy': True, 'recurrence': None, 'status': 'confirmed', 'master_event_id': None, 'job_status_id': 'r4kpfndfyy3la9lapyb6udzu', 'owner': 'Code Inbox <yo.code.inbox@gmail.com>', 'original_start_time': None, 'object': 'event', 'message_id': None, 'ical_uid': None, 'metadata': None, 'notifications': None, 'event_collection_id': None, 'capacity': None, 'round_robin_order': None, 'visibility': None}

    Event ID: c92mwkdflwoati4d9mqshp074, Title: Nylas Calendar Testing, Start Time: 1970-01-01 00:00:00, End Time: 1970-01-01 00:00:00
    Event ID: a78lwinreqpjwctfzost31y33, Title: Team Meeting, Start Time: 2023-10-21 15:00:00, End Time: 2023-10-21 16:00:00
    Event ID: 10sd4nkwkcvaxvpafaaq4rszr, Title: Team Meeting, Start Time: 2023-10-21 15:00:00, End Time: 2023-10-21 16:00:00
    Event ID: dick3o1il1hovyswnqoit0rd0, Title: Team Meeting, Start Time: 2023-10-21 15:00:00, End Time: 2023-10-21 16:00:00
    Event ID: 3s62glyr7fhew4vn9arxb05ek, Title: Team Meeting, Start Time: 2023-10-21 15:00:00, End Time: 2023-10-21 16:00:00
    Event ID: 8pn8g4tvx7b301t9k2hxueda6, Title: Team Meeting, Start Time: 2023-10-21 15:00:00, End Time: 2023-10-21 16:00:00
    Event ID: bfbn01g8a31c4o2md8mqgiziv, Title: Team Meeting, Start Time: 2023-10-21 15:00:00, End Time: 2023-10-21 16:00:00
    Event ID: 7llw323dzocdfg0xxidpzmz90, Title: Team Meeting, Start Time: 2023-10-21 15:00:00, End Time: 2023-10-21 16:00:00
    Event ID: c037aujdhhcd0xtqu1vpdz4zx, Title: Team Meeting, Start Time: 2023-10-21 15:00:00, End Time: 2023-10-21 16:00:00
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
