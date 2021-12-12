import logging
from http import HTTPStatus
from aiohttp import web

from app.api.handlers.base_view import BaseView

logger = logging.getLogger(__name__)

class DeliveryPriceView(BaseView):
    URL = r'/api/v1/delivery/price'

    async def post(self) -> web.Response:
        logger.info('Calc delivery price')
        req = await self.request.json()
        cost = await self.geo_service.get_cost(req['start'], req['end'])
        return web.json_response(data={'price': cost}, status=HTTPStatus.OK)
