"""
    Test File for Main function
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_version():
    """
    Test to check the application version
    """
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.json()
    assert response.json()["version"] == app.version
