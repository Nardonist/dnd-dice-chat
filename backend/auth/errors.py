from typing import Dict

from fastapi import HTTPException


class SessionDoesNotExsits(ValueError):
    pass


class UserDoesNotExsits(ValueError):
    pass


class LoginError(HTTPException):
    def __init__(
        self,
        status_code: int = 401,
        detail: str = "Invalid credentials",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)
