from urllib import response
from fastapi.testclient import TestClient
from app.main import app
import pytest
import math
from random import randint

client = TestClient(app)

def test_home():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() ==  "Hello World"

def test_calculate_sqrt():
  response = client.get("/4")
  assert response.status_code == 200
  assert response.json() == 16

def test_calculate_twice():
  response = client.get("/twice/3")
  assert response.status_code == 200
  assert response.json() == 18

list_of_numbers = [randint(1, 10) for _ in range(10)]


@pytest.mark.parametrize('number', list_of_numbers)
def test_return_sqrt_twice(number: int):
  response =client.get(f"/twice/{number}")
  assert response.status_code == 200
  assert response.json() == math.pow(number, 2) * 2