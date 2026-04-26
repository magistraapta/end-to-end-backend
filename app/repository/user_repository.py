from app.models.user_schema import UserSchema
from motor.motor_asyncio import AsyncIOMotorDatabase

class UserRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["users"]

    async def create_user(self, user: UserSchema):
        await self.collection.insert_one(user.model_dump())

    async def get_user(self, user_id: int):
        return await self.collection.find_one({"_id": user_id})
    
    async def update_user(self, user_id: int, user: UserSchema):
        await self.collection.update_one({"_id": user_id}, {"$set": user.model_dump()})

    async def delete_user(self, user_id: int):
        await self.collection.delete_one({"_id": user_id})
        
    async def get_all_users(self):
        return await self.collection.find().to_list(length=100)
    
    async def get_user_by_email(self, email: str):
        return await self.collection.find_one({"email": email})
    
    async def get_user_by_id(self, user_id: int):
        return await self.collection.find_one({"_id": user_id})
    
    async def get_user_by_name(self, name: str):
        return await self.collection.find_one({"name": name})