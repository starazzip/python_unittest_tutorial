# tests/test_api_client.py
import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
from tests.fixtures.api_mock_fixture import ApiMockFixture
import unittest
from unittest.mock import patch, Mock
from src.mock_advanced.api_client import ApiClient
import requests

class TestApiClient(unittest.TestCase, ApiMockFixture):
    def setUp(self):
        self.base_url = 'http://testserver.com'
        self.client = ApiClient(self.base_url)
        
    @patch('src.mock_advanced.api_client.requests.Session.request')
    def test_get_success(self, mock_request):
        self._mock_request(
            mock_request,
            status_code=200,
            json_data={'message': 'success'},
            raise_for_status=None
        )

        response = self.client.get('api/test', params={'key': 'value'})

        self.assertEqual(response, {'message': 'success'})
        mock_request.assert_called_once_with(
            method='GET',
            url='http://testserver.com/api/test',
            timeout=10,
            params={'key': 'value'}
        )

    @patch('src.mock_advanced.api_client.requests.Session.request')
    def test_post_success(self, mock_request):
        self._mock_request(
            mock_request,
            status_code=201,
            json_data={'id': 1, 'status': 'created'},
            raise_for_status=None
        )

        data = {'name': 'test'}
        response = self.client.post('api/create', data=data)

        self.assertEqual(response, {'id': 1, 'status': 'created'})
        mock_request.assert_called_once_with(
            method='POST',
            url='http://testserver.com/api/create',
            timeout=10,
            json=data
        )

if __name__ == '__main__':
    unittest.main()
