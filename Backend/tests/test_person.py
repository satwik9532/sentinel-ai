from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_person():

    payload = {
        "first_name": "Satwik",
        "last_name": "Mishra",
        "phone_number": "9999999999",
        "email": "satwik@test.com",
    }

    response = client.post(
        "/api/v1/persons",
        json=payload,
    )

    assert response.status_code == 201