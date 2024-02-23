import requests
from utils.constants import Constants


class Helpers:
    @staticmethod
    def check_success(obj):
        assert obj.status_code == 200

    @staticmethod
    def clean_board(url):
        request = requests.request(
            "DELETE",
            url,
            params={
                'key': Constants.API_KEY,
                'token': Constants.API_TOKEN
            }
        )
        return request

    @staticmethod
    def check_label(label_id):
        assert label_id is not None

    @staticmethod
    def check_list(list_id):
        assert list_id is not None