from fastapi import FastAPI, Depends
from config.config import init_db 
from contextlib import asynccontextmanager
from auth.jwt_bearer import JWTBearer
from routes.admin import router as AdminRouter
from routes.user import router as UserRouter

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello World" }

app.include_router(AdminRouter, tags=["Admin"], prefix="/admin",)
app.include_router(UserRouter, tags=["User"], prefix="/user", dependencies=[Depends(token_listener)],)
