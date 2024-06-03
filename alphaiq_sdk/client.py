from alphaiq_sdk.signals import Signals
from alphaiq_sdk.models import Models
from alphaiq_sdk.mapping import Mapping
from alphaiq_sdk.generative import Generative

class AlphaIQ(Signals, Models, Mapping, Generative):

    def __init__(self, token):
        self.token = token
        # self.host_url = "https://data.app.alphaiq.ai/api/v1"
        self.host_url = "https://staging.app.alphaiq.ai/api/v1"
        # self.host_url = "http://44.222.52.51:9000/api/v1"
        self.headers = {'Authorization': f'Bearer {token}','Origin':'https://staging.app.alphaiq.ai'}
        super().__init__(self.host_url, self.headers)

def client(token):
    return AlphaIQ(token)



