from datetime import datetime

from pydantic import BaseModel


class Product(BaseModel):
    product_id: str
    name: str
    category: str
    unit_price: float
    active: bool
    created_at: datetime
