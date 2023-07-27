from fastapi import Depends, APIRouter

from api.models import ShowUser, UserCreate
from db.dals import UserDAL
from db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

user_router = APIRouter()


async def _create_new_user(body: UserCreate, db) -> ShowUser:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name,
                email=body.email,
            )
            return ShowUser(user_id=user.user_id, name=user.name, email=user.email)


@user_router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _create_new_user(body, db)

