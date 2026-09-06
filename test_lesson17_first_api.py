"""
Professionalization pass: automated tests for Lesson 17's FastAPI app.

Demonstrates testing a FastAPI application with TestClient - sending
real requests to the app in-memory (no server needed) and asserting
on status codes and response bodies. This is standard professional
practice: an API without tests is a real production risk.
"""

from fastapi.testclient import TestClient
from lesson17_first_api import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}


def test_get_student():
    response = client.get("/students/5")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 5
    assert data["name"] == "Abdalla"


def test_create_student():
    response = client.post("/students", params={"name": "Sara", "age": 19})
    assert response.status_code == 200
    assert "Sara" in response.json()["message"]
    assert "19" in response.json()["message"]
