from fastapi import FastAPI

from routers import router as houses_router

app = FastAPI(
    title="Tech Challenge API",
    description="API for the Tech Challenge",
    version="1.0.0",
)

app.include_router(houses_router)
