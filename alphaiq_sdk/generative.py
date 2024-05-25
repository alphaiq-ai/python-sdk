import requests

class Generative:
    def __init__(self, host_url, headers):
        self.host_url = host_url
        self.headers = headers

    def get_signal_explanations(self, ticker: str):

        url = self.host_url + f"/generative/company/signal_explanation/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response

    def get_question_answer(self, ticker: str):

        url = self.host_url + f"/generative/company/compass/questionContent/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response 

    def get_trending_content(self, ticker: str):

        url = self.host_url + f"/generative/company/compass/reportContent/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response 
    
    def get_compass_report_pdf(self, ticker: str):

        url = self.host_url + f"/pdf/compass/{ticker}"

        response = requests.get(url, headers=self.headers).json()
        return response 
    
