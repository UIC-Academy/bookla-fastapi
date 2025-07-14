import os
from datetime import UTC, datetime, timedelta

from fastapi import HTTPException, UploadFile
from jose import jwt
from passlib.context import CryptContext

from app.settings import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    SECRET_KEY,
)

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_jwt_token(data: dict, expires_delta: float | None = None):
    """
    - Creates a new JWT token for logging-in user
    """

    # Access tokenni nima bilan generatsiya qilaman?
    # Access token qanaqa token o'zi?
    delta = (
        timedelta(minutes=expires_delta)
        if expires_delta
        else timedelta(days=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    expire_time = datetime.now(UTC) + delta
    data.update({"exp": expire_time})

    # data = {"username": <>, "password": <>, "role": <>, "exp": <>}

    jwt_token = jwt.encode(data, SECRET_KEY, ALGORITHM)

    return jwt_token


def generate_confirmation_token(email):
    """Generate JWT token"""
    payload = {
        "email": email,
        "exp": datetime.now(UTC) + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# Image Validation

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB


async def validate_image(file: UploadFile):
    # Check file extension
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, "Invalid file type")

    # Check file size
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(400, "File too large")

    return file
