# tests/api_mock_fixture.py

from unittest.mock import Mock
import requests

class ApiMockFixture:
    def _mock_request(self, mock_request, status_code=200, json_data=None, headers=None, raise_for_status=None, side_effect=None):
        mock_response = Mock(spec=requests.Response)
        mock_response.status_code = status_code
        mock_response.json.return_value = json_data
        mock_response.headers = headers or {}
        mock_response.raise_for_status.side_effect = raise_for_status

        if side_effect:
            mock_request.side_effect = side_effect
        else:
            mock_request.return_value = mock_response
