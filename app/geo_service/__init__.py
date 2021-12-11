from http import HTTPStatus
from aiohttp import ClientSession

from app.config import Config
from app.geo_service.exceptions import GeoApiError, RouteNotFound

URL_ROUTES = 'http://www.mapquestapi.com/directions/v2/routematrix'
class GeoService:

    def __init__(self, api_key: str, min_cost: int, money_for_meter: int) -> None:
        self.min_cost = min_cost
        self.money_for_meter = money_for_meter
        self.session = ClientSession()
        self.api_key = api_key

    async def _get_distance(self, start: str, end: str) -> int:
        if start == '' or end == '':
            raise ValueError()

        data = {'locations': [start, end]}
        params = {'key': self.api_key}
        async with self.session.get(
            URL_ROUTES, json=data, params=params
        ) as response:
            if response.status != HTTPStatus.OK:
                raise GeoApiError()
            api_response = await response.json()
        if 'distance' not in api_response:
            raise RouteNotFound()
        return int(api_response['distance'][1] * 1000)

    async def get_cost(self, start, end):
        distance = await self._get_distance(start, end)
        if distance is None or distance == 0:
            raise RouteNotFound()
        cost = int(max(self.min_cost, distance * self.money_for_meter))
        return cost

    async def close(self) -> None:
        await self.session.close()
