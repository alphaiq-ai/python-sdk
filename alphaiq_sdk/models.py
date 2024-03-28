import requests

class Models:
    def __init__(self, host_url, headers):
        self.host_url = host_url
        self.headers = headers

    def get_models_spindex(self, rawSmoothFlag: str, startDate: str, endDate: str, **kwargs):
        optional_args = {
            'consilience_id': kwargs.get('consilience_id', None),
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

        url = self.host_url + "/models/spindex?"
        
        # Constructing URL based on provided optional arguments
        for key, value in optional_args.items():
            if value is not None:
                url += f"{key}={value}&"

        # Adding mandatory arguments to the URL
        url += f"rawSmoothFlag={rawSmoothFlag}&startDate={startDate}&endDate={endDate}"

        response = requests.get(url, headers=self.headers).json()
        return response
    
    def get_bulk_model(self, rawSmoothFlag: str, model_name: str):

        url = self.host_url + f"/bulk/models?rawSmoothFlag={rawSmoothFlag}&modelName={model_name}"

        response = requests.get(url, headers=self.headers).json()
        return response