from fastapi.testclient import testclient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    responde = client.get("/health")

    assert response.status_code == 200
    assert responde.json()["status"] == "ok"