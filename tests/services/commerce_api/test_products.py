from fastapi.testclient import TestClient
from services.commerce_api.main import app

client = TestClient(app)


def test_get_products_default_page():
    response = client.get("/products")

    assert response.status_code == 200

    body = response.json()

    assert body["page"] == 1
    assert body["page_size"] == 20
    assert body["total"] == 50
    assert len(body["data"]) == 20
    assert body["data"][0]["product_id"] == "PRD00001"


def test_get_products_second_page():
    response = client.get(
        "/products",
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
    assert body["data"][0]["product_id"] == "PRD00004"


def test_get_products_rejects_invalid_page_size():
    response = client.get(
        "/products",
        params={"page_size": 101},
    )

    assert response.status_code == 422
