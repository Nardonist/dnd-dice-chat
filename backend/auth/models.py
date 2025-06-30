from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel


class UserModel(SQLModel, table=True):
    __tablename__ = "user"  # type: ignore

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(max_length=512)
    username: str = Field(max_length=512)
    password: str = Field()
    fullname: str | None = None
    sessions: list["SessionModel"] = Relationship(back_populates="user")


class SessionModel(SQLModel, table=True):
    __tablename__ = "session"  # type: ignore

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    user: UserModel = Relationship(back_populates="sessions")
    last_login: datetime = Field(default_factory=datetime.now)
    agent: str
    host: int
