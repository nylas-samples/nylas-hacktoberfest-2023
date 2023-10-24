import os
from datetime import datetime

import nylas
from dotenv import load_dotenv
from nylas.models.calendars import ListCalendersQueryParams
from nylas.models.errors import NylasApiError
from nylas.models.events import (
    CreateEventQueryParams,
    CreateEventRequest,
    ListEventQueryParams,
)

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
        nylas.models.errors.NylasApiError: If there is an error during the calendar retrieval process.
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


def read_calendar_events(
    client: nylas.Client, calendar_id: str, start_time: int, end_time: int
) -> list:
    """
    Read calendar events within a specified time range.

    Args:
        client (nylas.Client): An instance of the Nylas Client.
        calendar_id (str): The ID of the calendar to read events from.
        start_time (int): The start time of the range in Unix timestamp format.
        end_time (int): The end time of the range in Unix timestamp format.

    Returns:
        list: A list of calendar events within the specified time range.

    Raises:
        nylas.models.errors.NylasApiError: If there is an error while fetching calendar events.
    """
    try:
        # Get events from the specified calendar within the time range
        query_params = ListEventQueryParams(
            limit=20, calendar_id=calendar_id, start=start_time, end=end_time
        )

        events, _, _ = client.events.list(
            identifier=os.environ.get("GRANT_ID"), query_params=query_params
        )

        return list(events)
    except NylasApiError as e:
        print(f"Error while fetching calendar events: {e}")


def update_calendar_event(
    client,
    title,
    location,
    start_time,
    end_time,
    description=None,
    participants=None,
    event_id=None,
    calendar_id=None,
) -> bool:
    """
    Update a calendar event and save it inside a specific calendar.

    Args:
        client (nylas.Client): The initialized Nylas API client.
        title (str): The title or name of the event.
        location (str): The location where the event will take place.
        start_time (int): The start time of the range in Unix timestamp format.
        end_time (int): The end time of the range in Unix timestamp format.
        description (str, optional): A description or additional information about the event.
        participants (list, optional): List of participant dictionaries with an "email" field.
        event_id (str, optional): The ID of the event which the event should be updated.
        calendar_id (str, optional): The ID of the calendar in which the event should be updated.

    Returns:
        bool: A boolean type to indicate whether or not the event was updated successfully.

    Raises:
        nylas.client.errors.NylasError: If there's an issue with the Nylas API.

    Examples:
        update a simple event with participants and save it:
        >>> participants = [{'email': 'oss1@wiseai.dev'}, {'email': 'oss2@wiseai.dev'}]
        >>> event = update_calendar_event(client, 'Meeting', 'Conference Room', 1729457999, 1729458000, participants, 'your_event_id', 'your_calendar_id')

        update an event with a description and participants and save it:
        >>> participants = [{'email': 'oss1@wiseai.dev'}, {'email': 'oss2@wiseai.dev'}]
        >>> event = update_calendar_event(client, 'Team Meeting', 'Virtual', 1729457999, 1729458000, 'Discuss project progress', participants, 'your_event_id', 'your_calendar_id')
    """
    try:
        query_params = CreateEventQueryParams(
            calendar_id=calendar_id, notify_participants=True
        )
        client.events.update(
            identifier=os.environ.get("GRANT_ID"),
            event_id=event_id,
            request_body={
                "title": title,
                "description": description,
                "location": location,
                "when": {"start_time": start_time, "end_time": end_time},
                "participants": participants,
            },
            query_params=query_params,
        )
        return True
    except NylasApiError as e:
        print(f"Error update event: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


def main() -> None:
    try:
        # Initialize the Nylas client with API_KEY environment variable
        client = nylas.Client(
            api_key=os.environ.get("API_KEY"),
        )
        # display all calendar ids
        display_calendar_ids(client)

        # Replace with your actual calendar ID, start, and end time
        calendar_id = "tfnid9uts44nb1bqku4bednt14@group.calendar.google.com"
        start_time = "2023-10-01T00:00:00Z"
        start_datetime_obj = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
        start_unix_time = int(start_datetime_obj.timestamp())

        end_time = "2024-10-20T23:59:59Z"
        end_datetime_obj = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ")
        end_unix_time = int(end_datetime_obj.timestamp())
        events = read_calendar_events(
            client, calendar_id, start_unix_time, end_unix_time
        )
        print("\nGetting events before event update for Calendar 'test-update':\n")
        if events:
            for event in events:
                human_readable_start_time = datetime.fromtimestamp(
                    event.when.start_time
                )
                formatted_start_datetime = human_readable_start_time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                human_readable_end_time = datetime.fromtimestamp(event.when.end_time)
                formatted_end_datetime = human_readable_end_time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                print(
                    f"Event id: {event.id}, Event title: {event.title}, start time: {formatted_start_datetime}, end time: {formatted_end_datetime}"
                )
        else:
            print("No events found in the specified calendar.")
        participants = [{"email": "oss1@wiseai.dev"}, {"email": "oss2@wiseai.dev"}]
        event = update_calendar_event(
            client,
            "Team Meeting Update",
            "Virtual",
            start_unix_time,
            end_unix_time,
            "Discuss project update",
            participants,
            "c7c5ccevt3agepcccv1an05sec",
            calendar_id,
        )
        print(f"\nEvent Update: {event}\n")
        events = read_calendar_events(
            client, calendar_id, start_unix_time, end_unix_time
        )
        print("\nGetting events after event update for Calendar 'test-update':\n")
        if events:
            for event in events:
                human_readable_start_time = datetime.fromtimestamp(
                    event.when.start_time
                )
                formatted_start_datetime = human_readable_start_time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                human_readable_end_time = datetime.fromtimestamp(event.when.end_time)
                formatted_end_datetime = human_readable_end_time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                print(
                    f"Event id: {event.id}, Event title: {event.title}, start time: {formatted_start_datetime}, end time: {formatted_end_datetime}"
                )
        else:
            print("No events found in the specified calendar.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
