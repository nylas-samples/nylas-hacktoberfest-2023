# Creating a Calendar Event using Nylas v3 Ruby SDK

# Importing dependencies
require 'dotenv/load'
require 'nylas'

# Initializing Nylas API Client
nylas = Nylas::Client.new(
    api_key: ENV["API_KEY"]
)

# # List the calendars
# all_calendars = nylas.client.calendar.list(identifier: "GRANT_ID")
# puts all_calendars

# Creating Calendar Event
begin
    new_calendar_event = nylas.events.create(
        identifier: ENV["GRANT_ID"],
        request_body: {
            when: {
                start_time: 00000, # add start time
                end_time: 00000,  # add end time
            },
            title: "My New Calendar Event 1",
            description: "Calendar test #1, using Nylas v3 Ruby SDK",
        },
        query_params:{
            calendar_id: "ADD_CALENDAR_ID", # add Calendar ID
        }
    )
    
    # print the created calendar event
    puts new_calendar_event

rescue => error
    puts "Nylas Error: #{error}"
end