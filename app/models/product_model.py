from pydantic import Field

from .base_model import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: float = Field(..., gt=0)
    category: str
    quantity: int = Field(..., ge=0)
    is_active: bool = True
    popularity_score: int = 0
