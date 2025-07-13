from fastapi import APIRouter, BackgroundTasks

from app.dependencies import current_user_dep
from app.schemas import UserOut
from app.tasks import write_notification

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/profile", response_model=UserOut)
async def get_profile(current_user: current_user_dep):
    return current_user


@router.post("/send_notification/{email}")
async def send_test_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
