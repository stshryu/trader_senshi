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


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation Successfull",
                "data": "{'sample_data': 'hi'}"
            }
        }
