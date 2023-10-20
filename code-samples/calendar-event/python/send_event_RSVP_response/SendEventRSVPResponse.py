# Import your dependencies
import os
from nylas import Client
from dotenv import load_dotenv

# Load your env variables
load_dotenv()

# Set Nylas API_KEY
nylas = Client(
    api_key=os.environ.get("API_KEY")
)

# Read settings from environment variables
grant_id = os.environ.get("GRANT_ID")
calendar_id = os.environ.get("CALENDAR_ID")
event_id = os.environ.get("EVENT_ID")

# Set status confirmation
status = 'maybe'   # yes | no | maybe

# If the calendar_id is another than the email please be sure to point to correct calendar_id
try:
    response = nylas.events.send_rsvp(grant_id, event_id, {"status": status}, {"calendar_id": calendar_id})
except Exception as e:
    print(f'An error occurred, exception {str(e)}')
else:
    print(f'RSVP Response succeed, request id: {response.request_id}')


# Check event RSVP status
try:
    response = nylas.events.find(grant_id, event_id, {"calendar_id": calendar_id})
except Exception as e:
    print(f'An error occurred, exception {str(e)}')
else:
    event = response.data
    print(f'Event: {event.title}, id: {event.id}')

    # Search for participant email
    for participant in event.participants:
        print(f'Participant: {participant.email},  status: {participant.status}')
