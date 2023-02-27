from fastapi import FastAPI

from src.auth.router import router as auth_router

app = FastAPI()

app.include_router(router=auth_router, prefix="/auth", tags=["Auth"])