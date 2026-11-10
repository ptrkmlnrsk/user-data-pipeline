import logging

from user_data_pipeline.data_access.api_client import JSONPlaceholderClient
from user_data_pipeline.validation.validators import validate_posts, validate_users

logger = logging.getLogger(__name__)


def run_pipeline():
    logger.info("Define client")
    client = JSONPlaceholderClient(base_url="https://jsonplaceholder.typicode.com/")

    logger.info("Get users data")
    users_raw = client.get_users()

    logger.info("Get posts data")
    posts_raw = client.get_posts()

    logger.info("Validate users data")
    validate_users(users_raw)

    logger.info("Validate posts data")
    validate_posts(posts_raw)

    # zapis surówki do bazy
    # save_to_database()

    # tutaj dopier user i posts powinno wejsc do pydantica
