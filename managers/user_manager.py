from typing import Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.user_model import UserModel
from schemas.user_schemas import User, UserCreate, UserWithPass


class UserManager:
    @staticmethod
    async def insert_user(user_data: UserCreate, db: AsyncSession) -> User:
        user = UserModel(**user_data.model_dump())
        db.add(user)
        await db.commit()
        return User.model_validate(user)

    @staticmethod
    async def select_user_by_email(user_email: str, db: AsyncSession, with_pass: bool = False) -> Optional[Union[User, UserWithPass]]:
        query_result = await db.execute(
            select(UserModel).where(UserModel.email == user_email)
        )
        user = query_result.scalar_one_or_none()
        if not user:
            return None
        
        resp_model = UserWithPass if with_pass else User
        return resp_model.model_validate(user)
