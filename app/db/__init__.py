from sqlalchemy import select, text
from sqlalchemy.sql.expression import insert, update
from app.db.dataclasses import dish
from app.db.dataclasses.dish import Dish
from app.db.dataclasses.restaurant import Restaurnat
from app.db.exceptions import DatabaseClientError, DishDatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from aiohttp import web
from .schema import meta, dishes, restaurants

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

    async def _create_dish(self, name: str, price: int, resturant_uuid: str) -> str:
        """
        Internal method for creating dish
        """
        query_args = {
            'price': price,
            'name': name,
            'restaurant_id': None
        }
        try:
            async with self.engine.begin() as conn:
                result = await conn.execute(
                    insert(dishes),
                    query_args
                )
            return result
        except Exception as err:
            raise DishDatabaseError(
                args=query_args,
                message=err.args
            )

    async def create_dish(self, dish: Dish) -> str:
        """
        External method for creating dish
        """
        try:
            dish_uuid = await self._create_dish(
                dish.name,
                dish.price,
                dish.restaurant_uuid
            )
        except DishDatabaseError as err:
            raise DatabaseClientError(err)


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

    async def read_dishes(self) -> list[Restaurnat]:
        """
        External method for selecting dish from database
        """
        try:
            result = await self._read_dishes()
            print(result)
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
                    update(dishes),
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
                    insert(restaurants),
                    query_args
                )
        except Exception as err:
            raise DishDatabaseError(
                args=query_args,
                message=err.args
            )

    async def _read_restaurants(self):
        """
        Internal method for reading restaurants
        """
        try:
            async with self.engine.begin() as conn:
                result = await conn.execute(
                    select(restaurants)
                )
            return result
        except Exception as err:
            raise DishDatabaseError(err)

    async def read_restaurants(self) -> list[Restaurnat]:
        """
        External method for selecting dish from database
        """
        try:
            result = await self._read_restaurants()
            return [
                Restaurnat(row[1], row[2], row[3]) for row in result.fetchall()
            ]
        except DishDatabaseError as err:
            raise DatabaseClientError(err)

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
                    update(restaurants),
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
