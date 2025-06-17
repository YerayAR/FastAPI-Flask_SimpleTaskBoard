"""Routes related to user registration and authentication."""

from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import schemas
from ..services import auth_service
from ..core import security

# Router without a prefix as endpoints are at the root (e.g. /register)
router = APIRouter(prefix="", tags=["auth"])


@router.post("/register", response_model=schemas.UserRead)
def register(user: schemas.UserCreate, db: Session = Depends(auth_service.get_db)):
    """Create a new user account if the username is not taken."""

    db_user = auth_service.get_user(db, user.username)
    if db_user:
        # Username already exists in the database
        raise HTTPException(status_code=400, detail="Username already registered")

    user = auth_service.create_user(db, user)
    return user


@router.post("/token", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(auth_service.get_db),
):
    """Authenticate the user and return a JWT access token."""

    user = auth_service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Generate JWT token with expiration
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

