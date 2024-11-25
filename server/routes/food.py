from fastapi import Body, APIRouter, HTTPException, Response, status
from beanie import PydanticObjectId

from database.database import retrieve_all_foods, create_food, retrieve_food, remove_food
from models.food import Food
from schemas.food import UpdateFoodModel

router = APIRouter()

@router.get("/get_all_foods")
async def get_all_foods(response: Response):
    food_list = await retrieve_all_foods()
    response.status_code = status.HTTP_200_OK
    return food_list

@router.post("/add_food")
async def add_food(response: Response, food: Food=Body(...)):
    new_food = await create_food(food)
    response.status_code = status.HTTP_201_CREATED
    return new_food

@router.post("/delete_food/{food_id}")
async def delete_food(response: Response, food_id: PydanticObjectId):
    deleted_food_id = await remove_food(food_id)
    if deleted_food_id:
        response.status_code = status.HTTP_200_OK
        return f"Deleted Food ID: {deleted_food_id}"
    return HTTPException(status_code=404, detail=f"Food with id: {food_id} not found")

@router.get("/get_food/{food_id}")
async def get_food(response: Response, food_id: PydanticObjectId):
    food_exists = await retrieve_food(food_id)
    if food_exists:
        response.status_code = status.HTTP_200_OK
        return food_exists
    return HTTPException(status_code=404, detail=f"Food with id: {food_id} not found")

