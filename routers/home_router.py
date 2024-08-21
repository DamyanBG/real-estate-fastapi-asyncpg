from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from schemas.home_schemas import HomeCreate, Home
from managers.home_manager import HomeManager

home_router = APIRouter(prefix="/homes", tags=["home"])

@home_router.post("/", response_model=Home, status_code=status.HTTP_201_CREATED)
async def post_home(home_data: HomeCreate, db: AsyncSession = Depends(get_db)):
    home = await HomeManager.insert_home(home_data, db)
    return home
