from datetime import datetime, timedelta, timezone

from fastapi import Request, Response

from backend.auth.errors import LoginError, SessionDoesNotExsits, UserDoesNotExsits
from backend.auth.schemas import LoginSchema
from backend.auth.services.session_service import SessionService
from backend.auth.services.user_service import UserService
from backend.auth.utils import convert_host_to_int
from backend.settings import SESSION_EXPIRE_SECONDS


class LoginUseCase:

    def __init__(self, user_service: UserService, session_service: SessionService) -> None:
        self.user_service = user_service
        self.session_service = session_service

    async def login(
        self,
        login_schema: LoginSchema,
        response: Response,
        user_agent: str | None,
        request: Request,
    ) -> None:
        try:
            user = await self.user_service.get_user_by_username_or_email(
                username_or_email=login_schema.username_or_email
            )
        except UserDoesNotExsits:
            raise LoginError

        if not self.user_service.verify_passord(user=user, password=login_schema.password):
            raise LoginError

        if user_agent is None:
            user_agent = "unknow"

        host = 0
        if request.client is not None:
            host = convert_host_to_int(request.client.host)

        try:
            session = await self.session_service.get_session(agent=user_agent, host=host, user=user)
        except SessionDoesNotExsits:
            session = await self.session_service.create_new_session(user=user, agent=user_agent, host=host)
        response.set_cookie(
            "session",
            str(session.id),
            expires=datetime.now(timezone.utc) + timedelta(seconds=SESSION_EXPIRE_SECONDS),
        )
        response.status_code = 200
