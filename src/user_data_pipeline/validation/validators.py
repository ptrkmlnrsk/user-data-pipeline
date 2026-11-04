from user_data_pipeline.models.post_response import Post
from user_data_pipeline.models.user_response import User


def validate_users(users_raw: list[dict]):
    return [User.model_validate(user) for user in users_raw]


def validate_posts(posts_raw: list[dict]):
    return [Post.model_validate(post) for post in posts_raw]
