import logging
from typing import Union
from uuid import UUID
from sqlalchemy import select, text
from sqlalchemy.sql.expression import insert, update
from app.db.dataclasses import dish
from app.db.dataclasses.dish import Dish
from app.db.dataclasses.restaurant import Restaurnat
from app.db.exceptions import DatabaseClientError, DishDatabaseError, RestaurantDatabaseError 
from sqlalchemy.ext.asyncio import create_async_engine
from aiohttp import web
from .schema import meta, dishes, restaurants, orders, orders_to_dishes

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

    async def _create_dish(
        self, name: str,
        price: int, resturant_uuid: str
    ) -> str:
        """
        Internal method for creating dish
        """
        query_args = {
            'price': price,
            'name': name,
        }
        try:
            async with self.engine.begin() as conn:
                restaurant_id = await conn.execute(
                    select(restaurants)
                    .where(restaurants.c.external_id == resturant_uuid)
                )
                query_args['restaurant_id'] = restaurant_id.fetchone()[0]
                result = await conn.execute(
                    insert(dishes).returning(dishes.c.external_id),
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
            return dish_uuid.fetchall()
        except DishDatabaseError as err:
            raise DatabaseClientError(err)


    async def _read_dishes(self):
        """
        Internal method for selecting dish from database
        """
        try:
            async with self.engine.begin() as conn:
                prepeared = dishes.join(restaurants,
                    dishes.c.restaurant_id == restaurants.c.id
                )
                result = await conn.execute(
                    select(
                        dishes.c.name,
                        dishes.c.price,
                        dishes.c.external_id,
                        restaurants.c.external_id
                    ).select_from(prepeared)
                )
            return result
        except Exception as err:
            raise DishDatabaseError(err)

    async def read_dishes(self) -> list[Dish]:
        """
        External method for selecting dish from database
        """
        try:
            result = await self._read_dishes()
            return [
                Dish(
                    row[0],
                    row[1],
                    str(row[3]),
                    str(row[2])
                ) for row in result.fetchall()
            ]
        except DishDatabaseError as err:
            raise DatabaseClientError(err)


    async def _update_dish(self, dish_id: str, price=None, restaurant_id=None) -> Union[str, None]:
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
                prepeared = dishes.join(restaurants,
                    dishes.c.restaurant_id == restaurants.c.id
                )
                await conn.execute(
                    update(prepeared)
                    .where(dishes.c.external_id == dish_id)
                    .returning(
                        dishes.c.name,
                        dishes.c.price,
                        restaurants.c.external_id,
                        dishes.c.external_id
                    ),
                    query_args
                )
        except Exception as err:
            raise DishDatabaseError(
                args=[price, restaurant_id],
                message=err.args
            )

    async def update_dish(self, dish_id: str, price, restaurant_id) -> Dish:
        """
        External method for updating a dish
        """
        if price is None and restaurant_id is None:
            return None
        try:
            query = self._update_dish(
                dish_id,
                price,
                restaurant_id,
            ).fetchone()
            return Dish(query[0], query[1], query[2], query[3])
        except DishDatabaseError as err:
            raise DatabaseClientError(err)

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
                    insert(restaurants).returning(restaurants.c.external_id),
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
            raise RestaurantDatabaseError(err)

    async def read_restaurants(self) -> list[Restaurnat]:
        """
        External method for selecting dish from database
        """
        try:
            result = await self._read_restaurants()
            return [
                Restaurnat(str(row[1]), row[2], row[3]) for row in result.fetchall()
            ]
        except RestaurantDatabaseError as err:
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

    async def _read_orders(self):
        """
        Internal method for getting all the orders
        """
        try:
            async with self.engine.begin() as conn:
                await conn.execute(
                    select(orders),
                )
        except Exception as err:
            raise DishDatabaseError(
                message=err.args
            )

    async def read_orders(self):
        """
        External method for getting all the orders
        """
        try:
            result = await self._read_orders()
            print(result)
            return result
        except DishDatabaseError as err:
            raise DatabaseClientError(err)

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
