from user_data_pipeline.data_access.api_client import JSONPlaceholderClient

from user_data_pipeline.validation.validators import validate_posts, validate_users


def run():
    client = JSONPlaceholderClient(base_url="https://jsonplaceholder.typicode.com/")

    users_raw = client.get_users()
    posts_raw = client.get_posts()

    validate_users(users_raw)
    validate_posts(posts_raw)

    # validate(users)
    # zapis surówki do bazy
    # save_to_database()

    # tutaj dopier user i posts powinno wejsc do pydantica


run()
