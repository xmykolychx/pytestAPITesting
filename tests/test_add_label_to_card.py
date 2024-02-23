from utils.endpoints import Endpoints
from test_data.test_data import TestData
from utils.helpers import Helpers

import requests
from random import choice


def test_add_label_to_card(api_client, trello_credentials, create_board, create_list, create_card, create_label):
    api_key, api_token = trello_credentials

    list_id = create_list(create_board, TestData.list_name)

    card_id = create_card(list_id, TestData.board_name)

    try:
        label_id = create_label(card_id, TestData.label_name, choice(TestData.label_colors))
    except requests.exceptions.HTTPError as e:
        print("Error adding label to card:", e.response.content.decode())
        raise

    Helpers.check_label(label_id)

    Helpers.check_success(api_client.get(
        f"{Endpoints.BASE_URL}/{Endpoints.LABELS}/{label_id}",
        params={'key': api_key, 'token': api_token})
    )

    Helpers.check_success(Helpers.clean_board(Endpoints.BASE_URL + Endpoints.BOARDS + '/' + create_board))
