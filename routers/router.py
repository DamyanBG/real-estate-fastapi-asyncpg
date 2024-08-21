from fastapi import APIRouter

from routers import home_router, user_router, image_router

main_router = APIRouter()
main_router.include_router(home_router.home_router)
main_router.include_router(user_router.user_router)
main_router.include_router(image_router.image_router)
