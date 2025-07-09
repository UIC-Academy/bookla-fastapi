from fastapi import APIRouter

from app.dependencies import current_user_dep
from app.schemas import UserOut

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/profile", response_model=UserOut)
async def get_profile(current_user: current_user_dep):
    return current_user
