from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.user_model import UserModel
from schemas.user_schemas import User, UserCreate


class UserManager:
    @staticmethod
    async def insert_user(user_data: UserCreate, db: AsyncSession) -> User:
        user = UserModel(**user_data.model_dump())
        db.add(user)
        await db.commit()
        return User.model_validate(user)

    @staticmethod
    async def select_user_by_email(user_email: str, db: AsyncSession) -> Optional[User]:
        query_result = await db.execute(
            select(UserModel).where(UserModel.email == user_email)
        )
        user = query_result.scalar_one_or_none()
        if not user:
            return None
        return User.model_validate(user)
