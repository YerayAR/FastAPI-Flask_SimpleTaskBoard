"""Tests covering the registration and authentication workflow."""

import os
import pytest
from fastapi.testclient import TestClient

from backend.main import app
from backend.config.database import Base, engine

# Create a test client that will call into our FastAPI app
client = TestClient(app)


def setup_module(module):
    """Reset the database before the tests run."""

    if os.path.exists("test.db"):
        os.remove("test.db")
    Base.metadata.create_all(bind=engine)


def test_register_and_login():
    """Ensure a user can register, login and access a protected route."""

    # Register a new user
    response = client.post("/register", json={"username": "alice", "password": "secret"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert "id" in data

    # Login and acquire token
    response = client.post("/token", data={"username": "alice", "password": "secret"})
    assert response.status_code == 200
    token = response.json()["access_token"]
    assert token

    # Access a protected route using the token
    response = client.get("/items/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
