from fastapi import APIRouter   
from app.handler.user_handler import UserHandler

class UserRouter:
    def __init__(self, user_handler: UserHandler):
        self.user_handler = user_handler
        self.router = APIRouter()

    def setup_routes(self):
        self.router.post("/users")(self.user_handler.create_user)
        self.router.get("/users/{user_id}")(self.user_handler.get_user)
        self.router.put("/users/{user_id}")(self.user_handler.update_user)
        self.router.delete("/users/{user_id}")(self.user_handler.delete_user)