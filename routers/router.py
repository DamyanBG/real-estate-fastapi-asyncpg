from fastapi import APIRouter

from routers.home_router import home_router

main_router = APIRouter()
main_router.include_router(home_router)
