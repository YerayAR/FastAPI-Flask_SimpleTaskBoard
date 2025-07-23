"""Esquemas Pydantic para la entidad Task."""
from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: int

    class Config:
        orm_mode = True
