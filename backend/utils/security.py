"""Security helpers for password hashing and JWT operations."""

from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt

# NOTE: In a real application these values should come from configuration or
# environment variables.
SECRET_KEY = "secret"  # in production use env var
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Generate a signed JWT token."""

    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

from passlib.context import CryptContext

# Configure passlib to use bcrypt for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Validate a plaintext password against a hash."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password for storing in the database."""
    return pwd_context.hash(password)

