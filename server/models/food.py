from typing import Optional, Any
from beanie import Document
from pydantic import BaseModel

class Food(Document):
    name: str
    calories: int
    description: str
    quantity: int
    origin: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Grilled Chicken",
                "calories": 300,
                "description": "Grilled chicken",
                "quantity": 5,
                "origin": "Whole Foods"
            }
        }
