from app.repository.user_repository import UserRepository
from app.models.user_schema import UserSchema
from fastapi import HTTPException
import hashlib

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user: UserSchema):
        if await self.user_repository.get_user_by_email(user.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        user.password = hashlib.sha256(user.password.encode()).hexdigest()

        return await self.user_repository.create_user(user)
    
    async def get_user(self, user_id: int):
        return await self.user_repository.get_user(user_id)
    
    async def update_user(self, user_id: int, user: UserSchema):
        user.password = hashlib.sha256(user.password.encode()).hexdigest()

        return await self.user_repository.update_user(user_id, user)
    
    async def delete_user(self, user_id: int):
        return await self.user_repository.delete_user(user_id)
    
    async def get_all_users(self):
        return await self.user_repository.get_all_users()
    
    async def get_user_by_email(self, email: str):
        return await self.user_repository.get_user_by_email(email)