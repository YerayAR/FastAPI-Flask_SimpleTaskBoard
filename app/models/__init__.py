"""Expose SQLAlchemy models to be imported easily throughout the project."""

# Currently only the ``User`` model exists, but additional models could be
# added here in the future for convenience of importing.
from .user import User

