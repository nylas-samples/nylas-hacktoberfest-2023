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

#printing calendars
no_calendar= 0
print("SNo. | Calendar Name | Calendar ID\n")
for i in calendar:
    print(f"{no_calendar}. {i.name} | {i.id}")
    no_calendar+=1

try:
    new_calendar = nylas.calendars.create(calendar)
    print("Calendar created successfully.")
    print("Calendar ID:", new_calendar["id"])
except Exception as e:
    print("Error:", str(e))
