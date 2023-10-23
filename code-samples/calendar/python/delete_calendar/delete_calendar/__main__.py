import os

import nylas
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

from nylas.models.calendars import ListCalendersQueryParams
from nylas.models.errors import NylasApiError

# Load environment variables from a .env file
load_dotenv()


def display_calendar_ids(client: nylas.Client) -> None:
    """
    Retrieve and display the Calendar IDs and names of connected calendars.

    This function authenticates with the Nylas account using the provided credentials and
    fetches the list of connected calendars. It then displays the Calendar IDs, names, and
    descriptions of the calendars.

    Note:
        Ensure that you have set up your Nylas application with the required credentials
        ('API_KEY' and 'GRANT_ID').

    Args:
        client (nylas.Client): An instance of the Nylas Client.

    Raises:
        Exception: If there is an error during the calendar retrieval process.
    """
    try:
        # Get a list of connected calendars
        query_params = ListCalendersQueryParams(limit=10)

        calendars, _, _ = client.calendars.list(
            identifier=os.environ.get("GRANT_ID"), query_params=query_params
        )

        if calendars:
            print("Connected Calendars:\n")
            for calendar in calendars:
                print(
                    f"Calendar ID: {calendar.id}, Name: {calendar.name}, Description: {calendar.description}"
                )
        else:
            print("No connected calendars found.")

    except NylasApiError as e:
        print(f"Nylas Error: {e}")


def delete_calendar(client: nylas.Client, calendar_id: str) -> bool:
    """
    Delete a calendar using the Nylas Python SDK.

    Args:
        client (nylas.Client): An instance of the Nylas Client.
        calendar_id (str): The ID of the calendar to be deleted.

    Returns:
        bool: True if the calendar was successfully deleted, False otherwise.

    Raises:
        Exception: If there's an error while interacting with the Nylas API.
    """
    try:
        # Delete the calendar by its ID
        client.calendars.destroy(
            calendar_id=calendar_id, identifier=os.environ.get("GRANT_ID")
        )
        return True
    except NylasApiError as e:
        print(f"Nylas Error: {e}")
        return False


def main() -> None:
    try:
        # Initialize the Nylas client with API_KEY environment variable
        client = nylas.Client(
            api_key=os.environ.get("API_KEY"),
        )
        # create a test calendar
        client.calendars.create(
            identifier=os.environ.get("GRANT_ID"),
            request_body={
                "name": "test",
                "description": "test description",
            },
        )
        # display all calendar ids
        print("\nCalendars before delete:\n")
        display_calendar_ids(client)
        # Replace with your actual calendar ID
        calendar_id = "g0oi8mfkvnr9hgiqscsda17vlg@group.calendar.google.com"

        success = delete_calendar(client, calendar_id)
        success = delete_calendar(client, calendar_id)
        if success:
            print("Calendar deleted successfully.")
        else:
            print("Failed to delete the calendar.")
        print("\nCalendars after delete:\n")
        display_calendar_ids(client)
    except NylasApiError as e:
        print(f"Nylas Error: {e}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
