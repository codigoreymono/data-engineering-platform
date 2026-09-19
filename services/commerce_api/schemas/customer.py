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
