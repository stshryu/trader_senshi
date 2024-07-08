from typing import List, Union
from beanie import PydanticObjectId
from models.profile import Profile
from models.food import Food
from models.cold_brew import ColdBrew

profile_collection = Profile
food_collection = Food
cold_brew_collection = ColdBrew

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

########## Profile ##########  
async def add_profile(new_profile: Profile) -> Profile:
    profile = await new_profile.create()
    return profile

async def get_profile_by_username(username: str) -> Profile:
    profile = await profile_collection.find(Profile.username == username).first_or_none()
    return profile

