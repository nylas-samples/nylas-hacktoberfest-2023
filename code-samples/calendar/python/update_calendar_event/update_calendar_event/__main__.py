import datetime
import os

import nylas
from dotenv import load_dotenv
from nylas.client.errors import NylasError

# Load environment variables from a .env file
load_dotenv()


def update_calendar_event(
    client,
    event_id,
    title=None,
    location=None,
    start_time=None,
    end_time=None,
    description=None,
    participants=None,
):
    """
    Update an existing calendar event.

    Args:
        client (nylas.APIClient): The initialized Nylas API client.
        event_id (str): The ID of the event to update.
        title (str, optional): The updated title of the event.
        location (str, optional): The updated location of the event.
        start_time (str, optional): The updated start time of the event in ISO 8601 format.
        end_time (str, optional): The updated end time of the event in ISO 8601 format.
        description (str, optional): The updated description of the event.
        participants (list, optional): The updated list of participant dictionaries with an "email" field.

    Returns:
        nylas.events.Event: The updated event object.

    Raises:
        nylas.client.errors.NylasError: If there's an issue with the Nylas API.
    """
    try:
        event = client.events.get(event_id)

        if title is not None:
            event.title = title
        if location is not None:
            event.location = location
        if start_time is not None and end_time is not None:
            event.when = {"start_time": start_time, "end_time": end_time}
        if description is not None:
            event.description = description
        if participants is not None:
            event.participants = participants

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

        # Retrieve all events associated with this calendar to choose an id to update the event.
        events = get_all_events(client, "dvr7bn8t2vitjwicq4a0wlmyz")
        if events:
            print(f"\nFirst event before update: {events[0]}\n")

        else:
            print("No events found in the specified calendar.")
        participants = [{"email": "oss3@wiseai.dev"}, {"email": "oss4@wiseai.dev"}]
        updated_event = update_calendar_event(
            client,
            "a78lwinreqpjwctfzost31y33",
            title="Updated Meeting",
            location="New Conference Room",
            start_time="2023-10-21T10:00:00Z",
            end_time="2023-10-21T11:00:00Z",
            description="Discuss project status",
            participants=participants,
        )

        events = get_all_events(client, "dvr7bn8t2vitjwicq4a0wlmyz")
        if events:
            print(f"\nFirst event after update: {events[0]}\n")
    except NylasError as e:
        raise NylasError(f"Error creating event: {e.message}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
