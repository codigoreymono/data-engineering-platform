from services.commerce_api.generators.customers import generate_customers
from services.commerce_api.generators.orders import generate_orders
from services.commerce_api.generators.products import generate_products

CUSTOMERS = generate_customers(
    count=100,
    seed=42,
)

PRODUCTS = generate_products(
    count=50,
    seed=42,
)

ORDERS = generate_orders(
    customers=CUSTOMERS,
    products=PRODUCTS,
    count=200,
    seed=42,
)
