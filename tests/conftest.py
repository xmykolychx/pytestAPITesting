import pytest
import requests

from utils.constants import Constants
from utils.endpoints import Endpoints
from test_data.test_data import TestData


@pytest.fixture
def api_client():
    return requests.Session()  # Use a session to persist connection


@pytest.fixture
def trello_credentials():
    """The better approach to access such values will be with the help of os, 
    but there is currently a problem with python versions of my computer."""

    api_key = Constants.API_KEY
    api_token = Constants.API_TOKEN
    if not api_key or not api_token:
        raise ValueError("Trello API key and token are not set in environment variables.")
    return api_key, api_token


@pytest.fixture
def create_board(request, api_client, trello_credentials):
    api_key, api_token = trello_credentials

    def _create_board(name=TestData.board_name):
        url = f"{Endpoints.BASE_URL}/{Endpoints.BOARDS}"
        response = api_client.post(url, params={'key': api_key, 'token': api_token, 'name': name})
        assert response.status_code == 200
        board_id = response.json()['id']
        return board_id

    board_id = _create_board()
    return board_id


@pytest.fixture
def create_list(api_client, trello_credentials):
    api_key, api_token = trello_credentials

    def _create_list(board_id, name="Test List"):
        url = f"{Endpoints.BASE_URL}/{Endpoints.LISTS}"
        response = api_client.post(url, params={'key': api_key, 'token': api_token, 'name': name, 'idBoard': board_id})
        list_id = response.json()['id']
        return list_id

    return _create_list


@pytest.fixture
def create_card(api_client, trello_credentials):
    api_key, api_token = trello_credentials

    def _create_card(list_id, name="Test Card"):
        url = f"{Endpoints.BASE_URL}/{Endpoints.CARDS}"
        response = api_client.post(url, params={'key': api_key, 'token': api_token, 'name': name, 'idList': list_id})
        card_id = response.json()['id']
        return card_id

    return _create_card


@pytest.fixture
def create_label(api_client, trello_credentials):
    api_key, api_token = trello_credentials

    def _create_label(card_id, name, color):
        url = f"{Endpoints.BASE_URL}/{Endpoints.CARDS}/{card_id}/{Endpoints.LABELS}"
        params = {
            'key': api_key,
            'token': api_token,
            'name': name,
            'color': color
        }
        response = api_client.post(url, params=params)
        response.raise_for_status()
        label_id = response.json()['id']
        return label_id

    return _create_label

@pytest.fixture
def create_sticker(api_client, trello_credentials):
    api_key, api_token = trello_credentials

    def _create_sticker(card_id, sticker_image, top, left, zIndex):
        url = f"{Endpoints.BASE_URL}/{Endpoints.CARDS}/{card_id}{Endpoints.STICKERS}"
        params = {
            'key': api_key,
            'token': api_token,
            'image': sticker_image,
            'top': top,
            'left': left,
            'zIndex': zIndex
        }
        try:
            response = api_client.post(url, params=params)
            response.raise_for_status()  # Raise exception for non-200 response codes
            sticker_id = response.json()['idSticker']
            return sticker_id
        except requests.exceptions.HTTPError as e:
            print("Error creating sticker:", e.response.content.decode())
            raise

    return _create_sticker
