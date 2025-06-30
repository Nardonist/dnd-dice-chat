from typing import Annotated

from fastapi import APIRouter, Body, Header, Request, Response

from backend.auth.depends import LoginUseCaseDep, RegistrationUseCaseDep
from backend.auth.models import UserModel
from backend.auth.schemas import LoginSchema

router = APIRouter(prefix="/auth")


@router.post("/registration")
async def registration(
    registration_use_case: RegistrationUseCaseDep,
    user: UserModel,
    request: Request,
    response: Response,
    user_agent: Annotated[str | None, Header()] = None,
) -> None:
    await registration_use_case.register_user(
        user,
        response=response,
        user_agent=user_agent,
        request=request,
    )


@router.post("/login", status_code=200)
async def login(
    login_use_case: LoginUseCaseDep,
    response: Response,
    request: Request,
    login_schema: Annotated[LoginSchema, Body()],
    user_agent: Annotated[str | None, Header()] = None,
) -> None:
    await login_use_case.login(
        login_schema=login_schema,
        response=response,
        user_agent=user_agent,
        request=request,
    )
