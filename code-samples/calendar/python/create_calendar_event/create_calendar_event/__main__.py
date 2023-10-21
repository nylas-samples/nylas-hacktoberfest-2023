import datetime
import os

import nylas
from dotenv import load_dotenv
from nylas.client.errors import NylasError

# Load environment variables from a .env file
load_dotenv()


def create_calendar_event(
    client,
    title,
    location,
    start_time,
    end_time,
    description=None,
    participants=None,
    calendar_id=None,
):
    """
    Create a new calendar event and save it inside a specific calendar.

    Args:
        client (nylas.APIClient): The initialized Nylas API client.
        title (str): The title or name of the event.
        location (str): The location where the event will take place.
        start_time (str): The start time of the event in ISO 8601 format.
        end_time (str): The end time of the event in ISO 8601 format.
        description (str, optional): A description or additional information about the event.
        participants (list, optional): List of participant dictionaries with an "email" field.
        calendar_id (str, optional): The ID of the calendar where the event should be saved.

    Returns:
        nylas.events.Event: The created event object.

    Raises:
        nylas.client.errors.NylasError: If there's an issue with the Nylas API.

    Examples:
        Create a simple event with participants and save it in a specific calendar:
        >>> participants = [{'email': 'oss1@wiseai.dev'}, {'email': 'oss2@wiseai.dev'}]
        >>> event = create_calendar_event(client, 'Meeting', 'Conference Room', '2023-10-21T09:00:00Z', '2023-10-21T10:00:00Z', participants, 'your_calendar_id' )

        Create an event with a description and participants and save it in a specific calendar:
        Create an event with a description and participants and save it in a specific calendar:
        >>> participants = [{'email': 'oss1@wiseai.dev'}, {'email': 'oss2@wiseai.dev'}]
        >>> event = create_calendar_event(client, 'Team Meeting', 'Virtual', '2023-10-21T15:00:00Z', '2023-10-21T16:00:00Z', 'Discuss project progress', participants, 'your_calendar_id')
    """
    try:
        event = client.events.create(
            title=title,
            location=location,
            when={"start_time": start_time, "end_time": end_time},
            description=description,
            participants=participants,
            calendar_id=calendar_id,
        )
        event.save()
        return event
    except NylasError as e:
        raise NylasError(f"Error creating event: {e.message}")


def display_calendar_ids(client):
    """
    Retrieve and display the Calendar IDs and names of connected calendars.
    This function authenticates with the Nylas account using the provided credentials and
    fetches the list of connected calendars. It then displays the Calendar IDs and names
    of the calendars.
    Args:
        client (nylas.APIClient): The initialized Nylas API client.
    Note:
        Ensure that you have set up your Nylas application with the required credentials and
        permissions ('client_id', 'client_secret', 'access token'').
    Raises:
        nylas.client.errors.NylasError: If there is an error during the calendar retrieval process.
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


def get_all_events(client, calendar_id):
    """
    Retrieve all events for a specific calendar.

    Args:
        client (nylas.APIClient): The initialized Nylas API client.
        calendar_id (str): The ID of the calendar to fetch events from.

    Returns:
        list of nylas.events.Event: A list of event objects from the specified calendar.

    Raises:
        nylas.exceptions.NylasException: If there's an issue with the Nylas API.
    """
    try:
        events = client.events.where(calendar_id=calendar_id).all()
        return events
    except NylasError as e:
        raise NylasError(f"Nylas Error: {e.message}")


def main():
    try:
        # Initialize the Nylas client with environment variables
        client = nylas.APIClient(
            client_id=os.environ.get("CLIENT_ID"),
            client_secret=os.environ.get("CLIENT_SECRET"),
            access_token=os.environ.get("ACCESS_TOKEN"),
        )
        # Retrieve all calendars to choose an id to associate an event with it.
        display_calendar_ids(client)
        participants = [{"email": "oss1@wiseai.dev"}, {"email": "oss2@wiseai.dev"}]
        event = create_calendar_event(
            client,
            "Team Meeting",
            "Virtual",
            "2023-10-21T15:00:00Z",
            "2023-10-21T16:00:00Z",
            "Discuss project progress",
            participants,
            "dvr7bn8t2vitjwicq4a0wlmyz",
        )
        print(f"\nEvent created: {event}\n")
        events = get_all_events(client, "dvr7bn8t2vitjwicq4a0wlmyz")
        if events:
            for event in events:
                # Convert the timestamp to a datetime object
                datetime_start = datetime.datetime.utcfromtimestamp(
                    event.when.get("start_time", 0)
                )
                datetime_end = datetime.datetime.utcfromtimestamp(
                    event.when.get("end_time", 0)
                )

                # Format the datetime object as a human-readable string
                human_readable_start_time = datetime_start.strftime("%Y-%m-%d %H:%M:%S")
                human_readable_end_time = datetime_end.strftime("%Y-%m-%d %H:%M:%S")
                print(
                    f"Event ID: {event.id}, Title: {event.title}, Start Time: {human_readable_start_time}, End Time: {human_readable_end_time}"
                )
        else:
            print("No events found in the specified calendar.")
    except NylasError as e:
        raise NylasError(f"Error creating event: {e.message}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
