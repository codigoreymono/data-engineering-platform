from datetime import datetime, timedelta, timezone
from random import Random

from services.commerce_api.schemas.product import Product

PRODUCTS_BY_CATEGORY = {
    "electronics": (
        "Wireless Headphones",
        "Mechanical Keyboard",
        "USB-C Hub",
        "Webcam",
        "Portable Speaker",
    ),
    "home": (
        "Desk Lamp",
        "Coffee Maker",
        "Storage Box",
        "Electric Kettle",
        "Table Fan",
    ),
    "office": (
        "Notebook",
        "Desk Organizer",
        "Office Chair",
        "Monitor Stand",
        "Whiteboard",
    ),
    "sports": (
        "Yoga Mat",
        "Water Bottle",
        "Resistance Bands",
        "Training Gloves",
        "Running Belt",
    ),
}

START_DATE = datetime(2025, 1, 1, tzinfo=timezone.utc)


def generate_products(
    count: int = 50,
    seed: int = 42,
) -> list[Product]:
    rng = Random(seed)

    products = []

    categories = tuple(PRODUCTS_BY_CATEGORY)

    for index in range(1, count + 1):
        category = rng.choice(categories)
        name = rng.choice(PRODUCTS_BY_CATEGORY[category])

        product = Product(
            product_id=f"PRD{index:05d}",
            name=name,
            category=category,
            unit_price=round(rng.uniform(10.0, 1_500.0), 2),
            active=rng.random() >= 0.1,
            created_at=START_DATE
            + timedelta(
                days=rng.randint(0, 365),
                seconds=rng.randint(0, 86_399),
            ),
        )

        products.append(product)

    return products
