from user_data_pipeline.data_access.api_client import JSONPlaceholderClient

from user_data_pipeline.models.response import User


def run():
    client = JSONPlaceholderClient(base_url="https://jsonplaceholder.typicode.com/")

    users_raw = client.get_users()
    # posts = client.get_posts()

    print(users_raw)

    validate_users(users_raw)

    # validate(users)
    # zapis surówki do bazy
    # save_to_database()

    # tutaj dopier user i posts powinno wejsc do pydantica


def validate_users(users_raw: list[dict]):
    return [User.model_validate(user) for user in users_raw]


def validate_posts(posts_raw: list[dict]):
    # return Posts(**posts_raw)
    pass


def save_to_database():
    pass


run()
