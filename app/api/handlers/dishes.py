import logging
from http import HTTPStatus
from aiohttp import web

from app.api.handlers.base_view import BaseView

logger = logging.getLogger(__name__)

class DishesView(BaseView):
    URL = r'/api/v1/dishes'

    async def get(self) -> web.Response:
        logger.info('get dished')
        return web.json_response(status=HTTPStatus.OK)

    async def post(self) -> web.Response:
        logger.info('create dish')
        return web.json_response(status=HTTPStatus.OK)


class OneDishView(BaseView):
    URL = r'/api/v1/dishes/{dish_id}'

    async def get(self) -> web.Response:
        logger.info('get dish')
        return web.json_response(status=HTTPStatus.OK)
