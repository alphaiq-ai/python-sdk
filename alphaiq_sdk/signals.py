import requests

class Signals:
    def __init__(self, host_url, headers):
        self.host_url = host_url
        self.headers = headers

    def get_quant_linguistics_signals(self, startDate: str, endDate: str, **kwargs):
        optional_args = {
            'consilienceId': kwargs.get('consilience_id', None),
            'ticker': kwargs.get('ticker', None),
            'cik': kwargs.get('cik', None),
            'lei': kwargs.get('lei', None),
            'isin': kwargs.get('isin', None),
            'cusip': kwargs.get('cusip', None),
            'sedol': kwargs.get('sedol', None)
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
        url += f"startDate={startDate}&endDate={endDate}"

        response = requests.get(url, headers=self.headers).json()
        return response
    
    def get_bulk_signals(self, strategyType: str):

        url = self.host_url + f"/bulk/signals?strategyType={strategyType}"

        response = requests.get(url, headers=self.headers).json()
        return response
    
    def get_bulk_signals_yearly(self, strategyType: str, alphaHorizon: str, year: int):

        url = self.host_url + f"/bulk/signals/yearly?strategyType={strategyType}&alphaHorizon={alphaHorizon}&year={year}"

        response = requests.get(url, headers=self.headers).json()
        return response