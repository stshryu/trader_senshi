from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello World" }
