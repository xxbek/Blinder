import re
import uuid
from pydantic import BaseModel, EmailStr, field_validator
from fastapi import HTTPException

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class ConfigDict:
        """Tells pydantic to cover even non dict obj to json"""

        from_attributes = True


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    email: EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr

    @field_validator('name')
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail="Name should contain only letters")
        return value
