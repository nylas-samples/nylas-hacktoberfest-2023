import os
from datetime import datetime

import nylas
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

from nylas.models.availability import GetAvailabilityRequest
from nylas.models.errors import NylasApiError

# Load environment variables from a .env file
load_dotenv()


def get_calendar_availability(client: nylas.Client, start_time: int, end_time: int):
    """
    Get calendar availability within a specified time range.
    Args:
        client (nylas.Client): An instance of the Nylas Client.
        start_time (int): The start time of the range in Unix timestamp format.
        end_time (int): The end time of the range in Unix timestamp format.
    Raises:
        nylas.models.errors.NylasApiError: If there is an error while fetching calendar events.
    """
    try:
        # TODO: add participants
        query_params = GetAvailabilityRequest(
            start_time=start_time,
            end_time=end_time,
        )
        availability, _, _ = client.calendars.get_availability(
            identifier=os.environ.get("GRANT_ID"), request_body=query_params
        )
        return availability
    except NylasApiError as e:
        print(f"Error while fetching calendar availability: {e}")


def main() -> None:
    try:
        # Initialize the Nylas client with API_KEY environment variable
        client = nylas.Client(
            api_key=os.environ.get("API_KEY"),
        )
        # Replace with your actual start and end times
        start_time = "2023-10-01T00:00:00Z"
        start_datetime_obj = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
        start_unix_time = int(start_datetime_obj.timestamp())

        end_time = "2024-10-20T23:59:59Z"
        end_datetime_obj = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ")
        end_unix_time = int(end_datetime_obj.timestamp())
        availability = get_calendar_availability(client, start_unix_time, end_unix_time)
        print(availability)
    except NylasApiError as e:
        print(f"Nylas Error: {e}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
