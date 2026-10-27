from unittest.mock import Mock, patch

from src.user_data_pipeline.data_access.api_client import JSONPlaceholderClient


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

    with patch("user_data_pipeline.data_access.api_client.requests.get") as mock_get:
        mock_get.return_value = mock_response  # udaje funkcje requests.get()

        result = client.get_users()
        # realne wykonanie funkcji ale z podmienionym requests.get() przez patch()

    # Assert - sprawdzenie wyniku
    assert result == expected_users

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5.0,
    )

    mock_response.raise_for_status.assert_called_once_with()
