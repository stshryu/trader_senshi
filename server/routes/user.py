from fastapi import Body, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
import bcrypt

from database.database import add_user 
from models.user import User
from schemas.user import UserData, UserSignIn 
from auth.auth import verify_password, get_password_hash, create_access_token

router = APIRouter()

@router.post("/login")
async def user_login_with_username(user_credentials: UserSignIn=Body(...)):
    user_exists = await User.find_one(User.username == user_credentials.username)
    if user_exists:
        password = verify_password(user_credentials.password, user_exists.password)
        if password:
            access_token = create_access_token({"sub": user_exists.username}, None)
            return {"access_token": access_token, "token_type": "bearer"}

        raise HTTPException(status_code=403, detail="Incorrect email or password")
    raise HTTPException(status_code=403, detail="Incorrect email or password")


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
