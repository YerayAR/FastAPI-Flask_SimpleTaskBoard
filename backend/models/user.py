"""SQLAlchemy model definitions."""

# Basic column types for the ORM model
from sqlalchemy import Column, Integer, String

# Base class imported from the application's database module
from ..config.database import Base

class User(Base):
    """Represents a registered user in the system."""

    __tablename__ = "users"

    # Surrogate primary key
    id = Column(Integer, primary_key=True, index=True)

    # Unique username used for login
    username = Column(String, unique=True, index=True)

    # Password hash stored using bcrypt
    hashed_password = Column(String)

