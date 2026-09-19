from fastapi import APIRouter, Query

from services.commerce_api.dataset import CUSTOMERS
from services.commerce_api.schemas.customer import Customer
from services.commerce_api.schemas.page import Page

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
)


@router.get("", response_model=Page[Customer])
def get_customers(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> Page[Customer]:
    start = (page - 1) * page_size
    end = start + page_size

    return Page[Customer](
        data=CUSTOMERS[start:end],
        page=page,
        page_size=page_size,
        total=len(CUSTOMERS),
    )
