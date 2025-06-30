from uuid import UUID

from sqlmodel import select

from backend.auth.errors import UserDoesNotExsits
from backend.auth.models import UserModel
from backend.database import DBSession


class UserRepository:
    def __init__(self) -> None:
        pass

    async def create_new_user(self, user: UserModel) -> UserModel:
        async with DBSession() as session:
            session.add(user)
        return user

    async def get(
        self,
        user_id: UUID | None = None,
        username: str | None = None,
        email: str | None = None,
    ) -> UserModel:
        assert user_id is not None or username is not None or email is not None
        if user_id is not None:
            statement = select(UserModel).where((UserModel.id == user_id))
        elif email is not None:
            statement = select(UserModel).where((UserModel.email == email))
        else:
            statement = select(UserModel).where((UserModel.username == username))

        async with DBSession() as session:
            result = await session.execute(statement)
            user: UserModel | None = result.scalar_one_or_none()
            if user is None:
                raise UserDoesNotExsits
            return user
