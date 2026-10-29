from user_data_pipeline.data_access.api_client import JSONPlaceholderClient


def run():
    client = JSONPlaceholderClient(base_url="https://jsonplaceholder.typicode.com/")

    users = client.get_users()
    # posts = client.get_posts()

    print(users)

    # validate(users)
    # zapis surówki do bazy
    save_to_database()

    # tutaj dopier user i posts powinno wejsc do pydantica


def validate(data: list[dict]):
    pass


def save_to_database():
    pass


run()
