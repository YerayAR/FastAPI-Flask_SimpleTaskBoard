"""Definiciones de modelo ORM para tareas."""
from sqlalchemy import Column, Integer, String

from ..config.database import Base

class Task(Base):
    """Simple task model used for demo purposes."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
