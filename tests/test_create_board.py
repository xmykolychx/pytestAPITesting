from utils.endpoints import Endpoints
from utils.helpers import Helpers


def test_create_board(api_client, trello_credentials, create_board):
    Helpers.check_success(Helpers.clean_board(Endpoints.BASE_URL + Endpoints.BOARDS + '/' + create_board))
