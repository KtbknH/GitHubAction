from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate_sqrt(mocker):
  mocker.patch(
    "App.main.get_square",
    return_value=16
  )
  result = 32 
  response = client.get("/twice/4")
  assert result == response.json()
  assert response.status_code == 200 

 
