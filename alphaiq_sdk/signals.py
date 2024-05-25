import requests

class Signals:
    def __init__(self, host_url, headers):
        self.host_url = host_url
        self.headers = headers

    def get_quant_linguistics_signals(self, signalVariation: str, startDate: str, endDate: str, **kwargs):
        optional_args = {
            'consilienceId': kwargs.get('consilience_id', None),
            'ticker': kwargs.get('ticker', None),
            'cik': kwargs.get('cik', None),
            'lei': kwargs.get('lei', None),
            'isin': kwargs.get('isin', None),
            'cusip': kwargs.get('cusip', None)
        }

        # Checking if at least one optional argument is present
        if not any(optional_args.values()):
            raise ValueError("One and only one company identifier argument must be provided.")

        url = self.host_url + "/signals/quantLinguistics?"
        
        # Constructing URL based on provided optional arguments
        for key, value in optional_args.items():
            if value is not None:
                url += f"{key}={value}&"

        # Adding mandatory arguments to the URL
        url += f"signalVariation={signalVariation}&startDate={startDate}&endDate={endDate}"

        response = requests.get(url, headers=self.headers).json()
        return response
    
    def get_bulk_signals_all(self):

        url = self.host_url + f"/bulk/signals/all"

        response = requests.get(url, headers=self.headers).json()
        return response
    
    def get_bulk_signals_top_level(self):

        url = self.host_url + f"/bulk/signals/topLevel"

        response = requests.get(url, headers=self.headers).json()
        return response