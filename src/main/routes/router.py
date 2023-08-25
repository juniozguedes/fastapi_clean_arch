from fastapi import FastAPI
from posts_routes import router as posts_router


def generate_routes(app: FastAPI):
    app.include_router(posts_router)
