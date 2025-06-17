"""Integration tests for task CRUD endpoints."""

import os
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, engine

client = TestClient(app)


def setup_module(module):
    """Ensure a clean database for task tests."""
    if os.path.exists("test.db"):
        os.remove("test.db")
    Base.metadata.create_all(bind=engine)


def test_task_crud_flow():
    """Create, list and delete tasks through the API."""

    # Create a new task
    response = client.post("/tasks/", json={"title": "Test", "description": "demo"})
    assert response.status_code == 200
    task = response.json()
    assert task["title"] == "Test"

    # List tasks should contain the created one
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1

    # Delete the task
    response = client.delete(f"/tasks/{task['id']}")
    assert response.status_code == 204

    # Ensure list is empty again
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []
