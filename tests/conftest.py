import pytest
from fastapi.testclient import TestClient

from intro_fastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
