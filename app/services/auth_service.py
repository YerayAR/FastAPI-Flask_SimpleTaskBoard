"""Service functions related to authentication and user management."""

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from .. import models, schemas
from ..database import SessionLocal
from ..core import security

# OAuth2 scheme used by FastAPI to retrieve the token from request headers
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    """Provide a transactional database session to path operations."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(db: Session, username: str):
    """Retrieve a user record by username."""

    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    """Persist a new user to the database."""

    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    """Validate the provided credentials."""

    user = get_user(db, username)
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Return the current user based on the JWT token."""

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = security.jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(db, username)
    if user is None:
        raise credentials_exception
    return user

