package com.nylas

import com.nylas.models.CreateCalendarRequest
import com.nylas.models.Calendar
import com.nylas.models.NylasApiError
import com.nylas.models.NylasSdkTimeoutError
import com.nylas.models.Response

fun main() {
    try {
        val nylas = NylasClient.Builder("API_KEY").build()

        val createCalendarRequest = CreateCalendarRequest.Builder("My Calendar") // Calendar name is required and other attributes are optional.
            .description("My calendar description") 
            .location("My calendar location") 
            .timezone("America/New_York")
            .build()

        val response: Response<Calendar> = nylas.calendars().create("GRANT_ID", createCalendarRequest)

        val calendar: Calendar = response.data

        println(
            "Created calendar with id ${calendar.id}, name ${calendar.name}, and description ${calendar.description}"
        )
    } catch (e: NylasSdkTimeoutError) {
        e.printStackTrace()
    } catch (e: NylasApiError) {
        e.printStackTrace()
    }
}
