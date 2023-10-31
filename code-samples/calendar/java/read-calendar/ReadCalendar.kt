package com.nylas

import com.nylas.models.Calendar;
import com.nylas.models.ListResponse;
import com.nylas.models.NylasApiError;
import com.nylas.models.NylasSdkTimeoutError;

fun main() {
    try {
        val nylas = NylasClient.Builder("API_KEY").build()

        val calendars: ListResponse<Calendar> = nylas.calendars().list("GRANT_ID")

        for (calendar in calendars.data) {
            println(
                "Reading calendar with id ${calendar.id}, name ${calendar.name}, and description ${calendar.description}"
            )
        }
    } catch (e: NylasSdkTimeoutError) {
        e.printStackTrace()
    } catch (e: NylasApiError) {
        e.printStackTrace()
    }
}