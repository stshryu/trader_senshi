from typing import Optional, Any
from fastapi.security import HTTPBasicCredentials
from beanie import Document
from pydantic import BaseModel, EmailStr

class Profile(Document):
    username: str,
    email: EmailStr,
    password: str

    class Config:
        json_schema_extra = { 
            "example": {
                "username": "JorgEl",
                "email": "jorgel@gmail.com",
                "password": "secret"
            }
        }

class ProfileSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": {
                "username": "jorgel@gmail.com",
                "password": "secret"
            }
        }

class ProfileData(BaseModel):
    username: str,
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "username": "JorgEl",
                "email": "jorgel@gmail.com"
            }
        }
