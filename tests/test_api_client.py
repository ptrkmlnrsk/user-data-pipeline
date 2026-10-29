from unittest.mock import Mock, patch

import pytest
import requests

from src.user_data_pipeline.data_access.api_client import JSONPlaceholderClient


class FakeResponse:
    def __init__(self, payload, status_code=200):
        self.payload = payload
        self.status_code = status_code

    # stworzenie obiektu który bede mogl przekazać jako fake resposne

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP{self.status_code}")

    def json(self):
        return self.payload


def test_get_returns_json_list(monkeypatch):
    client = JSONPlaceholderClient(base_url="https://example.test/")

    def fake_get(base_url, timeout):
        assert base_url == "https://example.test/users"
        assert timeout == 10.0

        return FakeResponse([{"id": 1}])

    monkeypatch.setattr(client.session, "get", fake_get)
    assert client.get_users() == [{"id": 1}]


def test_get_raises_for_http_error(monkeypatch):
    client = JSONPlaceholderClient(base_url="https://example.test/")

    def fake_get(base_url, timeout):
        return FakeResponse([], status_code=500)

    monkeypatch.setattr(client.session, "get", fake_get)

    with pytest.raises(requests.HTTPError):
        client.get_users()


def test_get_users_returns_valid_data():
    expected_users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"},
    ]

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = expected_users
    # mock_resposne udaje odpowiedź HTTP

    client = JSONPlaceholderClient(
        base_url="https://jsonplaceholder.typicode.com",
        timeout=5.0,
    )

    with patch.object(client.session, "get", return_value=mock_response) as mock_get:
        # udaje funkcje requests.get() i zwraca zmockowany obiekt
        result = client.get_users()
        # realne wykonanie funkcji ale z podmienionym requests.get() przez patch()

    # Assert - sprawdzenie wyniku
    assert result == expected_users

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5.0,
    )

    mock_response.raise_for_status.assert_called_once_with()
