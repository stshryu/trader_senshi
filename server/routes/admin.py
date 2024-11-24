from fastapi import Body, APIRouter, HTTPException
import bcrypt

from database.database import add_admin
from models.admin import Admin
from schemas.admin import AdminData 
from auth.auth import get_password_hash

router = APIRouter()

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
