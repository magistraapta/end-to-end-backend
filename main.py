from fastapi import FastAPI
from app.database.database import Database
from app.repository.user_repository import UserRepository
from app.service.user_service import UserService
from app.handler.user_handler import UserHandler
from app.router.user_router import UserRouter
from contextlib import asynccontextmanager
import uvicorn
from fastapi.responses import JSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    database = Database(app)
    await database.init_app()

    user_repository = UserRepository(app.state.mongodb_db)
    user_service = UserService(user_repository)
    user_handler = UserHandler(user_service)
    user_router = UserRouter(user_handler)
    user_router.setup_routes()

    app.include_router(user_router.router)
    app.state.database = database

    try:
        yield
    finally:
        await database.close()


fastapi = FastAPI(lifespan=lifespan)

@fastapi.get("/health")
async def health():
    return JSONResponse(status_code=200, content={"message": "server running"})



if __name__ == "__main__":
    uvicorn.run(fastapi, host="0.0.0.0", port=8000)
