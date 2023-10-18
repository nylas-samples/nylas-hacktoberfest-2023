import os
from nylas import Client
from dotenv import load_dotenv

load_dotenv()

nylas = Client(
    api_key = os.getenv("API_KEY")
)

#creating a calendar
calendar = {
    "name": "New Calendar Name"
}

# Getting the list of calendars
response = nylas.calendars.list(identifier=os.getenv("GRANT_ID"))
calendars = response.data 


# printing calendars 
calendar_index = 0
print("SNo. | Calendar Name | Calendar ID\n")
for calendar in calendars:
    print(f"{calendar_index}. {calendar.name} | {calendar.id}")
    calendar_index+=1

try:
    new_calendar = nylas.calendars.create(calendar)
    print("Calendar created successfully.")
    print("Calendar ID:", new_calendar["id"])
except Exception as e:
    print("Error:", str(e))
