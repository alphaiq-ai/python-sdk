import requests

class Mapping:
    def __init__(self, host_url, headers):
        self.host_url = host_url
        self.headers = headers

    def get_company_identifiers_map(self, **kwargs):
        optional_args = {
            'consilienceId': kwargs.get('consilienceId', None),
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

        url = self.host_url + "/mapping/companyIdentifierMapping?"
        
        # Constructing URL based on provided optional arguments
        for key, value in optional_args.items():
            if value is not None:
                url += f"{key}={value}&"

        response = requests.get(url, headers=self.headers).json()
        return response
    
    def get_spindex_factors_map(self, **kwargs):
        optional_args = {
            'spindexId': kwargs.get('spindexId', None)
        }

        url = self.host_url + "/mapping/spindexFactors?"
        
        # Constructing URL based on provided optional arguments
        for key, value in optional_args.items():
            if value is not None:
                url += f"{key}={value}&"

        response = requests.get(url, headers=self.headers).json()
        return response
    
    def get_compass_questions_map(self, **kwargs):
        optional_args = {
            'questionId': kwargs.get('questionId', None)
        }

        url = self.host_url + "/mapping/compassQuestions?"
        
        # Constructing URL based on provided optional arguments
        for key, value in optional_args.items():
            if value is not None:
                url += f"{key}={value}&"

        response = requests.get(url, headers=self.headers).json()
        return response
    
    def get_bulk_mapping(self):

        url = self.host_url + f"/bulk/mapping"

        response = requests.get(url, headers=self.headers).json()
        return response