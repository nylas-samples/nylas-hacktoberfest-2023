import base64
import os
from datetime import datetime

import nylas
from dotenv import load_dotenv
from nylas.models.errors import NylasApiError
from nylas.models.response import ListResponse
from nylas.models.grants import CreateGrantRequest
from nylas.models.grants import ListGrantsQueryParams
from nylas.models.response import Response
from nylas.models.grants import Grant

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

def create_grant(client: nylas.Client, request_body: CreateGrantRequest) -> Response[Grant]:
    """
    Create a Grant using the provided Nylas client and request body.

    Args:
        client (nylas.Client): An instance of the Nylas Client.
        request_body (CreateGrantRequest): The values to create the Grant with.

    Returns:
        Response[Grant]: A response containing the created Grant.

    Raises:
        nylas.NylasApiError: If there is an error during the request.
    """
    try:
        grant, _ = client.auth.grants.create(request_body)
        return grant

    except NylasApiError as e:
        raise e

def main() -> None:
    try:
        # Initialize the Nylas client with API_KEY environment variable
        client = nylas.Client(
            api_key=os.environ.get("API_KEY"),
        )

        # List grants before creating a new grant
        print("Grants Before Creation:")
        before_grants = list_grants(client, ListGrantsQueryParams(limit=10, orderBy='asc'))
        for grant in before_grants:
            decoded_bytes = base64.b64decode(grant.state)
            decoded_string = decoded_bytes.decode("utf-8")
            print(f"Grant ID: {grant.id}, Status: {decoded_string}")

        # Create a new grant
        grant_request_body = CreateGrantRequest(
            provider="google",
            settings={
                "refresh_token": "your_refresh_token", # change it to your refresh token
            },
            state="optional_state",
            scope=["calendar.read", "calendar.write"],
        )

        new_grant = create_grant(client, grant_request_body)
        print("New Grant Created:")
        decoded_bytes = base64.b64decode(new_grant.state)
        decoded_string = decoded_bytes.decode("utf-8")
        print(f"Grant ID: {new_grant.id}, State: {decoded_string}")

        # List grants after creating the grant
        print("Grants After Creation:")
        after_grants = list_grants(client, ListGrantsQueryParams(limit=10, orderBy='asc'))
        for grant in after_grants:
            decoded_bytes = base64.b64decode(grant.state)
            decoded_string = decoded_bytes.decode("utf-8")
            print(f"Grant ID: {grant.id}, Status: {decoded_string}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
