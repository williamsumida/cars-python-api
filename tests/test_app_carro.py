from fastapi.testclient import TestClient
from cars_python_api.app import app

client = TestClient(app)


def test_get_carros():
    response = client.get("/carro")
    assert response.status_code == 200
