# 🗓️ Update Calendar Event 

Update a calendar event using the Nylas Python SDK and Poetry.

## 📜 Introduction

The `update_calendar_event` project is a Python script that leverages the Nylas Python SDK to read and update calendar events from a Nylas calendar. It's designed to provide a straightforward way to fetch, display, and update calendar events.

## ✨ Features

- Update a calendar event given an event id.
- Handle Nylas API errors and edge cases.
- Integrates with Poetry for dependency management.

## ⚙️ Requirements

Before using this project, make sure you have the following prerequisites:

- Python 3.10 or higher
- Make
- Nylas API credentials (Client ID and Client Secret)
- A Nylas Calendar and Event ID

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
    cd nylas-hacktoberfest-2023/code-samples/calendar/python/update_calendar_event
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


    poetry run update_calendar_event
    Connected Calendars:

    Calendar ID: mahmoudddharmouchhh@gmail.com, Name: mahmoudddharmouchhh@gmail.com, Description: None
    Calendar ID: en.lb#holiday@group.v.calendar.google.com, Name: Holidays in Lebanon, Description: Holidays and Observances in Lebanon
    Calendar ID: addressbook#contacts@group.v.calendar.google.com, Name: Birthdays, Description: Displays birthdays, anniversaries, and other event dates of people in Google Contacts.
    Calendar ID: 8t4pnfu73fdiv73qreji1d2j5534dmbl@import.calendar.google.com, Name: Coursera Calendar - Mahmoud Harmouch - mahmoudddharmouchhh@gmail.com, Description: None
    Calendar ID: n1rd0h727dk44lva57qnbbeis8@group.calendar.google.com, Name: test, Description: test description
    Calendar ID: co9ko6p4qbd5fvh7i55urnvf5s@group.calendar.google.com, Name: test, Description: test description
    Calendar ID: tfnid9uts44nb1bqku4bednt14@group.calendar.google.com, Name: test-update, Description: Updated test description

    Getting events before event update for Calendar 'Holidays in Lebanon':

    Event ID: 20231029_vabqu54s35oscpe0c4vrpa1ge8, Title: Daylight Saving Time ends, Date: 2023-10-29
    Event ID: 20231101_kmkmk16d13k9eujfo6a6e35pjs, Title: All Saints' Day, Date: 2023-11-01
    Event ID: 20231122_0jde09qqr52tjc799p6va0utog, Title: Independence Day, Date: 2023-11-22
    Event ID: 20231225_p5bj5vkffcn43i4k3iera3nqi0, Title: Christmas Day, Date: 2023-12-25
    Event ID: 20240101_n3v98pm4u92lr6lm7iveq1cuno, Title: New Year, Date: 2024-01-01
    Event ID: 20240106_6pag1jetl9itovsah5p5dbgj9c, Title: Orthodox Christmas, Date: 2024-01-06
    Event ID: 20240209_nmgj4fjqh9e22jep0f9b0crlo0, Title: St Maron's Day, Date: 2024-02-09
    Event ID: 20240214_1jset7t0e4dnrtcv3c2fcmb4hc, Title: Commemoration of the Assasination of PM Rafic Hariri, Date: 2024-02-14
    Event ID: 20240309_r7394l4jpq2e3gadrasahfa7uk, Title: Teachers' Day, Date: 2024-03-09
    Event ID: 20240311_rde04plhnbp5lvl545himtieno, Title: Ramadan Start, Date: 2024-03-11
    Event ID: 20240321_mgrl7k4gcru26e3vuiicd6f8lg, Title: Mother's Day, Date: 2024-03-21
    Event ID: 20240325_j317tit4na5vov3ddkgb431h9s, Title: Feast of the Annunciation, Date: 2024-03-25
    Event ID: 20240329_c7ij4kmu32mbp7blsdob6cqss8, Title: Good Friday, Date: 2024-03-29
    Event ID: 20240331_eis398fog9t0do5gi7lfad9huo, Title: Daylight Saving Time starts, Date: 2024-03-31
    Event ID: 20240401_b43ikfevomk2d2487l905lrb3o, Title: Easter Monday, Date: 2024-04-01
    Event ID: 20240410_8usc9m0q1llaedug9km0magm5k, Title: Eid al-Fitr, Date: 2024-04-10
    Event ID: 20240411_mctqbffr0brik7i2cvf0h7151o, Title: Eid ul Fitr Holiday, Date: 2024-04-11
    Event ID: 20240501_9l3e03vgkkfhf3ak25a6n1imos, Title: Labor Day, Date: 2024-05-01
    Event ID: 20240503_au947ei7j7t16shff28g32f4tc, Title: Orthodox Good Friday, Date: 2024-05-03
    Event ID: 20240505_jltlnsbrec2h1mtbtsa49a6ss0, Title: Orthodox Easter Day, Date: 2024-05-05
    Error update event: Not Found

    Event Update: False


    Getting events after event update for Calendar 'Holidays in Lebanon':

    Event ID: 20231029_vabqu54s35oscpe0c4vrpa1ge8, Title: Daylight Saving Time ends, Date: 2023-10-29
    Event ID: 20231101_kmkmk16d13k9eujfo6a6e35pjs, Title: All Saints' Day, Date: 2023-11-01
    Event ID: 20231122_0jde09qqr52tjc799p6va0utog, Title: Independence Day, Date: 2023-11-22
    Event ID: 20231225_p5bj5vkffcn43i4k3iera3nqi0, Title: Christmas Day, Date: 2023-12-25
    Event ID: 20240101_n3v98pm4u92lr6lm7iveq1cuno, Title: New Year, Date: 2024-01-01
    Event ID: 20240106_6pag1jetl9itovsah5p5dbgj9c, Title: Orthodox Christmas, Date: 2024-01-06
    Event ID: 20240209_nmgj4fjqh9e22jep0f9b0crlo0, Title: St Maron's Day, Date: 2024-02-09
    Event ID: 20240214_1jset7t0e4dnrtcv3c2fcmb4hc, Title: Commemoration of the Assasination of PM Rafic Hariri, Date: 2024-02-14
    Event ID: 20240309_r7394l4jpq2e3gadrasahfa7uk, Title: Teachers' Day, Date: 2024-03-09
    Event ID: 20240311_rde04plhnbp5lvl545himtieno, Title: Ramadan Start, Date: 2024-03-11
    Event ID: 20240321_mgrl7k4gcru26e3vuiicd6f8lg, Title: Mother's Day, Date: 2024-03-21
    Event ID: 20240325_j317tit4na5vov3ddkgb431h9s, Title: Feast of the Annunciation, Date: 2024-03-25
    Event ID: 20240329_c7ij4kmu32mbp7blsdob6cqss8, Title: Good Friday, Date: 2024-03-29
    Event ID: 20240331_eis398fog9t0do5gi7lfad9huo, Title: Daylight Saving Time starts, Date: 2024-03-31
    Event ID: 20240401_b43ikfevomk2d2487l905lrb3o, Title: Easter Monday, Date: 2024-04-01
    Event ID: 20240410_8usc9m0q1llaedug9km0magm5k, Title: Eid al-Fitr, Date: 2024-04-10
    Event ID: 20240411_mctqbffr0brik7i2cvf0h7151o, Title: Eid ul Fitr Holiday, Date: 2024-04-11
    Event ID: 20240501_9l3e03vgkkfhf3ak25a6n1imos, Title: Labor Day, Date: 2024-05-01
    Event ID: 20240503_au947ei7j7t16shff28g32f4tc, Title: Orthodox Good Friday, Date: 2024-05-03
    Event ID: 20240505_jltlnsbrec2h1mtbtsa49a6ss0, Title: Orthodox Easter Day, Date: 2024-05-05
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
