from alphaiq_sdk.signals import Signals
from alphaiq_sdk.models import Models
from alphaiq_sdk.mapping import Mapping
from alphaiq_sdk.generative import Generative

class AlphaIQ(Signals, Models, Mapping, Generative):

    def __init__(self, token):
        self.token = token
        # self.host_url = "https://data.app.alphaiq.ai/api/v1/"
        self.host_url = "https://api.app.alphaiq.ai/api/v1/"
        self.headers = {'Authorization': f'Bearer {token}'}
        super().__init__(self.host_url, self.headers)

def client(token):
    return AlphaIQ(token)



