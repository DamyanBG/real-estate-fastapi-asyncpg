from fastapi import FastAPI

from routers.router import main_router

app = FastAPI()
app.include_router(main_router)
