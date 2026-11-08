from pydantic import TypeAdapter

from user_data_pipeline.models.post_response import PostResponse
from user_data_pipeline.models.user_response import UserResponse

user_adapter = TypeAdapter(list[UserResponse])
post_adapter = TypeAdapter(list[PostResponse])


def validate_users(users_raw: list[dict]) -> list[UserResponse]:
    return user_adapter.validate_python(users_raw)


def validate_posts(posts_raw: list[dict]) -> list[PostResponse]:
    return post_adapter.validate_python(posts_raw)
