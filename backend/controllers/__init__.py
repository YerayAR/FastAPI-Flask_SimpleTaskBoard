"""Expose the different API routers used by the application."""

# Individual router modules implementing API endpoints
from . import auth, items, tasks

# Allow ``from backend.controllers import auth`` style imports
__all__ = ["auth", "items", "tasks"]

