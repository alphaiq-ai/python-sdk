import requests

BASE_PATH = "/identifiers"


class Identifiers:
    def __init__(self, host_url, headers):
        self.host_url = host_url
        self.headers = headers

    def get_identifiers(self) -> dict:
        url = self.host_url + BASE_PATH
        response = requests.get(url, headers=self.headers).json()
        return response

    def search_identifier(self, query: str):
        url = self.host_url + BASE_PATH + f"/search?q={query}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_all_companies_name(self):
        url = self.host_url + BASE_PATH + f"/companies"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_all_lvl4_industries_name(self):
        url = self.host_url + BASE_PATH + f"/industries"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_high_risk_industries(self, view_change: str):
        url = self.host_url + BASE_PATH + f"/industries/highrisk/{view_change}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_low_risk_industries(self, view_change: str):
        url = self.host_url + BASE_PATH + f"/industries/lowrisk/{view_change}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_high_risk_companies_across_all_industries(self, view_change: str):
        url = self.host_url + BASE_PATH + f"/companies/highrisk/{view_change}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_high_risk_companies_of_particular_lvl2_industry(self, view_change: str, lvl2_industry_name: str):
        url = self.host_url + BASE_PATH + f"/companies/highrisk/{view_change}?lvl2IndustryName={lvl2_industry_name}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_high_risk_companies_of_particular_lvl3_industry(self, view_change: str, lvl3_industry_name: str):
        url = self.host_url + BASE_PATH + f"/companies/highrisk/{view_change}?lvl3IndustryName={lvl3_industry_name}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_high_risk_companies_of_particular_lvl4_industry(self, view_change: str, lvl4_industry_name: str):
        url = self.host_url + BASE_PATH + f"/companies/highrisk/{view_change}?lvl4IndustryName={lvl4_industry_name}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_low_risk_companies_across_all_industries(self, view_change: str):
        url = self.host_url + BASE_PATH + f"/companies/lowrisk/{view_change}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_low_risk_companies_of_particular_lvl2_industry(self, view_change: str, lvl2_industry_name: str):
        url = self.host_url + BASE_PATH + f"/companies/lowrisk/{view_change}?lvl2IndustryName={lvl2_industry_name}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_low_risk_companies_of_particular_lvl3_industry(self, view_change: str, lvl3_industry_name: str):
        url = self.host_url + BASE_PATH + f"/companies/lowrisk/{view_change}?lvl3IndustryName={lvl3_industry_name}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_low_risk_companies_of_particular_lvl4_industry(self, view_change: str, lvl4_industry_name: str):
        url = self.host_url + BASE_PATH + f"/companies/lowrisk/{view_change}?lvl4IndustryName={lvl4_industry_name}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_identifier_details(self, identifier: str):
        url = self.host_url + BASE_PATH + f"/details/{identifier}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_identifier_latest_spindex_score(self, identifier: str):
        url = self.host_url + BASE_PATH + f"/scores/{identifier}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_company_latest_six_weeks_spindex_scores(self, company_name: str):
        url = self.host_url + BASE_PATH + f"/company/{company_name}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def add_identifier_to_favorites(self, identifier: str):
        url = self.host_url + BASE_PATH + f"/favorites/add/{identifier}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def remove_identifier_from_favorites(self, identifier: str):
        url = self.host_url + BASE_PATH + f"/favorites/remove/{identifier}"
        response = requests.delete(url, headers=self.headers).json()
        return response

    def get_user_dashboard_data(self):
        url = self.host_url + BASE_PATH + f"/users/list"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_identifier_compared_scores(self, identifier: str):
        url = self.host_url + BASE_PATH + f"/comparedscore/{identifier}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_constituents_companies_with_latest_overallrisk(self, lvl4_industry_name: str):
        url = self.host_url + BASE_PATH + f"/industry/{lvl4_industry_name}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_identifier_timeseries_overallrisk(self, identifier: str):
        url = self.host_url + BASE_PATH + f"/timeseries/overallrisk/{identifier}"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_industries_overview(self):
        url = self.host_url + BASE_PATH + f"/industries/overview"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_companies_overview(self):
        url = self.host_url + BASE_PATH + f"/companies/overview"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_all_level_industries_names(self):
        url = self.host_url + BASE_PATH + f"/industries/names"
        response = requests.get(url, headers=self.headers).json()
        return response