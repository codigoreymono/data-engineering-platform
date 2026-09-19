from collections.abc import Sequence
from datetime import timedelta
from random import Random

from services.commerce_api.schemas.customer import Customer
from services.commerce_api.schemas.order import Order, OrderItem, OrderStatus
from services.commerce_api.schemas.product import Product

STATUSES = (
    OrderStatus.PENDING,
    OrderStatus.PAID,
    OrderStatus.SHIPPED,
    OrderStatus.DELIVERED,
    OrderStatus.CANCELLED,
)

STATUS_WEIGHTS = (
    0.05,
    0.10,
    0.15,
    0.60,
    0.10,
)


def generate_orders(
    customers: Sequence[Customer],
    products: Sequence[Product],
    count: int = 200,
    seed: int = 42,
) -> list[Order]:
    if not customers:
        raise ValueError("customers cannot be empty")

    if not products:
        raise ValueError("products cannot be empty")

    rng = Random(seed)

    orders = []

    for index in range(1, count + 1):
        customer = rng.choice(customers)

        item_count = rng.randint(
            1,
            min(4, len(products)),
        )

        selected_products = rng.sample(
            products,
            k=item_count,
        )

        items = [
            OrderItem(
                product_id=product.product_id,
                quantity=rng.randint(1, 5),
                unit_price=round(
                    product.unit_price * rng.uniform(0.85, 1.0),
                    2,
                ),
            )
            for product in selected_products
        ]

        earliest_order_date = max(
            customer.created_at,
            *(product.created_at for product in selected_products),
        )

        order = Order(
            order_id=f"ORD{index:06d}",
            customer_id=customer.customer_id,
            status=rng.choices(
                STATUSES,
                weights=STATUS_WEIGHTS,
                k=1,
            )[0],
            created_at=earliest_order_date
            + timedelta(
                days=rng.randint(0, 180),
                seconds=rng.randint(0, 86_399),
            ),
            items=items,
        )

        orders.append(order)

    return orders
