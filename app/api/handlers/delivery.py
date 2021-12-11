import logging
from http import HTTPStatus
from aiohttp import web

from app.api.handlers.base_view import BaseView

logger = logging.getLogger(__name__)

class DeliveryPriceView(BaseView):
    URL = r'/api/v1/delivery/price'

    async def post(self) -> web.Response:
        logger.info('Calc delivery price')
        return web.json_response(status=HTTPStatus.OK)
