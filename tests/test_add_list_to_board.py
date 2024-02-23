from utils.endpoints import Endpoints
from test_data.test_data import TestData
from utils.helpers import Helpers


def test_add_list_to_board(api_client, trello_credentials, create_board, create_list):
    api_key, api_token = trello_credentials

    list_id = create_list(create_board, TestData.list_name)

    Helpers.check_list(list_id)

    Helpers.check_success(api_client.get(
        f"{Endpoints.BASE_URL}/{Endpoints.LISTS}/{list_id}",
        params={'key': api_key, 'token': api_token})
    )

    Helpers.check_success(Helpers.clean_board(Endpoints.BASE_URL + Endpoints.BOARDS + '/' + create_board))
