import pytest
from pydantic import ValidationError

from user_data_pipeline.models.user_response import UserResponse
from user_data_pipeline.validation.validators import validate_users


def test_validate_users_data():
    users_raw = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {"lat": "-37.3159", "lng": "81.1496"},
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets",
            },
        }
    ]

    result = validate_users(users_raw)

    assert len(result) == 1
    assert isinstance(result[0], UserResponse)
    assert result[0].id == 1


def test_validate_incomplete_users_data():
    users_raw = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "geo": {"lat": "-37.3159", "lng": "81.1496"},
            },
            "phone": "1-770-736-8031 x56442",
            "company": {
                "name": "Romaguera-Crona",
                "bs": "harness real-time e-markets",
            },
        }
    ]

    with pytest.raises(ValidationError):
        validate_users(users_raw)


def test_invalid_field_types_in_users_data():
    users_raw = [
        {
            "id": "1",
            "name": ["Leanne Graham"],
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": 929983874,
                "geo": ("lat", "-37.3159", "lng", "81.1496"),
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets",
            },
        }
    ]

    with pytest.raises(ValidationError):
        validate_users(users_raw)
