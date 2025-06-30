from uuid import UUID

from sqlmodel import select

from backend.auth.errors import SessionDoesNotExsits
from backend.auth.models import SessionModel
from backend.database import DBSession


class SessionRepository:
    def __init__(self) -> None:
        pass

    async def create(self, session: SessionModel) -> SessionModel:
        async with DBSession() as db_session:
            db_session.add(session)
            await db_session.commit()
        return session

    async def get_one(
        self,
        pk: UUID | None,
        agent: str | None = None,
        host: int | None = None,
        user_id: UUID | None = None,
    ) -> SessionModel:
        assert pk is not None or agent is not None or host is not None
        async with DBSession() as db_session:
            if pk is not None:
                statement = select(SessionModel).where(SessionModel.id == pk)
            else:
                statement = select(SessionModel).where(SessionModel.agent == agent and SessionModel.host == host)
            if user_id is not None:
                statement = statement.where(SessionModel.user_id == user_id)
            result = await db_session.execute(statement)
            session: SessionModel | None = result.scalar_one_or_none()
            if session is None:
                raise SessionDoesNotExsits
            return session
