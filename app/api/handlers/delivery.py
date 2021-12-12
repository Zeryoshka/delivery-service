import logging
import json
from http import HTTPStatus
from aiohttp import web
from pydantic import ValidationError
from pydantic.json import pydantic_encoder

from app.api.handlers.base_view import BaseView
from app.api.schemas.request_schemas import DeliveryPriceRequestSchema
from app.api.schemas.response_schemas import DeliveryPriceResponseSchema
from app.geo_service.exceptions import GeoApiError, RouteNotFound

logger = logging.getLogger(__name__)

class DeliveryPriceView(BaseView):
    URL = r'/api/v1/delivery/price'

    async def post(self) -> web.Response:
        logger.info('Calc delivery price')
        try:
            data = DeliveryPriceRequestSchema.parse_raw(
                await self.request.text()
            )
        except ValidationError as err:
            logger.debug(f'Error parsing delivery price: {err}')
            raise web.HTTPBadRequest()

        try:
            cost = await self.geo_service.get_cost(data.start, data.end)
        except RouteNotFound:
            logger.info('Route not found by API')
            raise web.HTTPNotFound()
        except GeoApiError:
            logger.info('GeoApi error')
            raise web.HTTPInternalServerError()

        response_data = DeliveryPriceResponseSchema(price = cost)
        return web.Response(
            text=json.dumps(response_data, default=pydantic_encoder),
            headers={'Content-Type': 'application/json'},
            status=HTTPStatus.OK
        )
