import logging
from enum import Enum
from http import HTTPStatus
from aiohttp import ClientSession

from app.geo_service.exceptions import GeoApiError, RouteNotFound

logger = logging.getLogger(__name__)

class GeoApiMode(Enum):
    EXTERNAL_API = 'EXTERNAL_API'
    IN_PLACE_COUNTER = 'IN_PLACE_COUNTER'


URL_ROUTES = 'http://www.mapquestapi.com/directions/v2/routematrix'
class GeoService:

    def __init__(self, api_key: str, min_cost: int, money_for_meter: int, mode: str) -> None:
        self._min_cost = min_cost
        self._money_for_meter = money_for_meter
        self._session = ClientSession()
        self._mode = GeoApiMode(mode)
        if self._mode == GeoApiMode.IN_PLACE_COUNTER:
            self._get_distance = self._get_distance_in_place
        elif self._mode == GeoApiMode.EXTERNAL_API:
            if api_key is None:
                logger.error("Api key is None")
                raise ValueError()
            self._api_key = api_key
        else:
            raise ValueError(f'Incorrect GeoApiMode: {mode}')
        logger.info(f"Create geo service with mode {self._mode}")

    async def _get_distance(self, start: str, end: str) -> int:
        if start == '' or end == '':
            logger.debug('in get distance start ot end equal zero')
            raise ValueError()

        data = {'locations': [start, end]}
        params = {'key': self._api_key}
        async with self._session.get(
            URL_ROUTES, json=data, params=params
        ) as response:
            if response.status != HTTPStatus.OK:
                logger.info(f'Geo Api return status {response.status}')
                raise GeoApiError()
            api_response = await response.json()
        if 'distance' not in api_response:
            logger.info(f'Unrecognised format geo api response')
            raise RouteNotFound()
        return int(api_response['distance'][1] * 1000)

    async def get_cost(self, start, end):
        distance = await self._get_distance(start, end)
        if distance is None or distance == 0:
            raise RouteNotFound()
        cost = int(max(self._min_cost, distance * self._money_for_meter))
        return cost

    async def close(self) -> None:
        logger.info("Session closed")
        await self._session.close()

    async def _get_distance_in_place(self, start, end):
        return abs((hash(start) - hash(end))/10**15)
