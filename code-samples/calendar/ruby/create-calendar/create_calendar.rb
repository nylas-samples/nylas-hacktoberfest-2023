# Creating a Calendar using Nylas v3 Ruby SDK

# Importing dependencies
require 'dotenv/load'
require 'nylas'

# Initializing Nylas API Client
nylas = Nylas::Client.new(
    api_key: ENV["API_KEY"]
)

begin
    help Nylas::Client.calendar.create
rescue => error
    puts error
end