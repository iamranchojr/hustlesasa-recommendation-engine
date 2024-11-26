from app.models import User
from app.repositories import user_repository


def get_user_by_id(
        user_id: int,
) -> User | None:
    return user_repository.get_user_by_id(
        user_id=user_id,
    )
