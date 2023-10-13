import os
from nylas import Client
from dotenv import load_dotenv
from datetime import datetime

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



# formats and returns the when parameter to fit in different kinds of cases
def formatter(when):
    if when.object=="date":
        return f"{when.date} all day"
    elif when.object=="timespan":
        return f"{datetime.fromtimestamp(when.start_time)} {when.start_timezone} to {datetime.fromtimestamp(when.end_time)} {when.end_timezone}"
    elif when.object=="datespan":
        return f"{when.start_date} to {when.end_date}"
    return ""

# print events of that calendar
try:
    events = nylas.events.list(identifier=os.getenv("GRANT_ID"), query_params={"calendar_id": calendars[selected_calendar].id}).data
    if(len(events)==0):
        print("No events to show")
    else:
        event_index = 1
        for event in events:
            print(f"{event_index}. {event.title}\nEvent ID: {event.id}\nWhen: {formatter(event.when)}\n")
            event_index+=1

except:
    raise Exception("Something went wrong!")