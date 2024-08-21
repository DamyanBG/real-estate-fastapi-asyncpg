from sqlalchemy.ext.asyncio import AsyncSession

from models.user_model import UserModel
from schemas.user_schemas import User, UserCreate

class UserManager:
    @staticmethod
    async def insert_user(user_data: UserCreate, db: AsyncSession) -> User:
        user = UserModel(**user_data.model_dump())
        db.add(user)
        await db.commit()
        return User.model_validate(user)
