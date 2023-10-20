import nylas
from nylas.client.errors import NylasError
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Initialize the Nylas client with environment variables
client = nylas.APIClient(
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET'),
    access_token=os.environ.get('ACCESS_TOKEN')
)

def display_calendar_ids():
    """
    Retrieve and display the Calendar IDs and names of connected calendars.

    This function authenticates with the Nylas account using the provided credentials and
    fetches the list of connected calendars. It then displays the Calendar IDs and names
    of the calendars.

    Note:
        Ensure that you have set up your Nylas application with the required credentials
        ('client_id' and 'client_secret').

    Raises:
        NylasError: If there is an error during the calendar retrieval process.
    """
    try:
        # Get a list of connected calendars
        calendars = client.calendars.all()

        if calendars:
            print("Connected Calendars:\n")
            for calendar in calendars:
                print(f"Calendar ID: {calendar.id}, Name: {calendar.name}")
        else:
            print("No connected calendars found.")

    except NylasError as e:
        raise NylasError(f"Nylas Error: {e.message}")

def read_calendar_events(calendar_id, start_time, end_time):
    """
    Read calendar events within a specified time range.

    Args:
        calendar_id (str): The ID of the calendar to read events from.
        start_time (str): The start time of the range (RFC3339 format, e.g., '2023-01-01T00:00:00Z').
        end_time (str): The end time of the range (RFC3339 format, e.g., '2023-01-31T23:59:59Z').

    Returns:
        list: A list of calendar events within the specified time range.

    Raises:
        NylasError: If there is an error while fetching calendar events.
    """
    try:
        # Get events from the specified calendar within the time range
        filters = {
            'calendar_id': calendar_id,
            #TODO: 'starts_after': start_time,
            #TODO: 'ends_before': end_time,
        }
        events = client.events.where(**filters)

        return list(events)
    except NylasError as e:
        raise NylasError(f"Error while fetching calendar events: {e.message}")

def main():
    try:
        # display all calendar ids
        display_calendar_ids()

        # Replace with your actual calendar ID, start, and end time
        calendar_id = 'f2p46w7r9scde9omji1ofakiq'
        start_time = '2023-10-01T00:00:00Z'
        end_time = '2023-10-20T23:59:59Z'

        events = read_calendar_events(calendar_id, start_time, end_time)
        print("\n Getting events for Calendar 'Holidays in Lebanon':\n")
        for event in events:
            print(f"Event: {event.title}, Date: {event.when['date']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()