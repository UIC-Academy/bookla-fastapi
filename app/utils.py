import os
from datetime import UTC, datetime, timedelta

from dotenv import load_dotenv
from jose import jwt
from passlib.context import CryptContext

load_dotenv()


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))


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
