from dataclasses import asdict
import logging
from http import HTTPStatus
from aiohttp import web
from pydantic import ValidationError

from app.api.handlers.base_view import BaseView
from app.api.schemas.request_schemas import CreateDishRequestSchema
from app.db.dataclasses.dish import Dish
from app.db.exceptions import DatabaseClientError

logger = logging.getLogger(__name__)

class DishView(BaseView):
    URL = r'/api/v1/dishes'

    async def get(self) -> web.Response:
        logger.info('invoking dishes service')
        try:
            logger.info('invoking db method')
            db_response = await self.db.read_dishes()
            logger.debug(f'db answer :{db_response}')
            return web.json_response(
                list(map(asdict, db_response))
            )
        except DatabaseClientError as err:
            logger.warn(f'DB error in get dishes handler: {err}')
            raise web.HTTPInternalServerError()

    async def post(self) -> web.Response:
        logger.info('invoking dishes service')
        try:
            data = CreateDishRequestSchema.parse_raw(
                await self.request.text()
            )
            new_dish = Dish(
                price=data.price,
                name=data.name,
                restaurant_uuid=data.restaurant
            )
        except ValidationError as err:
            logger.debug(f'Error parsing delivery price: {err}')
            raise web.HTTPBadRequest()

        logger.info('invoking db method')
        try:
            db_answer = await self.db.create_dish(new_dish)
        except DatabaseClientError as err:
            logger.error(err)
            raise web.HTTPInternalServerError()
        return web.json_response({ 'dish_id': str(db_answer[0][0]) }, status=HTTPStatus.CREATED)

class OneDishView(BaseView):
    URL = r'/api/v1/dishes/{dish_id}'

    async def get(self) -> web.Response:
        logger.info('get dish')
        return web.json_response(status=HTTPStatus.OK)
