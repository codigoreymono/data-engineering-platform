from datetime import datetime

from pydantic import BaseModel


class Customer(BaseModel):
    customer_id: str
    full_name: str
    email: str
    city: str
    state: str
    postal_code: str
    created_at: datetime


class CustomerPage(BaseModel):
    data: list[Customer]
    page: int
    page_size: int
    total: int
