package com.nylas

import com.nylas.NylasClient;
import com.nylas.models.DeleteResponse
import com.nylas.models.NylasApiError
import com.nylas.models.NylasSdkTimeoutError

fun main() {
    try {
        val nylas = NylasClient.Builder("API_ID").build()

        // Id of the existing calendar to be deleted.
        val calendarId = "CALENDAR_ID"

        val response: DeleteResponse = nylas.calendars().destroy("GRANT_ID", calendarId)

        if (response.requestId != null) {
            println("Calendar with id $calendarId is successfully deleted.")
        } else {
            println("Some issue encountered while deleting calendar with id $calendarId")
        }
    } catch (e: NylasSdkTimeoutError) {
        e.printStackTrace()
    } catch (e: NylasApiError) {
        e.printStackTrace()
    }
}
