# tests/test_api_client.py
import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
import unittest
from unittest.mock import Mock, patch

import requests

from src.mock_advanced.api_client import ApiClient
from tests.fixtures.api_mock_fixture import ApiMockFixture


@patch('requests.Session.request')
class TestApiClient(unittest.TestCase, ApiMockFixture):

    def setUp(self):
        self.base_url = 'http://testserver.com'
        self.client = ApiClient(self.base_url)

    def test_get_success(self, mock_request):
        # Arrange
        self._mock_request(mock_request,
                           status_code=200,
                           json_data={'message': 'success'},
                           raise_for_status=None)

        # Action
        response = self.client.get('api/test', params={'key': 'value'})

        # Assert
        self.assertEqual(response, {'message': 'success'})
        mock_request.assert_called_once_with(method='GET',
                                             url='http://testserver.com/api/test',
                                             timeout=10,
                                             params={'key': 'value'})

    def test_post_success(self, mock_request):
        # Arrange
        self._mock_request(mock_request,
                           status_code=201,
                           json_data={
                               'id': 1,
                               'status': 'created'
                           },
                           raise_for_status=None)

        # Action
        data = {'name': 'test'}
        response = self.client.post('api/create', data=data)

        #Assert
        self.assertEqual(response, {'id': 1, 'status': 'created'})
        mock_request.assert_called_once_with(method='POST',
                                             url='http://testserver.com/api/create',
                                             timeout=10,
                                             json=data)


if __name__ == '__main__':
    unittest.main()
