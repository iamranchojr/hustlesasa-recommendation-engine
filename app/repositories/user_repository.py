import json
from pathlib import Path

from app.models import User


# Path to the JSON file
USERS_DATA_JSON_FILE = Path(__file__).parent.parent / 'data/users_data.json'


def read_users_data() -> list[User]:
    with open(USERS_DATA_JSON_FILE, 'r') as f:
        users_data = json.load(f)

    return [User.model_validate(user) for user in users_data]


def get_users() -> list[User]:
    return read_users_data()


def get_user_by_id(
        user_id: int,
) -> User | None:
    users = read_users_data()

    for user in users:
        if user.id == user_id:
            return user

    return None
