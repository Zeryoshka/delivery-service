from dataclasses import asdict
import logging
from http import HTTPStatus
from aiohttp import web
from pydantic.error_wrappers import ValidationError

from app.db.dataclasses import Order
from app.api.handlers.base_view import BaseView
from app.api.schemas.request_schemas import CreateOrderRequestSchema
from app.db.exceptions import DatabaseClientError

logger = logging.getLogger(__name__)

class OrdersView(BaseView):
    URL = r'/api/v1/orders'

    async def get(self) -> web.Response:
        logger.info('get orders')
        db_response = await self.db.read_orders()
        logger.debug(f'db answer :{db_response}')
        return web.json_response(
                list(map(asdict, db_response))
            )

    async def post(self) -> web.Response:
        logger.info('create order')
        try:
            data = CreateOrderRequestSchema.parse_raw(
                await self.request.text()
            )
            new_order = Order(
                content=data.dishes,
                restaurant=data.restaurant,
                comment=data.comment
            )
            logger.info('invoking db method')
            db_response = await self.db.create_order(new_order)
        except DatabaseClientError as err:
            logger.error(f'Database client error: {err}')
            raise web.HTTPInternalServerError()
        except ValidationError as err:
            logger.debug(f'Error parsing delivery price: {err}')
            raise web.HTTPBadRequest()
        return web.json_response(
            { 'order_id' : str(db_response[0][0])},
            status=HTTPStatus.CREATED
        )


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
