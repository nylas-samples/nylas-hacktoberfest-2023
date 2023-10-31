import base64
import os
from datetime import datetime

import nylas
from dotenv import load_dotenv
from nylas.models.errors import NylasApiError
from nylas.models.grants import (Grant, ListGrantsQueryParams)
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


def delete_grant(client: nylas.Client, grant_id: str) -> None:
    """
    Delete a grant from the Nylas account.

    Args:
        client (nylas.Client): An instance of the Nylas Client.
        grant_id (str): The ID of the user grant to delete.

    Returns:
        None
    """
    try:
        # Delete the grant
        delete_response = client.auth.grants.destroy(grant_id)

        print(f"\nGrant with ID {grant_id} deleted successfully.")

    except NylasApiError as e:
        print(f"An error occurred while deleting the user grant: {e}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main() -> None:
    try:
        # Initialize the Nylas client with API_KEY environment variable
        client = nylas.Client(
            api_key=os.environ.get("API_KEY"),
        )

        # List grants before deleting the grant
        print("User Grants Before Delete:")
        before_grants = list_grants(
            client, ListGrantsQueryParams(limit=10, orderBy="asc")
        )
        for grant in before_grants:
            decoded_bytes = base64.b64decode(grant.state)
            decoded_string = decoded_bytes.decode("utf-8")
            print(f"Grant ID: {grant.id}, Status: {decoded_string}")

        # Specify the grant ID you want to delete
        grant_id_to_delete = "your-grant-id-to-delete"

        delete_grant(client, grant_id_to_delete)

        # List grants after deleting the grant
        print("\nUser Grants After Delete:")
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
