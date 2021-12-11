from sqlalchemy import select, text
from sqlalchemy.sql.expression import insert, update
from app.db.exceptions import DatabaseClientError, DishDatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from aiohttp import web
from .schema import meta, dishes

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


    async def _clear_initialize(self):
        """
        Method for db init,
        Removes all previous data
        """
        async with self.engine.begin() as conn:
            await conn.run_sync(meta.drop_all)
            await conn.run_sync(meta.create_all)

    async def _create_dish(self, price, resturant_id) -> str:
        """
        Internal method for creating dish
        """
        query_args = {
            'price': price,
            'restaurant_id': resturant_id
        }
        try:
            async with self.engine.begin() as conn:
                result = await conn.execute(
                    insert(table='Dishes'),
                    query_args
                )
                return result
        except Exception as err:
            raise DishDatabaseError(
                args=query_args,
                message=err.args
            )

    async def _read_dishes(self):
        """
        Internal method for selecting dish from database
        """
        try:
            async with self.engine.begin() as conn:
                result = await conn.execute(
                    select(dishes)
                )
                return result
        except Exception as err:
            raise DishDatabaseError(err)

    async def read_dishes(self):
        """
        External method for selecting dish from database
        """
        try:
            result = await self._read_dishes()
            return result
        except DishDatabaseError as err:
            raise DatabaseClientError(err)


    async def _update_dish(self, price=None, restaurant_id=None) -> None | str:
        """
        Internal method for updating a dish
        """
        if price is None and restaurant_id is None:
            return None
        query_args = dict()
        if price is not None:
            query_args['price'] = price
        if restaurant_id is not None:
            query_args['restaurant_id'] = restaurant_id
        try:
            async with self.engine.begin() as conn:
                await conn.execute(
                    update(table='Dishes'),
                    query_args
                )
        except Exception as err:
            raise DishDatabaseError(
                args=[price, restaurant_id],
                message=err.args
            )

    async def _create_restaurant(self, name, coords):
        """
        Internal method for creating restaurant
        """
        query_args = {
            'coords': coords,
            'name': name
        }
        try:
            async with self.engine.begin() as conn:
                await conn.execute(
                    insert(table='Restaurants'),
                    query_args
                )
        except Exception as err:
            raise DishDatabaseError(
                args=query_args,
                message=err.args
            )

    async def _update_restaurant(self, name, coords):
        """
        Internal method for creating restaurant
        """
        query_args = {
            'coords': coords,
            'name': name
        }
        try:
            async with self.engine.begin() as conn:
                await conn.execute(
                    update(table='Dishes'),
                    query_args
                )
        except Exception as err:
            raise DishDatabaseError(
                args=query_args,
                message=err.args
            )

    async def ping(self) -> None:
        """
        Method for testing connection to DB
        """
        try:
            async with self.engine.begin() as conn:
                await conn.execute(
                    select(text('1'))
                )
        except Exception as err:
            raise web.HTTPInternalServerError(body=err)
