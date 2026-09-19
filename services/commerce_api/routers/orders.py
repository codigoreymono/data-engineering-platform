from fastapi import APIRouter, Query

from services.commerce_api.dataset import ORDERS
from services.commerce_api.schemas.order import Order
from services.commerce_api.schemas.page import Page

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)


@router.get("", response_model=Page[Order])
def get_orders(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> Page[Order]:
    start = (page - 1) * page_size
    end = start + page_size

    return Page[Order](
        data=ORDERS[start:end],
        page=page,
        page_size=page_size,
        total=len(ORDERS),
    )
