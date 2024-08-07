from typing import Optional, Any
from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
    username: str
    email: EmailStr
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "Superman",
                "email": "test@gmail.com",
                "password": "secret"
            }
        }

    class Settings:
        name = "user"

class UserSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": { "username": "test@gmail.com", "password": "secret" }
        }

class UserData(BaseModel):
    username: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "username": "Superman",
                "email": "test@gmail.com"
            }
        }
