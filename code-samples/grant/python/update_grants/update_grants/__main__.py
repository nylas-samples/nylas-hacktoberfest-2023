import base64
import os
from datetime import datetime

import nylas
from dotenv import load_dotenv
from nylas.models.errors import NylasApiError
from nylas.models.grants import Grant, ListGrantsQueryParams, UpdateGrantRequest
from nylas.models.response import ListResponse, Response

# Load environment variables from a .env file
load_dotenv()


def list_grants(
    client: nylas.Client, query_params: ListGrantsQueryParams
) -> ListResponse[Grant]:
    """
    List Grants using the provided Nylas client and query parameters.

    Args:
        client (nylas.Client): An instance of the Nylas Client.
        query_params (nylas.models.grants.ListGrantsQueryParams): The query
        parameters to include in the request.

    Returns:
        ListResponse[Grant]: A list of Grant objects.

    Raises:
        nylas.NylasApiError: If there is an error during the request.
    """
    try:
        # Call the list method with the provided Nylas client and query parameters
        grants, _, _ = client.auth.grants.list(query_params)

        return grants

    except NylasApiError as e:
        raise e


def update_grant(
    client: nylas.Client, grant_id: str, request_body: UpdateGrantRequest
) -> None:
    """
    Update a user grant in the Nylas account.

    Args:
        client (nylas.Client): An instance of the Nylas Client.
        grant_id (str): The ID of the user grant to update.
        request_body (UpdateGrantRequest): The values to update the user grant with.

    Returns:
        None
    """
    try:
        # Update the user grant
        updated_grant = client.auth.grants.update(grant_id, request_body)
        print(f"User Grant updated successfully:")
        print(f"User Grant ID: {updated_grant.id}")
        print(f"Updated Scope: {updated_grant.scope}")
        # Add additional fields as needed

    except NylasApiError as e:
        print(f"An error occurred while updating the user grant: {e.msg}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main() -> None:
    try:
        # Initialize the Nylas client with API_KEY environment variable
        client = nylas.Client(
            api_key=os.environ.get("API_KEY"),
        )

        # List grants before creating a new grant
        print("User Grants Before Update:")
        before_grants = list_grants(
            client, ListGrantsQueryParams(limit=10, orderBy="asc")
        )
        for grant in before_grants:
            decoded_bytes = base64.b64decode(grant.state)
            decoded_string = decoded_bytes.decode("utf-8")
            print(f"Grant ID: {grant.id}, Status: {decoded_string}")

        # Specify the grant ID you want to update
        grant_id_to_update = "ADD_GRANT_ID_TO_UPDATE"

        # Define the request body to update the user grant
        update_request_body = UpdateGrantRequest(
            scope=["email.read", "calendar.write"],
            settings={
                "refresh_token": "your_refresh_token",  # change it to your refresh token
                # Add additional fields for updates as needed
            },
        )

        update_grant(client, grant_id_to_update, update_request_body)

        # List grants after creating the grant
        print("\nUser Grants After Update:")
        after_grants = list_grants(
            client, ListGrantsQueryParams(limit=10, orderBy="asc")
        )
        for grant in after_grants:
            decoded_bytes = base64.b64decode(grant.state)
            decoded_string = decoded_bytes.decode("utf-8")
            print(f"Grant ID: {grant.id}, Status: {decoded_string}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
