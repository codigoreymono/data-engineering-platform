from fastapi import APIRouter, Query

from services.commerce_api.generators.products import generate_products
from services.commerce_api.schemas.page import Page
from services.commerce_api.schemas.product import Product

router = APIRouter(
    prefix="/products",
    tags=["products"],
)

PRODUCTS = generate_products(count=50, seed=42)


@router.get("", response_model=Page[Product])
def get_products(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> Page[Product]:
    start = (page - 1) * page_size
    end = start + page_size

    return Page[Product](
        data=PRODUCTS[start:end],
        page=page,
        page_size=page_size,
        total=len(PRODUCTS),
    )
