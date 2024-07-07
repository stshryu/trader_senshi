from beanie import Document
from fastapi.security import HTTPBaseCredentials
from pydantic import BaseModel, EmailStr

class ColdBrew(Document):
    brew_length: int
    bean_type: str
    bean_grind: str
    profile_id: str

    class Config:
        json_schema_extra = {
            "example": {
                "brew_length": 30,
                "bean_type": "Blank Space Coffee",
                "bean_grind": "Fine",
                "profle_id": "abcdefg123456"
            }
        }

    class Settings:
        name = "ColdBrew"
