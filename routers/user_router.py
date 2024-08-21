from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from schemas.user_schemas import User, UserCreate
from managers.user_manager import UserManager

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/create", response_model=User)
async def post_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await UserManager.insert_user(user_data, db)
    return user
