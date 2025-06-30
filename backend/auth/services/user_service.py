import re
from uuid import UUID

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from backend.auth.models import UserModel
from backend.auth.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def get_user(self, user_id: UUID) -> UserModel:
        return await self.repository.get(user_id=user_id)

    async def get_user_by_username_or_email(self, username_or_email: str) -> UserModel:
        email_match = re.match(r"^\S+@\S+\.\S+$", username_or_email)
        if email_match:
            return await self.repository.get(email=username_or_email)
        return await self.repository.get(username=username_or_email)

    def hash_password(self, password: str) -> str:
        ph = PasswordHasher()
        hashed_password: str = ph.hash(password)
        return hashed_password

    def verify_passord(self, password: str, user: UserModel) -> bool:
        ph = PasswordHasher()
        try:
            return bool(ph.verify(user.password, password))
        except VerifyMismatchError:
            return False

    async def create_new_user(self, user_data: UserModel) -> UserModel:
        user_data.password = self.hash_password(user_data.password)
        await self.repository.create_new_user(user_data)
        return user_data
