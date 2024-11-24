from datetime import datetime, timedelta, timezone
from config.config import Settings
import jwt
import bcrypt

SECRET_KEY = Settings().SECRET_KEY
ALGORITHM = Settings().ALGORITHM

def verify_password(password, password_hash):
    return bcrypt.checkpw(
        bytes(password, encoding="utf-8"),
        bytes(password_hash, encoding="utf-8"),
    )

def get_password_hash(password):
    return bcrypt.hashpw(
        bytes(password, encoding="utf-8"),
        bcrypt.gensalt(),
    )

def create_access_token(data: dict, expires_delta: timedelta |  None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_jwt(token: str) -> dict:
    decoded_token = jwt.decode(token.encode(), SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_token if decoded_token["exp"] >= int(datetime.now(timezone.utc).timestamp()) else {}
