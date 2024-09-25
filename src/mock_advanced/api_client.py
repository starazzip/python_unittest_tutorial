# src/api_client.py

import requests

class ApiClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})
        self.timeout = timeout

    def get(self, endpoint, params=None):
        return self._send_request('GET', endpoint, params=params)

    def post(self, endpoint, data=None):
        return self._send_request('POST', endpoint, json=data)

    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        request_data = {
            'method': method,
            'url': url,
            'timeout': self.timeout,
            **kwargs
        }
        response = self.session.request(**request_data)
        response.raise_for_status()
        return response.json()
