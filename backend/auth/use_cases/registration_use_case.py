from datetime import datetime, timedelta, timezone

from fastapi import Request, Response

from backend.auth.models import UserModel
from backend.auth.services.session_service import SessionService
from backend.auth.services.user_service import UserService
from backend.auth.utils import convert_host_to_int
from backend.settings import SESSION_EXPIRE_SECONDS


class RegistrationUseCase:

    def __init__(self, user_service: UserService, session_service: SessionService) -> None:
        self.user_service = user_service
        self.session_service = session_service

    async def register_user(
        self,
        user: UserModel,
        user_agent: str | None,
        request: Request,
        response: Response,
    ) -> None:
        user = await self.user_service.create_new_user(user)
        if user_agent is None:
            user_agent = "unknow"
        host = 0
        if request.client is not None:
            host = convert_host_to_int(request.client.host)
        session = await self.session_service.create_new_session(user=user, agent=user_agent, host=host)
        response.set_cookie(
            "session",
            str(session.id),
            expires=datetime.now(timezone.utc) + timedelta(seconds=SESSION_EXPIRE_SECONDS),
        )
