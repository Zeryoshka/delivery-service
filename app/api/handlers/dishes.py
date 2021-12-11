import logging
from http import HTTPStatus
from aiohttp import web

from app.api.handlers.base_view import BaseView
from app.db.exceptions import DatabaseClientError

logger = logging.getLogger(__name__)

class OrderView(BaseView):
    URL = r'/api/v1/orders'

    async def get(self) -> web.Response:
        logger.info('orders service')
        try:
            logger.info('invoking db method')
            db_answer = await self.db.read_dishes()
            logger.debug(f'db answer :{db_answer}')
            return web.json_response(status=HTTPStatus.OK)
        except DatabaseClientError as err:
            return web.json_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
