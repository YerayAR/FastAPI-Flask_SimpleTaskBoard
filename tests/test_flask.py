"""Tests for the Flask front-end routes."""

import os
from frontend import create_app


def test_index_route():
    """Index should render with the API URL injected."""
    os.environ['FASTAPI_URL'] = 'http://api'
    app = create_app()
    client = app.test_client()

    response = client.get('/')
    assert response.status_code == 200
    assert b'Cyberpunk Task Board' in response.data
