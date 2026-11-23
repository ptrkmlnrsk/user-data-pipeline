from typing import Any

import pytest


@pytest.fixture(
    autouse=False
)  # autouse automatycznie uruchamia sie dla wsyzstkich testow
# True jest dobre do Mockowania API
def valid_user_data() -> dict[str, Any]:
    """Fixture with valid user data."""
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


@pytest.fixture(autouse=False)
def valid_post_data() -> dict[str, Any]:
    return {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    }


# pytest hooks
def pytest_runtest_setup(item):
    print(f"Preparing test {item.name}")
    # fazy ktore moge wykonac przed testami
    # tworzenie kluczy, autoryzacje uzytkownika, cos co nie jest testem


def pytest_runtest_teardown(item):
    print(f"Finishing test {item.name}")


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo is not None:
            print(f"Test failed {item.name}")
        else:
            print(f"Test passed {item.name}")
            # tutaj logger z poziomu CI/CD


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "slow: marks tests as slow",
    )
