from pydantic import BaseModel
from typing import Optional, Any


class UpdateFoodModel(BaseModel):
    name: Optional[str]
    calories: Optional[int]
    description: Optional[str]
    quantity: Optional[int]
    origin: Optional[str]

    class Collection:
        name = "Food"

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Apple",
                "calories": 100,
                "description": "An apple",
                "quantity": 20,
                "origin": "Farmers Market"
            }
        }
