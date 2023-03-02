from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.auth.router import router as auth_router
from src.storage.router import router as storage_router

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
def handle_validation_error(request, exc):
    return JSONResponse(status_code=422, content={"detail": "Invalid request payload"})


app.include_router(router=auth_router, prefix="/auth", tags=["Auth"])
app.include_router(router=storage_router, prefix="/storage", tags=["Storage"])
