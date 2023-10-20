# 🗓️ Delete Calendar Event 

Delete calendar events using the Nylas Python SDK and Poetry.

## 📜 Introduction

The `delete_calendar` project is a Python script that leverages the Nylas Python SDK to read and delete calendar events from a Nylas calendar. It's designed to provide a straightforward way to fetch, display, and delete calendar events using events ids.

## ✨ Features

- Read and delete calendar events using events ids.
- Handle Nylas API errors and edge cases.
- Integrates with Poetry for dependency management.

## ⚙️ Requirements

Before using this project, make sure you have the following prerequisites:

- Python 3.10 or higher
- Make
- Nylas API credentials (Client ID and Client Secret)
- A Nylas Event ID
- Writable Calendar Permissions (Ensure that you are attempting to delete events from a calendar for which you have the necessary write permissions. If you don't have write permissions, you won't be able to delete events.)

## 🔧 Using Make

You can use the `make` command for common development tasks. Here are some useful targets:

- `make venv`: Create a virtual environment.
- `make install`: Generate a `.env` file and install required dependencies.
- `make run`: Run the app using Poetry.
- `make clean`: Remove build, test, coverage, and Python artifacts.

## 🚀 Installation

1. Fork/Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/delete_calendar.git
    cd delete_calendar
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

1. Run the script to delete calendar events:

    ```bash
    make run
    ```

Read the on-screen information and copy a calendar event ID to delete it using its ID.

    ```bash
    *** Running the app locally... ***


    poetry run delete_calendar
    List of Event IDs:
    8lyufsks2dlxzvh5ads9h3llu
    c92mwkdflwoati4d9mqshp074
    8ubgm7kv9l2v1rxs26k5g397
    5nln0ohex4dn27gmqpe3qgyd8
    7mp9mc8xhiqhdxrz1d016321i
    885cbcl988aascqawtj6h55va
    4ew4b9o6w8gvzziz8dd6zzvxx
    28d6nu7pecfaqqtzgj8jrbmb8
    85shuq74xeim89dk9pzvhzjpm
    ar0xu8r084wrdtket5qcw4bgt
    4wgzheqwxjq5bw6ug31htgio5
    5ej4lyzc58jqhjqz9zrnqgn3x
    25x79a27goaaq5mrwv5084bsi
    6coplhoraf9esccd1kd4zihib
    2hfs2zxz2mzlcoixoj5215aem
    d2orjl3l6vmxrp8kqhu2fv2cr
    a1t8wfj1b8yuvjgju6fga1zob
    bb88xihtatdweg0tgo8plbrvt
    ceyqg4k6t02xlpze3yxsy0r1z
    beo568s8u05ijvcoh9tn2swg5
    2rmt7iktplfmr4v3yp7l9tppz
    axevzyws8x6h351h0ntpq4uzz
    e8m8x8tqrbx5t0ib1rlg0n0fk
    b5n1n1aiv09bfttnrc2vfo2vd
    2l0qncpie7izh31pyu6h7j28h
    6dbs08jm60uxuwjkjik0d5lbf
    42affp9mng41cqvizb3sd5m66
    ahdzncvs8p8zlc4aeczjyd5vo
    atz4qf0gdc3b8yple94uay1y8
    3i7dqq8ty1a14f7vwj1g1aohf
    3pi8qrx2kfyk7lrq5pyzlbe7s
    58u2d5wjvdwsixa5o6gm2lym2
    4o8vwiifs1k7f0b4q99m1cwpm
    138d1bri1gjc5e6kqree5wtl8
    b4mhw2z253riz0e1p7a9xn5au
    e0zanhxx9sgsbv07phttezgss
    7996t2mqe7outp110w3o5xw05
    2jfq861nvqsdjbi18hm1u2luc
    54x6ntmfigid84bcwyv1yh391
    Calendar event deleted successfully.
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
