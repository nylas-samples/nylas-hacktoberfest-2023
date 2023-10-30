import base64
import os
from datetime import datetime

import nylas
from dotenv import load_dotenv
from nylas.models.errors import NylasApiError
from nylas.models.grants import Grant, ListGrantsQueryParams
from nylas.models.response import ListResponse

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


def main() -> None:
    try:
        # Initialize the Nylas client with API_KEY environment variable
        client = nylas.Client(
            api_key=os.environ.get("API_KEY"),
        )
        # display all grants
        query_params = ListGrantsQueryParams(limit=10, orderBy="asc")
        grants_list = list_grants(client, query_params)
        print("List of Grants:")
        # grant attributes:
        # 'created_at', 'email', 'from_dict', 'from_json', 'grant_status',
        # 'id', 'ip', 'provider', 'provider_user_id', 'schema', 'scope',
        # 'settings', 'state', 'to_dict', 'to_json', 'updated_at', 'user_agent'
        for grant in grants_list:
            decoded_bytes = base64.b64decode(grant.state)
            decoded_string = decoded_bytes.decode("utf-8")
            print(f"Grant ID: {grant.id}, State: {decoded_string}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
