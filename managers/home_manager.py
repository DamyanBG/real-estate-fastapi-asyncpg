from sqlalchemy.ext.asyncio import AsyncSession

from models.home_model import HomeModel
from schemas.home_schemas import Home, HomeCreate


class HomeManager:
    @staticmethod
    async def insert_home(home_data: HomeCreate, db: AsyncSession) -> Home:
        home = HomeModel(**home_data.model_dump())
        db.add(home)
        await db.commit()
        return Home.model_validate(home)
