"""Routes exposing item related endpoints."""

from fastapi import APIRouter, Depends

from ..services import auth_service
from ..schemas import UserRead

# This router is grouped under the "/items" prefix
router = APIRouter(prefix="/items", tags=["items"])


@router.get("/me", response_model=UserRead)
async def read_users_me(current_user=Depends(auth_service.get_current_user)):
    """Return information about the currently authenticated user."""
    return current_user

