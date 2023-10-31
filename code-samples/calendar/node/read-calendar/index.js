import 'dotenv/config'; 
import Nylas from "nylas";

const nylas = new Nylas({
    apiKey: `${process.env.NYLAS_API_KEY}`,
}); 

try{ 
    nylas.calendars.find({
        identifier:`${process.env.NYLAS_GRANT_ID}`,
        calendarId: `${process.env.NYLAS_CALENDAR_ID}`

    }).then(calendar => { 
        console.log(calendar); 
    }); 

} catch(err){ 
    console.log(err); 
}

