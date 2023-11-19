import requests

BASE_PATH = "/users"


class Users:
    def __init__(self, host_url, headers):
        self.host_url = host_url
        self.headers = headers

    def update_username(self, first_name: str, last_name: str):
        url = self.host_url + BASE_PATH + "/update/username"
        payload = {"firstName": first_name, "lastName": last_name}
        response = requests.put(url, headers=self.headers, json=payload).json()
        return response

    def update_password(self, current_password: str, new_password: str):
        """
        :param current_password: must be base64 encoded
        :param new_password: must be base64 encoded
        :return:
        """
        url = self.host_url + BASE_PATH + "/update/password"
        payload = {"currentPassword": current_password, "newPassword": new_password}
        response = requests.put(url, headers=self.headers, json=payload).json()
        return response

    def delete_account(self):
        url = self.host_url + BASE_PATH + '/delete/account'
        response = requests.delete(url, headers=self.headers)
        return response.text

    def get_favorites_companies_of_user(self):
        url = self.host_url + BASE_PATH + f"/favorites/companies"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_favorites_industries_of_user(self):
        url = self.host_url + BASE_PATH + f"/favorites/industries"
        response = requests.get(url, headers=self.headers).json()
        return response
