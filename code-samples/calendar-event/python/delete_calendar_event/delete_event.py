import os
from nylas import Client
from dotenv import load_dotenv

load_dotenv()

# create nylas instance
nylas = Client(
    api_key = os.getenv("API_KEY")
)  

 
# get the list of calendars
response = nylas.calendars.list(identifier=os.getenv("GRANT_ID"))
calendars = response.data 


# print calendars 
calendar_index = 0
print("SNo. | Calendar Name | Calendar ID\n")
for calendar in calendars:
    print(f"{calendar_index}. {calendar.name} | {calendar.id}")
    calendar_index+=1


# select one calendar
print("select the calendar (index) to view its events!")
selected_calendar = int(input())
if(selected_calendar<0 or selected_calendar>=len(calendars)):
    raise Exception("Wrong index entered")


# print events of that calendar
events = nylas.events.list(identifier=os.getenv("GRANT_ID"), query_params={"calendar_id": calendars[selected_calendar].id}).data
print("SNo. | Event Title | Read Only | Event ID")
event_index = 0
for event in events:
    print(f"{event_index}. {event.title} | {str(event.read_only)} | {event.id}")
    event_index+=1


# select one event
print("Select the event (index) you want to delete")
selected_event = int(input())


# delete event, in case of failure, throw exception!
try:
    nylas.events.destroy(event_id=events[selected_event].id, identifier=os.getenv("GRANT_ID"), query_params={"calendar_id": calendars[selected_calendar].id})
    print("Event deleted successfully!")
except:
    raise Exception("Some error occured")
