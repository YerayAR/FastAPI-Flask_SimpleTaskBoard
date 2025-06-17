"""Database configuration for the project."""

# SQLAlchemy components used for creating the SQLite engine, base class and
# session factory
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Using a local SQLite database file for simplicity. In production this would be
# configurable via environment variables.
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine. `check_same_thread=False` is required for using
# SQLite with FastAPI as the web server runs in multiple threads.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Factory for creating new database sessions for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()

