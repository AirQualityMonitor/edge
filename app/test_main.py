import pytest

from app import app
from fastapi.testclient import TestClient
from fastapi import status


def test_get_initial_data():
    client = TestClient(app)
    response = client.get("/metric")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {}


def test_add_metric():
    client = TestClient(app)
    payload = {"name": "Temp", "unit": "C", "value": 24.3}
    response = client.post("/metric", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == payload


@pytest.mark.parametrize(
    "payload, message",
    [
        ({"name": "Temp", "unit": "C", "value": "hot"}, "value is not a valid float"),
        (
            {"name": "", "unit": "C", "value": 24.3},
            "name should contain from 1 to 7 characters",
        ),
        (
            {"name": "01234567", "unit": "C", "value": 24.3},
            "name should contain from 1 to 7 characters",
        ),
        (
            {"unit": "C", "value": 24.3},
            "field required",
        ),
    ],
)
def test_add_metric_with_wrong_payload(payload, message):
    client = TestClient(app)
    response = client.post("/metric", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == message


def test_get_last_metric():
    client = TestClient(app)
    first_payload = {"name": "Temp", "unit": "C", "value": 24.3}
    client.post("/metric", json=first_payload)
    second_payload = {"name": "RH", "unit": "%", "value": 50.12}
    client.post("/metric", json=second_payload)
    response = client.get("/metric")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"name": "RH", "unit": "%", "value": 50.12}
