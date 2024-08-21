from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from schemas.user_schemas import User, UserCreate
from managers.user_manager import UserManager
from auth.password import hash_password, check_hashed_password

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/create", response_model=User, status_code=status.HTTP_201_CREATED)
async def post_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await UserManager.select_user_by_email(
        user_data.email, db
    )
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered!",
        )
    user_data.password = hash_password(user_data.password)
    new_user = await UserManager.insert_user(user_data, db)
    return new_user
