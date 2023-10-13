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
print("SNo. Calendar Name | Calendar ID")
for calendar in calendars:
    print(f"{calendar_index}. {calendar.name} | {calendar.id}")
    calendar_index+=1


# select one calendar
print("select the calendar (index) to view its events!")
selected_calendar = int(input())
if(selected_calendar<0 or selected_calendar>=len(calendars)):
    raise Exception("Wrong index entered")


# print events of that calendar
try:
    events = nylas.events.list(identifier=os.getenv("GRANT_ID"), query_params={"calendar_id": calendars[selected_calendar].id}).data
    if(len(events)==0):
        print("No events to show")
    else:
        print("SNo. Event Title | When | Event ID")
        event_index = 0
        for event in events:
            print(f"{event_index}. {event.title} | {event.when.date} | {event.id}")
            event_index+=1

except:
    raise Exception("Something went wrong!")