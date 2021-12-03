from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import create_async_engine
from aiohttp import web

class DB:
    def __init__(self) -> None:
        self.engine = create_async_engine(
            "postgresql+asyncpg://postgres:pass@localhost:5432/db"
        )

    async def ping(self) -> None:
        try:
            async with self.engine.begin() as conn:
                await conn.execute(
                    select(text("1"))
                )
        except Exception as err:
            print(type(err), err)
            raise web.HTTPInternalServerError(body=err)
