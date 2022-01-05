import logging
from http import HTTPStatus
from aiohttp import web

from app.api.handlers.base_view import BaseView
from app.db.exceptions import DatabaseClientError
from dataclasses import asdict

logger = logging.getLogger(__name__)

class RestaurantView(BaseView):
    URL = r'/api/v1/restaurants'

    async def get(self) -> web.Response:
        logger.info('restaurants service')
        try:
            logger.info('invoking db method')
            db_answer = await self.db.read_restaurants()
            logger.debug(f'db answer :{db_answer}')
            return web.json_response(list(map(asdict, db_answer)))
        except DatabaseClientError as err:
            return web.json_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
