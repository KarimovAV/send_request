import requests


class HttpsMethods:
    """Custom HTTP Methods For Requests """

    headers = {"Content-Type": "application/json"}
    cookie = ""

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint=''):
        uri = self.base_url + endpoint
        return requests.get(uri, headers=self.headers, cookies=self.cookie)

    def post(self, body, endpoint=''):
        uri = self.base_url + endpoint
        return requests.post(uri, json=body, headers=self.headers, cookies=self.cookie)

    def put(self, body, endpoint='', key_id=''):
        uri = self.base_url + endpoint + key_id
        return requests.put(uri, json=body, headers=self.headers, cookies=self.cookie)

    def delete(self, endpoint='', key_id=''):
        uri = self.base_url + endpoint + key_id
        return requests.delete(headers=self.headers, cookies=self.cookie)