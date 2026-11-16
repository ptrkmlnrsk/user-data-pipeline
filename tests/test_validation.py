import pytest
from pydantic import ValidationError

from user_data_pipeline.models.user_response import Geo, UserResponse
from user_data_pipeline.validation.validators import validate_users


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
    print(errors)
    print(exc_info)

    assert errors[0]["loc"] == ("lat",)
    assert errors[0]["type"] == ("less_than_equal")
    assert False


def test_accept_coordinates_as_strings():
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
    validation_result = validate_users(users_raw=users_raw)

    assert validation_result[0].address.geo.lat == -37.3159
    assert validation_result[0].address.geo.lng == 81.1496
    assert isinstance(validation_result[0].address.geo.lat, float)
    assert isinstance(validation_result[0].address.geo.lng, float)


# test integracyjny sprawdza data flow


def test_validate_users_data():  # test integracyjny
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


def test_validate_incomplete_users_data():  # test integracyjny
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


def test_invalid_field_types_in_users_data():  # test integracyjny
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
