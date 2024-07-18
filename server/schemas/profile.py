from pydantic import BaseModel, EmailStr
from fastapi.security import HTTPBasicCredentials

class ProfileSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": {"username": "jorgel", "password": "secret"}
        }

class ProfileData(BaseModel):
    username: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "username": "JorgeEl",
                "email": "jorgel@gmail.com"
            }
        }
