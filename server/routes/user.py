from fastapi import Body, APIRouter, HTTPException
import bcrypt

from database.database import add_user 
from models.user import User
from schemas.user import UserData
from auth.auth import get_password_hash 

router = APIRouter()

@router.post("", response_model=UserData)
async def user_signup(user: User=Body(...)):
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(
            status_code=409, detail="User with email already exists"
        )

    user.password = get_password_hash(user.password)
    new_user = await add_user(user)
    return new_user 
