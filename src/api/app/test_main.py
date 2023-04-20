from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)

def test_read_menu():
      response = client.get("/lunch/malid")
      assert response.status_code == 200
      assert len(response.json()["menu"]) <= 7
      assert len(response.json()["menu"]) >= 4
