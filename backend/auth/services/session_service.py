from uuid import UUID

from backend.auth.models import SessionModel, UserModel
from backend.auth.repositories.session_repository import SessionRepository


class SessionService:
    def __init__(self, repository: SessionRepository) -> None:
        self.repository = repository
        pass

    async def create_new_session(self, agent: str, host: int, user: UserModel) -> SessionModel:
        session = await self.repository.create(SessionModel(user=user, user_id=user.id, agent=agent, host=host))
        return session

    async def get_session(
        self,
        session_id: UUID | None = None,
        agent: str | None = None,
        host: int | None = None,
        user: UserModel | None = None,
    ) -> SessionModel:
        session = await self.repository.get_one(
            pk=session_id,
            agent=agent,
            host=host,
            user_id=user.id if user is not None else None,
        )
        return session
