from app.service.user_service import UserService
from app.models.user_schema import UserSchema
from bson import ObjectId
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

class UserHandler:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def json_response(self, status_code: int, content):
        return JSONResponse(
            status_code=status_code,
            content=jsonable_encoder(content, custom_encoder={ObjectId: str}),
        )

    async def create_user(self, user: UserSchema):
        return self.json_response(status_code=201, content=await self.user_service.create_user(user))
    
    async def get_user(self, user_id: int):
        user = await self.user_service.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.json_response(status_code=200, content=user)
    
    async def update_user(self, user_id: int, user: UserSchema):
        user = await self.user_service.update_user(user_id, user)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.json_response(status_code=200, content=user)
    
    async def delete_user(self, user_id: int):
        user = await self.user_service.delete_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.json_response(status_code=200, content=user)
    
    async def get_all_users(self):
        return self.json_response(status_code=200, content=await self.user_service.get_all_users())
    
    async def get_user_by_email(self, email: str):
        return self.json_response(status_code=200, content=await self.user_service.get_user_by_email(email))