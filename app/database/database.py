from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self, app: FastAPI):
        self.app = app

    async def init_app(self):
        database_url = os.getenv("DATABASE_URL")
        database_name = os.getenv("DATABASE_NAME")
        
        self.mongodb_client = AsyncIOMotorClient(database_url)
        self.mongodb_db = self.mongodb_client[database_name]

        self.app.state.mongodb_client = self.mongodb_client
        self.app.state.mongodb_db = self.mongodb_db

        await self.mongodb_db.command("ping")

    async def close(self):
        self.mongodb_client.close()

        
