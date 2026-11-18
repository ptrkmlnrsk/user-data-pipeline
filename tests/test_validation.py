from typing import Any

import pytest
from pydantic import ValidationError

from user_data_pipeline.models.user_response import Geo, UserResponse
from user_data_pipeline.validation.validators import validate_users


@pytest.fixture
def valid_user_data() -> dict[str, Any]:
    return {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenbofrough",
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


@pytest.mark.parametrize(
    "lat, lng", [(90, 180), (-90, -180), (0, 0), (52.2297, 21.0122)]
)  # warto to dodawac i podawać tutaj w wartosic brzegowe np gdy cos nie dziala
def test_geo_valid_coordinates(lat, lng):
    geo = Geo(lat=lat, lng=lng)

    assert geo.lat == lat
    assert geo.lng == lng


@pytest.mark.parametrize(
    "lat, lng", [(91, 0), (-91, 0), (0, 181), (0, -181), (100, 200)]
)  # warto to dodawac i podawać tutaj w wartosic brzegowe np gdy cos nie dziala
def test_geo_invalid_coordinates(lat, lng):
    with pytest.raises(ValidationError):
        Geo(lat=lat, lng=lng)


def test_geo_invalid_lat_greater_than():
    with pytest.raises(ValidationError) as exc_info:
        Geo(lat=91, lng=100)

    errors = exc_info.value.errors()

    assert errors[0]["loc"] == ("lat",)
    assert errors[0]["type"] == ("less_than_equal")


def test_accept_coordinates_as_strings(valid_user_data: dict[str, Any]):
    users_raw = [valid_user_data]
    validation_result = validate_users(users_raw=users_raw)

    assert validation_result[0].address.geo.lat == -37.3159
    assert validation_result[0].address.geo.lng == 81.1496
    assert isinstance(validation_result[0].address.geo.lat, float)
    assert isinstance(validation_result[0].address.geo.lng, float)


def test_reject_user_id_as_string(valid_user_data: dict[str, Any]):
    valid_user_data["id"] = "1"
    users_raw = [valid_user_data]

    with pytest.raises(ValidationError) as exc_info:
        validate_users(users_raw=users_raw)

    errors = exc_info.value.errors()

    assert errors[0]["loc"] == (0, "id")


# test integracyjny sprawdza data flow


def test_validate_users_data(valid_user_data: dict[str, Any]):  # test integracyjny
    users_raw = [valid_user_data]

    result = validate_users(users_raw)

    assert len(result) == 1
    assert isinstance(result[0], UserResponse)
    assert result[0].id == 1


def test_validate_incomplete_users_data(valid_user_data: dict[str, Any]):
    del valid_user_data["address"]  # test integracyjny
    users_raw = [valid_user_data]

    with pytest.raises(ValidationError) as exc_info:
        validate_users(users_raw)

    errors = exc_info.value.errors()

    assert errors[0]["loc"] == (0, "address")


def test_invalid_field_types_in_users_data(
    valid_user_data: dict[str, Any],
):  # test integracyjny
    valid_user_data["id"] = "1"
    users_raw = [valid_user_data]

    with pytest.raises(ValidationError):
        validate_users(users_raw)
