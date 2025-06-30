from sqlmodel import SQLModel


class LoginSchema(SQLModel):
    username_or_email: str
    password: str
