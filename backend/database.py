from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from backend.settings import POSTGRES_URL

engine = create_async_engine(POSTGRES_URL, echo=True, future=True)

DBSession = async_sessionmaker(engine, expire_on_commit=False)
