from fastapi import FastAPI
from .routers import auth
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.on_event("startup")
async def startup():
    pass  # No caching setup needed

@app.on_event("shutdown")
async def shutdown():
    pass  # No caching shutdown needed
