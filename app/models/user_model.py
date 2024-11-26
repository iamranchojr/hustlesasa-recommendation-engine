from .base_model import BaseModel


class User(BaseModel):
    name: str
    email: str
