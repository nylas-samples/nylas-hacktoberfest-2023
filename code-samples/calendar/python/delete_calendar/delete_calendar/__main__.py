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

def get_all_event_ids():
    """
    Get a list of all event IDs associated with the user's calendar.

    Returns:
        list: A list of event IDs.

    Raises:
        NylasError: If there's an error while interacting with the Nylas API.
    """
    try:
        # Fetch all events for the authenticated user
        events = client.events.all()

        # Extract and return a list of event IDs
        event_ids = [event.id for event in events]
        return event_ids
    except NylasError as e:
        # Handle Nylas API errors
        print(f"Error: {e.message}")
        return []

def delete_calendar_event(event_id):
    """
    Delete a calendar event using the Nylas Python SDK.

    Args:
        event_id (str): The ID of the calendar event to be deleted.

    Returns:
        bool: True if the event was successfully deleted, False otherwise.

    Raises:
        NylasException: If there's an error while interacting with the Nylas API.
    """
    try:
        # Delete the calendar event by its ID
        client.events.delete(event_id)
        return True
    except NylasError as e:
        # Handle Nylas API errors
        print(f"Error: {e.message}")
        return False

def main():
    try:
        # display all event ids
        event_ids = get_all_event_ids()

        if event_ids:
            print("List of Event IDs:")
            for event_id in event_ids:
                print(event_id)
        else:
            print("Failed to fetch event IDs.")
        success = delete_calendar_event("8lyufsks2dlxzvh5ads9h3llu")

        if success:
            print("Calendar event deleted successfully.")
        else:
            print("Failed to delete the calendar event.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
