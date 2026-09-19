from datetime import datetime, timedelta, timezone
from random import Random

from services.commerce_api.schemas.customer import Customer

FIRST_NAMES = (
    "Ana",
    "Luis",
    "Carlos",
    "Sofia",
    "Diego",
    "Laura",
    "Miguel",
    "Elena",
)

LAST_NAMES = (
    "Garcia",
    "Martinez",
    "Lopez",
    "Hernandez",
    "Gonzalez",
    "Perez",
    "Ramirez",
    "Torres",
)

LOCATIONS = (
    ("Monterrey", "Nuevo Leon", "64000"),
    ("Guadalajara", "Jalisco", "44100"),
    ("Merida", "Yucatan", "97000"),
    ("Puebla", "Puebla", "72000"),
    ("Queretaro", "Queretaro", "76000"),
    ("Villahermosa", "Tabasco", "86000"),
)

START_DATE = datetime(2025, 1, 1, tzinfo=timezone.utc)


def generate_customers(
    count: int = 100,
    seed: int = 42,
) -> list[Customer]:
    rng = Random(seed)

    customers = []

    for index in range(1, count + 1):
        first_name = rng.choice(FIRST_NAMES)
        last_name = rng.choice(LAST_NAMES)
        city, state, postal_code = rng.choice(LOCATIONS)

        customer_id = f"CUS{index:05d}"

        created_at = START_DATE + timedelta(
            days=rng.randint(0, 365),
            seconds=rng.randint(0, 86_399),
        )

        customer = Customer(
            customer_id=customer_id,
            full_name=f"{first_name} {last_name}",
            email=(
                f"{first_name.lower()}."
                f"{last_name.lower()}."
                f"{customer_id.lower()}@example.com"
            ),
            city=city,
            state=state,
            postal_code=postal_code,
            created_at=created_at,
        )

        customers.append(customer)

    return customers
