"""Pydantic schemas defining request and response shapes."""

from pydantic import BaseModel

class UserBase(BaseModel):
    """Shared properties between different user schemas."""

    username: str

class UserCreate(UserBase):
    """Schema used for user registration."""

    password: str

class UserRead(UserBase):
    """Schema returned from the API when reading user information."""

    id: int

    class Config:
        # Enable compatibility with SQLAlchemy ORM objects
        orm_mode = True

class Token(BaseModel):
    """Returned by the login endpoint containing the JWT token."""

    access_token: str
    token_type: str

