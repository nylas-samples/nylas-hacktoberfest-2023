package com.nylas

import com.nylas.NylasClient
import com.nylas.models.DeleteResponse
import com.nylas.models.NylasApiError
import com.nylas.models.NylasSdkTimeoutError

fun main() {
    try{
        val nylas = NylasClient.Builder("API_ID").build()
    
        // Id of the existing user grant to be deleted.
        val grantId = "GRANT_ID"

        val response: DeleteResponse = nylas.auth().grants().destroy(grantId)
    
        if (response.requestId != null) {
            println("User grant with id $grantId is successfully deleted.")
        } else {
            println("Some issue encountered while deleting user grant with id $grantId")
        }
    } catch (e: NylasSdkTimeoutError) {
        e.printStackTrace()
    } catch (e: NylasApiError) {
        e.printStackTrace()
    }
}