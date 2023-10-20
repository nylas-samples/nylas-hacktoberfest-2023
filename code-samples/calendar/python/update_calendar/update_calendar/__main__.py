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

def update_calendar(calendar_id, new_attributes):
    """
    Update a calendar using the Nylas Python SDK.

    Args:
        calendar_id (str): The ID of the calendar to be updated.
        new_attributes (dict): A dictionary containing the new attributes to update.

    Returns:
        bool: True if the calendar was successfully updated, False otherwise.

    Raises:
        NylasException: If there's an error while interacting with the Nylas API.
    """
    try:
        # Fetch the calendar by its ID
        calendar = client.calendars.get(calendar_id)

        if calendar:
            # Update the calendar attributes
            for key, value in new_attributes.items():
                setattr(calendar, key, value)
            
            # Save the updated calendar
            calendar.save()
            return True
        else:
            print("Calendar not found.")
            return False
    except NylasError as e:
        # Handle Nylas API errors
        print(f"Error: {e.message}")
        return False

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


def main():
    try:
        # display all calendar ids
        display_calendar_ids()

        # Replace with your actual calendar ID
        calendar_id = 'dvr7bn8t2vitjwicq4a0wlmyz'
    
        # Define the new attributes to update
        new_attributes = {
            "name": "Updated Calendar Name",
            "description": "Updated Calendar Description"
        }

        success = update_calendar(calendar_id, new_attributes)

        if success:
            print("Calendar updated successfully.")
        else:
            print("Failed to update the calendar.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
