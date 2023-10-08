from nylas import APIClient

client = APIClient(
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
    access_token="ACCESS_TOKEN"
)

calendar = {
    "name": "New Calendar Name"
}

try:
    new_calendar = client.calendars.create(calendar)
    print("Calendar created successfully.")
    print("Calendar ID:", new_calendar["id"])
except Exception as e:
    print("Error:", str(e))
