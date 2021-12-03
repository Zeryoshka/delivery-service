from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import create_async_engine
from aiohttp import web

from app.config import Config

class DB:
    def __init__(self, config: Config) -> None:
        user = config.DB_USER
        password = config.DB_PASSWORD
        host = config.DB_HOST
        port = config.DB_PORT
        name = config.DB_NAME

        self.engine = create_async_engine(
            f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}'
        )

    async def ping(self) -> None:
        try:
            async with self.engine.begin() as conn:
                await conn.execute(
                    select(text('1'))
                )
        except Exception as err:
            raise web.HTTPInternalServerError(body=err)
