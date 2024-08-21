from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from schemas.user_schemas import User, UserCreate
from managers.user_manager import UserManager
from auth.password import hash_password, check_hashed_password
from auth.token import create_access_token
from schemas.auth_schemas import TokenResp, CredentialsReq

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/create", response_model=User, status_code=status.HTTP_201_CREATED)
async def post_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await UserManager.select_user_by_email(user_data.email, db)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered!",
        )
    user_data.password = hash_password(user_data.password)
    new_user = await UserManager.insert_user(user_data, db)
    return new_user


@user_router.post("/login", response_model=TokenResp)
async def login_user(credentials: CredentialsReq, db: AsyncSession = Depends(get_db)):
    existing_user = await UserManager.select_user_by_email(credentials.email, db, True)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad credentials!",
        )

    if not check_hashed_password(existing_user.password, credentials.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad credentials!",
        )

    access_token = create_access_token(existing_user.id)
    response = TokenResp(access_token=access_token)

    return response
