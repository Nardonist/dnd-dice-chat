from fastapi import FastAPI

from backend.auth.routing import router as auth_router

app = FastAPI()

app.include_router(auth_router)
