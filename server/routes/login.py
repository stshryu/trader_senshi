from fastapi import Body, APIRouter, HTTPException
import bcrypt

from models.admin import Admin
from models.user import User
from schemas.admin import AdminSignIn
from schemas.user import UserSignIn
from auth.auth import verify_password, create_access_token

router = APIRouter()

@router.post("/admin")
async def admin_login_with_username(admin_credentials: AdminSignIn=Body(...)):
    admin_exists = await Admin.find_one(Admin.username == admin_credentials.username)
    if admin_exists:
        password = verify_password(admin_credentials.password, admin_exists.password)
        if password:
            access_token = create_access_token({"sub": admin_exists.username}, None)
            return {"access_token": access_token, "token_type": "bearer"}

        raise HTTPException(status_code=403, detail="Incorrect email or password")
    raise HttpException(status_code=403, detail="Incorrect email or password")

@router.post("/user")
async def user_login_with_username(user_credentials: UserSignIn=Body(...)):
    user_exists = await User.find_one(User.username == user_credentials.username)
    if user_exists:
        password = verify_password(user_credentials.password, user_exists.password)
        if password:
            access_token = create_access_token({"sub": user_exists.username}, None)
            return {"access_token": access_token, "token_type": "bearer"}

        raise HTTPException(status_code=403, detail="Incorrect email or password")
    raise HttpException(status_code=403, detail="Incorrect email or password")

