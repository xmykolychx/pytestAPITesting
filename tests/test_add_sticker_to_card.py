from utils.endpoints import Endpoints
from test_data.test_data import TestData
from utils.helpers import Helpers


def test_add_sticker_to_card(api_client, trello_credentials, create_board, create_list, create_card, create_sticker):
    api_key, api_token = trello_credentials

    list_id = create_list(create_board, TestData.list_name)

    Helpers.check_list(list_id)

    card_id = create_card(list_id, TestData.board_name)

    Helpers.check_success(api_client.get(
        f"{Endpoints.BASE_URL}/{Endpoints.CARDS}/{card_id}",
        params={'key': api_key, 'token': api_token})
    )

    Helpers.check_success(Helpers.clean_board(Endpoints.BASE_URL + Endpoints.BOARDS + '/' + create_board))
