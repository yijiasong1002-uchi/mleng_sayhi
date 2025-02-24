"""
This module contains tests for the FastAPI application.
"""

from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)

def test_get_status():
    """Test the /status endpoint."""
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_say_hi():
    """Test the /sayhi/{name} endpoint."""
    response = client.get("/sayhi/Alice")
    assert response.status_code == 200
    assert response.json() == {"message": "Hi, Alice!"}

def test_sum_numbers():
    """Test the /sum endpoint."""
    response = client.post("/sum", json={"a": 3, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"sum": 8}
