from typing import Annotated

from fastapi import Depends

from backend.auth.repositories.session_repository import SessionRepository
from backend.auth.repositories.user_repository import UserRepository
from backend.auth.services.session_service import SessionService
from backend.auth.services.user_service import UserService
from backend.auth.use_cases.login_use_case import LoginUseCase
from backend.auth.use_cases.registration_use_case import RegistrationUseCase

user_repository = UserRepository()
session_repository = SessionRepository()

user_service = UserService(user_repository)
session_service = SessionService(session_repository)

registration_use_case = RegistrationUseCase(user_service=user_service, session_service=session_service)
login_use_case = LoginUseCase(user_service=user_service, session_service=session_service)


def get_regitration_use_case() -> RegistrationUseCase:
    return registration_use_case


def get_login_use_case() -> LoginUseCase:
    return login_use_case


RegistrationUseCaseDep = Annotated[RegistrationUseCase, Depends(get_regitration_use_case)]

LoginUseCaseDep = Annotated[LoginUseCase, Depends(get_login_use_case)]
