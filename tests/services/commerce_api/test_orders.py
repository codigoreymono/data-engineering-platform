from fastapi.testclient import TestClient
from services.commerce_api.main import app

client = TestClient(app)


def test_get_orders_default_page():
    response = client.get("/orders")

    assert response.status_code == 200

    body = response.json()

    assert body["page"] == 1
    assert body["page_size"] == 20
    assert body["total"] == 200
    assert len(body["data"]) == 20
    assert body["data"][0]["order_id"] == "ORD000001"


def test_get_orders_second_page():
    response = client.get(
        "/orders",
        params={
            "page": 2,
            "page_size": 3,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["page"] == 2
    assert body["page_size"] == 3
    assert len(body["data"]) == 3
    assert body["data"][0]["order_id"] == "ORD000004"


def test_get_orders_rejects_invalid_page():
    response = client.get(
        "/orders",
        params={"page": 0},
    )

    assert response.status_code == 422


def test_orders_reference_existing_customers_and_products():
    customers_response = client.get(
        "/customers",
        params={"page_size": 100},
    )
    products_response = client.get(
        "/products",
        params={"page_size": 100},
    )

    orders_page_1 = client.get(
        "/orders",
        params={"page": 1, "page_size": 100},
    )
    orders_page_2 = client.get(
        "/orders",
        params={"page": 2, "page_size": 100},
    )

    customer_ids = {
        customer["customer_id"] for customer in customers_response.json()["data"]
    }

    product_ids = {
        product["product_id"] for product in products_response.json()["data"]
    }

    orders = orders_page_1.json()["data"] + orders_page_2.json()["data"]

    assert all(order["customer_id"] in customer_ids for order in orders)

    assert all(
        item["product_id"] in product_ids for order in orders for item in order["items"]
    )
