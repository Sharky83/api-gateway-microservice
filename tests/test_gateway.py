import pytest
from fastapi.testclient import TestClient
from api_gateway import app

client = TestClient(app)

# Mock backend services for testing
# You may need to mock httpx.AsyncClient for full integration

def test_proxy_service1_health():
    response = client.get("/proxy/service1/health")
    assert response.status_code in [200, 404, 502]

def test_proxy_service2_health():
    response = client.get("/proxy/service2/health")
    assert response.status_code in [200, 404, 502]

def test_proxy_invalid_service():
    response = client.get("/proxy/invalid/health")
    assert response.status_code == 404

def test_proxy_missing_auth():
    response = client.get("/proxy/service1/health")
    assert response.status_code in [200, 404, 502]

# Add more tests for POST, PUT, DELETE as needed
