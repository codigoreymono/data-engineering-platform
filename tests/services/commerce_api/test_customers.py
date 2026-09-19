from fastapi.testclient import TestClient
from services.commerce_api.main import app

client = TestClient(app)


def test_get_customers_default_page():
    response = client.get("/customers")

    assert response.status_code == 200

    body = response.json()

    assert body["page"] == 1
    assert body["page_size"] == 20
    assert body["total"] == 100
    assert len(body["data"]) == 20
    assert body["data"][0]["customer_id"] == "CUS00001"


def test_get_customers_second_page():
    response = client.get(
        "/customers",
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
    assert body["data"][0]["customer_id"] == "CUS00004"


def test_get_customers_rejects_invalid_page():
    response = client.get(
        "/customers",
        params={"page": 0},
    )

    assert response.status_code == 422
