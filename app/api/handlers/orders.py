import logging
from http import HTTPStatus
from aiohttp import web

from app.api.handlers.base_view import BaseView

logger = logging.getLogger(__name__)

class OrdersView(BaseView):
    URL = r'/api/v1/orders'

    async def get(self) -> web.Response:
        logger.info('get orders')
        return web.json_response(status=HTTPStatus.OK)

    async def post(self) -> web.Response:
        logger.info('create order')
        return web.json_response(status=HTTPStatus.OK)


class OneOrderView(BaseView):
    URL = r'/api/v1/orders/{order_id}'

    async def get(self) -> web.Response:
        logger.info('get order')
        return web.json_response(status=HTTPStatus.OK)

    async def delete(self) -> web.Response:
        logger.info('delete order')
        return web.json_response(status=HTTPStatus.OK)

class OrderStatusView(BaseView):
    URL = r'/api/v1/orders/{order_id}/status'
    async def patch(self) -> web.Response:
        logger.info('update order status')
        return web.json_response(status=HTTPStatus.OK)
