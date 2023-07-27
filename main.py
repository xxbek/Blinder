from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from sqlalchemy import Column, Boolean, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

import settings
from sqlalchemy.dialects.postgresql import UUID
import uuid
import re


from pydantic import EmailStr
from pydantic import field_validator

from api.handlers import user_router


# API routes
app = FastAPI(title="Blinder-app")


main_api_router = APIRouter()
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
