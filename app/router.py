from fastapi import APIRouter, Query

from app.services import recommendation_service, user_service
from app.models import Product

router = APIRouter()


@router.get('/recommend-products')
async def recommend_products(
        user_id: int = None,
) -> list[Product]:
    user = None
    if user_id:
        user = user_service.get_user_by_id(
            user_id=user_id
        )

        # even if user is not found, we still want to proceed

    return recommendation_service.recommend_products(
        user=user
    )
