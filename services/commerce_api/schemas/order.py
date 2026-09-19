from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class OrderStatus(StrEnum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class OrderItem(BaseModel):
    product_id: str
    quantity: int = Field(ge=1)
    unit_price: float = Field(gt=0)


class Order(BaseModel):
    order_id: str
    customer_id: str
    status: OrderStatus
    created_at: datetime
    items: list[OrderItem] = Field(min_length=1)
