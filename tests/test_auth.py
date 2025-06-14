import os
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, engine

client = TestClient(app)


def setup_module(module):
    # ensure fresh db
    if os.path.exists("test.db"):
        os.remove("test.db")
    Base.metadata.create_all(bind=engine)


def test_register_and_login():
    response = client.post("/register", json={"username": "alice", "password": "secret"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert "id" in data

    # login
    response = client.post("/token", data={"username": "alice", "password": "secret"})
    assert response.status_code == 200
    token = response.json()["access_token"]
    assert token

    # access protected route
    response = client.get("/items/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
