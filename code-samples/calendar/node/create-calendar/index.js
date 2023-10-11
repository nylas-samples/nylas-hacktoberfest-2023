import Nylas from 'nylas'; 
import 'dotenv/config'; 

const nylas = new Nylas({
    apiKey: `${process.env.NYLAS_API_KEY}`,
}); 

try{ 
    nylas.calendars.create({
        identifier:`${process.env.NYLAS_GRANT_ID}`,
        requestBody: {
            name: 'new calendar', 
            description: 'new calendar made with ♡ in Nylas',
            location: 'remote',
            timezone: 'America/New_York'
        }
    })  
} catch(err){ 
    console.log(err); 
}

console.log("Your new calendar was successfully created ♡ Nylas")