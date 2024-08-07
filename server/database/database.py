from typing import List, Union
from beanie import PydanticObjectId
from models.food import Food
from models.cold_brew import ColdBrew
from models.admin import Admin
from models.user import User

profile_collection = Profile
food_collection = Food
cold_brew_collection = ColdBrew
admin_collection = Admin user_collection = User

########## Food ##########  
async def retrieve_foods() -> List[Food]:
    foods = await food_collection.all().to_list()
    return foods

async def add_food(new_food: Food) -> Food:
    food = await new_food.create()
    return food

async def retrieve_food(id: PydanticObjectId) -> Food:
    food = await food_collection.find(Food.id == id).first_or_none()
    return food

########## Cold Brew ##########  
async def retrieve_cold_brews(id: PydanticObjectId) -> List[ColdBrew]:
    cold_brews = await cold_brew_collection.find(ColdBrew.profile_id == id).to_list()
    return cold_brews

async def add_cold_brew(new_cb: ColdBrew) -> ColdBrew:
    cold_brew = await new_cb.create()
    return cold_brew

async def retrieve_cold_brew(id: PydanticObjectId) -> ColdBrew:
    cold_brew = await cold_brew_collection.find(ColdBrew.id == id).first_or_none()
    return cold_brew

########## User ##########  
async def add_user(new_user: User) -> User:
    user = await new_user.create()
    return user 

async def get_user_by_username(username: str) -> User:
    user = await user_collection.find(User.username == username).first_or_none()
    return user 

########## Admin ##########  
async def add_admin(new_admin: Admin) -> Admin:
    admin = await admin.create()
    return admin

async def get_admin_by_username(username: str) -> Admin:
    admin = await admin_collection.find(Admin.username == username).first_or_none()
    return admin
