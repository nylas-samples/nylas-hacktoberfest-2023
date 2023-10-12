const dotenv = require("dotenv");
const Nylas = require("nylas");

dotenv.config();

// configuring the Nylas client
const NylasConfig = {
    apiKey: `${process.env.API_KEY}`
}

// initialising the Nylas client with access token
const nylas = new Nylas(NylasConfig);

// enter the Event ID which you want to update
const eventId = '<Event ID to be updated>';

nylas.events.find(eventId, {identifier: `${process.env.GRANT_ID}`})
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