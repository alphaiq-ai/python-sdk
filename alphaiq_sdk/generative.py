import requests

class Generative:
    def __init__(self, host_url, headers):
        self.host_url = host_url
        self.headers = headers

    def get_spinsights_explorer_spindex_summary(self, ticker: str):

        url = self.host_url + f"/generative/company/spinsights/explorerContent/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response
     
    def get_spinsights_report_content(self, ticker: str):

        url = self.host_url + f"/generative/company/spinsights/reportContent/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response 

    def get_spinsights_report_pdf(self, ticker: str):

        url = self.host_url + f"/pdf/spinsights/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response 

    def get_compass_explorer_question_answer(self, ticker: str):

        url = self.host_url + f"/generative/company/compass/questionContent/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response 

    def get_compass_report_content(self, ticker: str):

        url = self.host_url + f"/generative/company/compass/reportContent/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response 
    
    def get_compass_report_pdf(self, ticker: str):

        url = self.host_url + f"/pdf/compass/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response 
    
