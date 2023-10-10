const dotenv = require("dotenv");
const Nylas = require("nylas");

dotenv.config();

// configuring the Nylas client
Nylas.config({
    clientId: process.env.CLIENT_ID,
    clientSecret: process.env.CLIENT_SECRET
});

// initialising the Nylas client with access token
const nylas = Nylas.with(process.env.ACCESS_TOKEN);

// enter the Event ID which you want to update
const eventId = '<Event ID to be updated>';

nylas.events.find(eventId)
    .then((event) => {
        event.title = '<Updated Event Title>';    //replace these placeholders with your own values
        event.location = '<Updated Location>';
        event.description = '<Updated Description>';
        // add more fields as per your requirement

        return event.save();
    })
    .then((updatedEvent) => {
        console.log(`Event updated successfully`);
        console.log(`Updated Title: ${updatedEvent.title}`);
        console.log(`Updated Location: ${updatedEvent.location}`);
        console.log(`Updated Description: ${updatedEvent.description}`);
        // add more console.log() functions if you have updated more fields
    })
    .catch((err) => console.error("Error: ", err));