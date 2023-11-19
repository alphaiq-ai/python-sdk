import requests

from alphaiq_sdk.config import config
from alphaiq_sdk.identifiers import Identifiers
from alphaiq_sdk.users import Users

HOST_URL = config.HOST_URL


class AlphaIQ(Identifiers, Users):

    def __init__(self, token):
        self.token = token
        self.host_url = HOST_URL
        self.headers = {'Authorization': f'Bearer {token}'}
        super().__init__(self.host_url, self.headers)


def client(token):
    return AlphaIQ(token)


def get_token(email: str, base64_password: str):
    url = HOST_URL + "/auth/gettoken"
    payload = {"email": email, "password": base64_password}
    response = requests.post(url, json=payload).json()
    return response
