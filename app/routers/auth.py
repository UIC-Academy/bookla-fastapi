from fastapi import APIRouter, HTTPException
from jose import JWTError, jwt

from app.dependencies import db_dep
from app.models import User
from app.schemas import TokenIn, UserOut, UserRegisterIn
from app.utils import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    REFRESH_TOKEN_EXPIRE_MINUTES,
    SECRET_KEY,
    create_jwt_token,
    hash_password,
    verify_password,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut)
async def register_user(db: db_dep, register_data: UserRegisterIn):
    is_user_exists = db.query(User).filter(User.email == register_data.email).first()

    if is_user_exists:
        raise HTTPException(status_code=400, detail="User already exists")

    is_first_user = db.query(User).count() == 0

    if is_first_user:
        user = User(
            email=register_data.email,
            password=hash_password(register_data.password),
            is_admin=True,
        )
    else:
        user = User(**register_data.model_dump())

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login")
async def login_user(db: db_dep, login_data: UserRegisterIn):
    user = db.query(User).filter(User.email == login_data.email).first()

    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=400, detail="User not found or you entered wrong credentials."
        )

    login_dict = {"email": user.email, "is_admin": user.is_admin}

    access_token = create_jwt_token(
        data=login_dict, expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    refresh_token = create_jwt_token(
        data=login_dict, expires_delta=REFRESH_TOKEN_EXPIRE_MINUTES
    )

    response = {"access_token": access_token, "refresh_token": refresh_token}

    return response


@router.post("/refresh")
async def get_access_token(db: db_dep, token_data: TokenIn):
    try:
        payload = jwt.decode(
            token_data.refresh_token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"verify_exp": True},
        )
        email: str = payload.get("email")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")

        new_access_token = create_jwt_token(
            data={"email": email}, expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES
        )

        response = {
            "access_token": new_access_token,
            "refresh_token": token_data.refresh_token,
            "token_type": "bearer",
        }

        return response

    except JWTError as err:
        raise HTTPException(status_code=401, detail="Invalid refresh token") from err
    except jwt.ExpiredSignatureError as err:
        raise HTTPException(
            status_code=401, detail="Refresh token has expired"
        ) from err
    except Exception as err:
        raise HTTPException(
            status_code=400, detail="Something went wrong. Please try again later."
        ) from err
