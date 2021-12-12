import json
import logging
from http import HTTPStatus
from aiohttp import web

from app.api.handlers.base_view import BaseView
from app.db.dataclasses.dish import Dish
from app.db.exceptions import DatabaseClientError

logger = logging.getLogger(__name__)

class OrderView(BaseView):
    URL = r'/api/v1/dishes'

    async def get(self) -> web.Response:
        logger.info('invoking dishes service')
        try:
            logger.info('invoking db method')
            db_answer = await self.db.read_dishes()
            logger.debug(f'db answer :{db_answer}')
            return web.json_response(status=HTTPStatus.OK)
        except DatabaseClientError as err:
            return web.json_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

    async def post(self) -> web.Response:
        logger.info('invoking dishes service')
        try:
            incoming_body = await self.request.json()
            logger.info('invoking db method')
            db_answer = await self.db.create_dish(
                Dish(
                    price=incoming_body['price'],
                    name=incoming_body['name']
                )
            )
            return web.json_response(incoming_body)
        except json.JSONDecodeError as err:
            logger.error(err)
            return web.json_response(status=HTTPStatus.BAD_REQUEST)
        except DatabaseClientError as err:
            logger.error(err)
            return web.json_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
