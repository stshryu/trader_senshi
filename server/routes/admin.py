from fastapi import Body, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
import bcrypt

from database.database import add_admin
from models.admin import Admin
from schemas.admin import AdminData, AdminSignIn
from auth.auth import verify_password, get_password_hash, create_access_token

router = APIRouter()

@router.post("/login")
async def admin_login_with_username(admin_credentials: AdminSignIn = Body(...)):
    admin_exists = await Admin.find_one(Admin.username == admin_credentials.username)
    if admin_exists:
        password = verify_password(admin_credentials.password, admin_exists.password)
        if password:
            access_token = create_access_token({"sub": admin_exists.username}, None)
            return {"access_token": access_token, "token_type": "bearer"}

        raise HTTPException(status_code=403, detail="Incorrect email or password")
    raise HTTPException(status_code=403, detail="Incorrect email or password")


@router.post("", response_model=AdminData)
async def admin_signup(admin: Admin = Body(...)):
    admin_exists = await Admin.find_one(Admin.email == admin.email)
    if admin_exists:
        raise HTTPException(
            status_code=409, detail="Admin with email already exists"
        )

    admin.password = get_password_hash(admin.password)
    new_admin = await add_admin(admin)
    return new_admin
